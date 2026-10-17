"""Parallel MTProto upload — several connections pushing parts at once.

Telethon uploads strictly sequentially, and its own FAQ says so: *"the library
does not download or upload files in parallel, which can also help with the
speed of downloading or uploading a single file"*. On this machine one stream
to Telegram measures ~160 KB/s (a 512 KB part takes ~3.2 s) while the line
itself does 1.34 MB/s against Cloudflare, so the server is throttling **per
connection**, not per account: borrowing N senders and interleaving the parts
is what multiplies throughput.

The technique is the well-trodden one from mautrix-telegram / FastTelethon:
open extra ``MTProtoSender`` connections that share the session's authorization
key, then push ``upload.SaveFilePart`` (or ``SaveBigFilePart`` for >10 MB) over
them with one part in flight per connection. Community reports put the safe
band at 4–8 workers; past 20 Telegram stops answering and flood waits appear,
so the count is clamped hard.
"""

from __future__ import annotations

import asyncio
import dataclasses
import hashlib
import math
import os
from pathlib import Path
from typing import Callable

from telethon import functions, types
from telethon.errors import FloodWaitError
from telethon.network import MTProtoSender
from telethon.tl.alltlobjects import LAYER

#: Telegram switches from SaveFilePart to SaveBigFilePart past 10 MB.
BIG_FILE_BYTES = 10 * 1024 * 1024

#: 512 KB is the documented maximum part size and the least chatty choice.
PART_SIZE_KB = 512

#: Community-tested safe band. Above this Telegram answers with flood waits.
MIN_WORKERS = 1
MAX_WORKERS = 8

#: Roughly one stream per 2.5 MB, inside the safe band.
BYTES_PER_WORKER = 2_500_000

#: A flood wait longer than this is not worth sitting on inside a publish.
FLOOD_WAIT_CAP = 30.0


def worker_count(file_size: int, workers: int | None = None) -> int:
    """How many connections to open: the caller's wish, clamped to the safe band."""
    if workers is None:
        workers = math.ceil(file_size / BYTES_PER_WORKER)
    try:
        wanted = int(workers)
    except (TypeError, ValueError):
        wanted = MIN_WORKERS
    return max(MIN_WORKERS, min(MAX_WORKERS, wanted))


def _part_count(file_size: int, part_size: int) -> int:
    return max(1, math.ceil(file_size / part_size))


def _file_id() -> int:
    """A random 63-bit id, the same shape Telethon generates for a new upload."""
    return int.from_bytes(os.urandom(8), "big") >> 1


def _md5_of(path: Path) -> bytes:
    """Whole-file MD5, required by the small-file constructor only."""
    digest = hashlib.md5()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.digest()


async def _new_sender(client) -> MTProtoSender:
    """A second connection to the session's own DC, sharing its auth key.

    No authorization export/import is needed because we stay on the DC the
    session is already authorised on; only a fresh connection has to announce
    itself with ``initConnection`` (Telethon's template carries ``query=None``,
    so a cheap ``help.getConfig`` is swapped in).
    """
    dc = await client._get_dc(client.session.dc_id)
    sender = MTProtoSender(client.session.auth_key, loggers=client._log)
    await sender.connect(client._connection(
        dc.ip_address, dc.port, dc.id,
        loggers=client._log, proxy=client._proxy, local_addr=client._local_addr,
    ))
    init = client._init_request
    if dataclasses.is_dataclass(init):
        init = dataclasses.replace(init, query=functions.help.GetConfigRequest())
    await sender.send(functions.InvokeWithLayerRequest(LAYER, init))
    return sender


async def _push_part(client, sender, request) -> None:
    """One part, retrying once through a short flood wait."""
    try:
        await client._call(sender, request)
    except FloodWaitError as exc:
        wait = min(float(getattr(exc, "seconds", 0) or 0), FLOOD_WAIT_CAP)
        if wait <= 0:
            raise
        await asyncio.sleep(wait)
        await client._call(sender, request)


async def upload_parallel(client, path, *, workers: int | None = None,
                          part_size_kb: int = PART_SIZE_KB,
                          progress: Callable[[int, int], None] | None = None):
    """Upload ``path`` over several connections and return the input handle.

    Returns the same shape Telethon's own ``upload_file`` does: ``InputFileBig``
    past 10 MB, otherwise ``InputFile`` with the file's MD5. The handle is what
    ``send_file`` accepts in place of a path, so nothing is uploaded twice.
    """
    path = Path(path)
    file_size = path.stat().st_size
    part_size = max(1, int(part_size_kb)) * 1024
    part_count = _part_count(file_size, part_size)
    is_big = file_size > BIG_FILE_BYTES
    file_id = _file_id()
    wanted = worker_count(file_size, workers)

    senders: list[MTProtoSender] = []
    try:
        for _ in range(wanted):
            try:
                senders.append(await _new_sender(client))
            except Exception:                                  # noqa: BLE001
                # A refused extra connection must not kill the upload: whatever
                # we did get still moves parts in parallel.
                break
        if not senders:
            raise RuntimeError("no parallel sender could be established")

        done = 0
        lock = asyncio.Lock()

        async def worker(sender: MTProtoSender, indices: list[int]) -> None:
            nonlocal done
            with open(path, "rb") as handle:
                for index in indices:
                    handle.seek(index * part_size)
                    data = handle.read(part_size)
                    if is_big:
                        request = functions.upload.SaveBigFilePartRequest(
                            file_id, index, part_count, data)
                    else:
                        request = functions.upload.SaveFilePartRequest(
                            file_id, index, data)
                    await _push_part(client, sender, request)
                    if progress is not None:
                        async with lock:
                            done += len(data)
                            progress(done, file_size)

        await asyncio.gather(*[
            worker(senders[i], list(range(i, part_count, len(senders))))
            for i in range(len(senders))
        ])
    finally:
        for sender in senders:
            try:
                await sender.disconnect()
            except Exception:                                  # noqa: BLE001
                pass

    if is_big:
        return types.InputFileBig(file_id, part_count, path.name)
    return types.InputFile(file_id, part_count, path.name, _md5_of(path))
