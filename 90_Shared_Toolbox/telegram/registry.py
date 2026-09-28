"""Topic registry — ``subject → (chat_id, message_thread_id)`` (issues #8/#10).

Why a registry: the Bot API has **no method to list forum topics**, and this
gateway is outbound-only (no message stream to learn ids from). Thread ids
therefore come from exactly two sources:

  * ``createForumTopic`` responses (topics the bot owns), and
  * one-shot link bootstrapping at gates G2/G5 (topic root message id == topic id).

Until a subject is *bound*, :meth:`Registry.resolve` raises
:class:`~telegram.errors.UnboundTopic` — the gateway refuses to guess.

The seed list mirrors the ``TOPICS`` constants of the legacy Playwright script
``90_Shared_Toolbox/tools/telegram_publisher.py`` so nothing is lost when that
script is retired (issue #20).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .errors import RegistryMiss, UnboundTopic

__all__ = ["Registry", "SEED_SUBJECTS", "DEFAULT_REGISTRY_PATH"]

DEFAULT_REGISTRY_PATH = Path(__file__).with_name("registry.json")

# (subject, human description) — source: telegram_publisher.py TOPICS
SEED_SUBJECTS: list[tuple[str, str]] = [
    ("00-Start-Here", "Rules + index. Read-only."),
    ("01-Cyber-Security", "CS501 materials."),
    ("02-English-Language", "CS502 materials."),
    ("03-Data-Mining", "CS602 materials."),
    ("04-Advanced-Software-Eng", "CS504 materials."),
    ("05-Soft-Computing", "CS603 materials."),
    ("06-Artificial-Intelligence", "CS605 materials."),
    ("90-Toolbox", "Tools, exporters, dashboard."),
    ("99-Chat", "Discussion only. Open chat."),
    ("70-Exams-and-MCQ", "Quiz links, exam booklets, results."),
    ("71-Progress-Analytics", "Weekly reports, mastery, review queue."),
]


class Registry:
    """Small JSON-backed map of subjects to Telegram topic coordinates."""

    def __init__(self, path: Path | str | None = None, seed: bool = True):
        self.path = Path(path) if path else DEFAULT_REGISTRY_PATH
        self._data: dict[str, Any] = {"subjects": {}}
        if self.path.exists():
            self._load()
        if seed:
            self.seed()

    # -- persistence -----------------------------------------------------
    def _load(self) -> None:
        raw = json.loads(self.path.read_text(encoding="utf-8"))
        if not isinstance(raw, dict) or "subjects" not in raw:
            raise RegistryMiss(f"corrupt registry file: {self.path}")
        self._data = raw

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp.write_text(
            json.dumps(self._data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        tmp.replace(self.path)

    # -- content ---------------------------------------------------------
    def seed(self) -> None:
        """Create unbound entries for the canonical subject list (idempotent)."""
        changed = False
        for subject, description in SEED_SUBJECTS:
            if subject not in self._data["subjects"]:
                self._data["subjects"][subject] = {
                    "description": description,
                    "chat_id": None,
                    "thread_id": None,
                    "topic_name": None,
                }
                changed = True
        if changed and self.path.parent.exists():
            self.save()

    def subjects(self) -> list[str]:
        return sorted(self._data["subjects"])

    def get(self, subject: str) -> dict[str, Any]:
        try:
            return self._data["subjects"][subject]
        except KeyError:
            known = ", ".join(self.subjects()) or "<none>"
            raise RegistryMiss(
                f"unknown subject {subject!r} (known: {known})"
            ) from None

    def bind(
        self,
        subject: str,
        chat_id: int,
        thread_id: int,
        topic_name: str | None = None,
    ) -> dict[str, Any]:
        """Bind (or rebind) a subject to a concrete topic."""
        entry = self.get(subject)  # raises RegistryMiss for unknown subjects
        for other, row in self._data["subjects"].items():
            if other != subject and row.get("chat_id") == chat_id and row.get("thread_id") == thread_id:
                raise RegistryMiss(
                    f"thread {thread_id}@{chat_id} is already bound to {other!r}"
                )
        entry.update(
            {"chat_id": int(chat_id), "thread_id": int(thread_id), "topic_name": topic_name or entry.get("topic_name")}
        )
        self.save()
        return dict(entry)

    def unbind(self, subject: str) -> dict[str, Any]:
        entry = self.get(subject)
        entry.update({"chat_id": None, "thread_id": None})
        self.save()
        return dict(entry)

    def resolve(self, subject: str) -> dict[str, Any]:
        """Return bound coordinates or raise (never guess a destination)."""
        entry = self.get(subject)
        if entry.get("chat_id") is None or entry.get("thread_id") is None:
            raise UnboundTopic(
                f"subject {subject!r} is not bound yet — bind it at gate G2/G5 "
                "(registry bind, or bootstrap from a topic message link)"
            )
        return dict(entry)
