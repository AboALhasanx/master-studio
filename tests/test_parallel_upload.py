"""Contract tests for the parallel uploader (no network, no Telegram).

The uploader exists because one MTProto stream is throttled to ~160 KB/s while
the line does 1.34 MB/s, so these tests pin the parts that make several
connections safe: the worker clamp, the split (every byte exactly once, in
order) and the handle type Telegram expects for each size.
"""

import asyncio
import hashlib
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "90_Shared_Toolbox"))

from telegram import parallel_upload  # noqa: E402
from telethon import types  # noqa: E402


class FakeSender:
    """Records the parts it was asked to save, in call order."""

    def __init__(self, name):
        self.name = name
        self.parts = []
        self.disconnected = False

    async def disconnect(self):
        self.disconnected = True


class FakeClient:
    """Just enough client for the uploader: senders, _call, session, init."""

    def __init__(self, dc_id=2):
        self.sent = []                    # (sender, request) in completion order
        self.senders = []
        self.session = type("S", (), {"dc_id": dc_id, "auth_key": b"k"})()
        self._log = {}
        self._proxy = None
        self._local_addr = None
        self._init_request = type("I", (), {"query": None})()

    async def _get_dc(self, dc_id):
        return type("DC", (), {"ip_address": "1.2.3.4", "port": 443, "id": dc_id})()

    def _connection(self, *a, **kw):
        return object()

    async def _call(self, sender, request):
        sender.parts.append(request.file_part)
        self.sent.append((sender, request))
        return True


def _patch_senders(monkeypatch, client, count):
    created = []

    async def fake_new_sender(_client):
        sender = FakeSender(f"w{len(created)}")
        created.append(sender)
        client.senders = created
        return sender

    monkeypatch.setattr(parallel_upload, "_new_sender", fake_new_sender)
    return created


def test_worker_count_is_clamped_to_the_safe_band():
    assert parallel_upload.worker_count(11_630_000) == 5
    assert parallel_upload.worker_count(11_630_000, 4) == 4
    assert parallel_upload.worker_count(1_000, 99) == parallel_upload.MAX_WORKERS
    assert parallel_upload.worker_count(1_000, 0) == parallel_upload.MIN_WORKERS
    assert parallel_upload.worker_count(1_000, None) == parallel_upload.MIN_WORKERS


def test_parts_cover_every_byte_exactly_once(tmp_path, monkeypatch):
    payload = bytes(range(256)) * 3000          # 768 KB -> 2 parts at 512 KB
    path = tmp_path / "small.pdf"
    path.write_bytes(payload)
    client = FakeClient()
    _patch_senders(monkeypatch, client, 4)

    handle = asyncio.run(parallel_upload.upload_parallel(
        client, path, workers=4, part_size_kb=512))

    parts = sorted(r.file_part for _s, r in client.sent)
    assert parts == list(range(handle.parts))
    assert handle.parts == 2
    assert isinstance(handle, types.InputFile)
    # the small-file constructor must carry the real MD5, or Telegram rejects it
    assert handle.md5_checksum == hashlib.md5(payload).digest()
    assert all(s.disconnected for s in client.senders)


def test_each_connection_moves_its_own_parts(tmp_path, monkeypatch):
    path = tmp_path / "spread.pdf"
    path.write_bytes(b"x" * (4 * 512 * 1024))    # 4 parts
    client = FakeClient()
    _patch_senders(monkeypatch, client, 2)

    asyncio.run(parallel_upload.upload_parallel(
        client, path, workers=2, part_size_kb=512))

    per_sender = {s.name: sorted(s.parts) for s in client.senders}
    assert per_sender == {"w0": [0, 2], "w1": [1, 3]}


def test_large_files_use_the_big_part_request(tmp_path, monkeypatch):
    path = tmp_path / "big.pdf"
    path.write_bytes(b"y" * (10 * 1024 * 1024 + 1))
    client = FakeClient()
    _patch_senders(monkeypatch, client, 8)

    handle = asyncio.run(parallel_upload.upload_parallel(
        client, path, workers=8, part_size_kb=512))

    assert isinstance(handle, types.InputFileBig)
    assert all(type(r).__name__ == "SaveBigFilePartRequest" for _s, r in client.sent)
    assert len(client.sent) == handle.parts


def test_it_falls_back_to_whatever_senders_it_could_open(tmp_path, monkeypatch):
    """A refused extra connection must not kill the upload."""
    path = tmp_path / "ok.pdf"
    path.write_bytes(b"z" * (2 * 512 * 1024))
    client = FakeClient()
    opened = []

    async def flaky(_client):
        if len(opened) >= 1:
            raise RuntimeError("too many connections")
        sender = FakeSender("only")
        opened.append(sender)
        client.senders = opened
        return sender

    monkeypatch.setattr(parallel_upload, "_new_sender", flaky)

    handle = asyncio.run(parallel_upload.upload_parallel(
        client, path, workers=4, part_size_kb=512))

    assert handle.parts == 2
    assert len(client.sent) == 2


def test_no_sender_at_all_is_an_error(tmp_path, monkeypatch):
    path = tmp_path / "no.pdf"
    path.write_bytes(b"q" * 1024)
    client = FakeClient()

    async def refuse(_client):
        raise RuntimeError("no connections available")

    monkeypatch.setattr(parallel_upload, "_new_sender", refuse)

    with pytest.raises(RuntimeError):
        asyncio.run(parallel_upload.upload_parallel(client, path, workers=4))
