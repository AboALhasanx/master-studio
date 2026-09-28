"""Transport boundary (roadmap gates G1 -> G2).

* **G1** shipped only a mock, so the code could not reach the network (SP1).
* **G2** adds :class:`HttpTransport`: a stdlib-only Bot API client whose
  payload is always ASCII-safe (``json.dumps(..., ensure_ascii=True)``) — the
  terminal-encoding fix proven during the manual smoke test — plus:
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
import urllib.request
from typing import Any, Protocol, runtime_checkable

from .errors import GatewayNotReady, RateLimited, TransportError

__all__ = ["Transport", "MockTransport", "HttpTransport", "RateLimitedScript", "build_transport"]


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
        # ensure_ascii keeps Arabic/Persian payloads encoding-independent — the
        # exact failure seen with curl in the terminal (mangled to '?').
        body = json.dumps(params, ensure_ascii=True).encode("ascii")
        request = urllib.request.Request(
            url, data=body, headers={"Content-Type": "application/json"}
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
