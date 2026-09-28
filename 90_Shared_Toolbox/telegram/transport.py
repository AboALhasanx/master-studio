"""Transport boundary (roadmap gates G1 -> G2).

* **G1** shipped only a mock, so the code could not reach the network (SP1).
* **G2** adds :class:`HttpTransport`: a stdlib-only Bot API client whose
  payload is always ASCII-safe (``json.dumps(..., ensure_ascii=True)``) — the
  terminal-encoding fix proven during the manual smoke test — plus:
    * local ``file://`` payloads -> ``multipart/form-data`` (Telegram 400s on a
      file URI sent as JSON, so uploads are a different wire format entirely),
    * 429 -> :class:`~telegram.errors.RateLimited` with ``retry_after``,
    * other API/HTTP failures -> :class:`~telegram.errors.TransportError`,
    * missing token -> :class:`~telegram.errors.GatewayNotReady` (exit 5).

The interface (``call(method, params)``) is identical for both transports, so
the executor, CLI and tests never branch on which one is installed.
"""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.parse
import urllib.request
import uuid
from pathlib import Path
from typing import Any, Protocol, runtime_checkable

from .errors import GatewayNotReady, RateLimited, TransportError

__all__ = ["Transport", "MockTransport", "HttpTransport", "RateLimitedScript", "build_transport"]

#: Bot API parameters that can carry a file upload.
_UPLOAD_PARAMS = frozenset(
    {"document", "photo", "video", "audio", "voice", "animation", "thumb", "sticker"}
)


def _split_uploads(params: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    """Separate local ``file://`` uploads from the plain scalar fields.

    Telegram's Bot API answers 400 ("wrong file identifier/HTTP URL
    specified") for a ``file://`` value sent as JSON, so anything meant to be
    uploaded has to leave as multipart instead.
    """
    fields: dict[str, Any] = {}
    files: dict[str, str] = {}
    for key, value in params.items():
        if key in _UPLOAD_PARAMS and isinstance(value, str) and value.startswith("file://"):
            files[key] = value
        else:
            fields[key] = value
    return fields, files


def _local_path(uri: str) -> Path:
    """``file:///C:/a/b.pdf`` -> ``WindowsPath`` (stdlib URL->path conversion)."""
    return Path(urllib.request.url2pathname(urllib.parse.urlparse(uri).path))


def _encode_multipart(fields: dict[str, Any], files: dict[str, str]) -> tuple[bytes, str]:
    """Build the ``multipart/form-data`` body the Bot API accepts for uploads."""
    boundary = uuid.uuid4().hex
    out = bytearray()

    for name, value in fields.items():
        if value is None:
            continue
        text = "true" if value is True else "false" if value is False else str(value)
        out += f"--{boundary}\r\n".encode("ascii")
        out += f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode("utf-8")
        out += text.encode("utf-8")
        out += b"\r\n"

    for name, uri in files.items():
        path = _local_path(uri)
        if not path.is_file():
            raise TransportError(f"file not found for '{name}': {path}")
        filename = path.name.replace('"', "")
        out += f"--{boundary}\r\n".encode("ascii")
        out += (
            f'Content-Disposition: form-data; name="{name}"; filename="{filename}"\r\n'
            .encode("utf-8")
        )
        out += b"Content-Type: application/octet-stream\r\n\r\n"
        out += path.read_bytes()
        out += b"\r\n"

    out += f"--{boundary}--\r\n".encode("ascii")
    return bytes(out), f"multipart/form-data; boundary={boundary}"


@runtime_checkable
class Transport(Protocol):
    """Minimal Bot-API-shaped surface the executor drives."""

    is_live: bool

    def call(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        """Invoke a Bot API method and return its ``result`` payload."""
        ...


class RateLimitedScript(Exception):
    """Placeholder used inside a script to simulate a 429 mid-sequence."""

    def __init__(self, retry_after: float = 3.0):
        super().__init__(f"rate limited (retry after {retry_after}s)")
        self.retry_after = retry_after


class MockTransport:
    """Recording transport: no sockets, deterministic, scriptable (gate G1)."""

    is_live = False

    def __init__(self, script: list[Any] | None = None):
        self.calls: list[tuple[str, dict[str, Any]]] = []
        self.script: list[Any] = list(script or [])
        self._next_id = 100_000

    def call(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        self.calls.append((method, dict(params)))
        if self.script:
            item = self.script.pop(0)
            if isinstance(item, RateLimitedScript):
                raise RateLimited(f"simulated 429 on {method}", retry_after=item.retry_after)
            if isinstance(item, BaseException):
                raise item
            if isinstance(item, dict):
                return item
        self._next_id += 1
        return {"message_id": self._next_id, "ok": True}

    def methods(self) -> list[str]:
        return [m for m, _ in self.calls]

    def last(self) -> tuple[str, dict[str, Any]]:
        return self.calls[-1]


class HttpTransport:
    """Live Bot API client (gate G2). Stdlib only, ASCII-safe payloads."""

    is_live = True

    def __init__(self, token: str, base_url: str = "https://api.telegram.org",
                 timeout: float = 30.0):
        if not token:
            raise GatewayNotReady("live transport needs TELEGRAM_BOT_TOKEN (set it in .env)")
        self.token = token
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def call(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        url = f"{self.base_url}/bot{self.token}/{method}"
        fields, files = _split_uploads(params)
        if files:
            body, content_type = _encode_multipart(fields, files)
        else:
            # ensure_ascii keeps Arabic/Persian payloads encoding-independent — the
            # exact failure seen with curl in the terminal (mangled to '?').
            body = json.dumps(params, ensure_ascii=True).encode("ascii")
            content_type = "application/json"
        request = urllib.request.Request(
            url, data=body, headers={"Content-Type": content_type}
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                payload = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            payload = self._error_payload(exc)
        except urllib.error.URLError as exc:
            raise TransportError(f"network error on {method}: {getattr(exc, 'reason', exc)}") from exc
        except TimeoutError as exc:
            raise TransportError(f"timeout on {method}") from exc
        return self._interpret(payload, method)

    @staticmethod
    def _error_payload(exc: urllib.error.HTTPError) -> dict[str, Any]:
        try:
            return json.loads(exc.read().decode("utf-8"))
        except Exception:  # noqa: BLE001 - never mask the original failure
            return {"ok": False, "error_code": getattr(exc, "code", 0),
                    "description": str(getattr(exc, "reason", "http error"))}

    @staticmethod
    def _interpret(payload: Any, method: str) -> dict[str, Any]:
        if isinstance(payload, dict) and payload.get("ok"):
            return payload.get("result") or {}
        if not isinstance(payload, dict):
            raise TransportError(f"unexpected response on {method}: {payload!r}")
        code = payload.get("error_code")
        description = str(payload.get("description", ""))
        retry = (payload.get("parameters") or {}).get("retry_after")
        if code == 429 or "Too Many Requests" in description:
            raise RateLimited(f"429 on {method}: {description}",
                              retry_after=float(retry or 1))
        raise TransportError(f"{code} on {method}: {description}")


def build_transport(live: bool = False, token: str | None = None) -> Transport:
    """Return the transport for the requested mode.

    Gate G1 raised for ``live=True``; gate G2 returns a real
    :class:`HttpTransport` once ``TELEGRAM_BOT_TOKEN`` is available, and still
    fails loudly (exit 5) when it is not.
    """
    if live:
        token = token if token is not None else os.environ.get("TELEGRAM_BOT_TOKEN", "")
        if not token:
            raise GatewayNotReady(
                "live mode needs TELEGRAM_BOT_TOKEN in .env (or pass a token)"
            )
        return HttpTransport(token)
    return MockTransport()
