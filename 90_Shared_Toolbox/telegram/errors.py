"""Exception hierarchy for the Telegram gateway.

Every exception carries a stable ``code`` used as the CLI exit status so
agents (and humans) can branch on failures without parsing text:

===== ==========================================================
 code  meaning
===== ==========================================================
  0    success
  1    unexpected internal error
  2    action validation failed (bad input — nothing executed)
  3    access denied (ACL, fail closed)
  4    destructive action missing ``--confirm``
  5    gateway not ready (live transport arrives at gate G2)
  6    topic registry miss / unbound subject
  7    transport-level failure (rate limit, API error)
===== ==========================================================
"""

from __future__ import annotations


class GatewayError(Exception):
    """Base class for all gateway failures."""

    code: int = 1


class ActionValidationError(GatewayError):
    """The requested action does not match the schema. Nothing ran."""

    code = 2


class AccessDenied(GatewayError):
    """Actor is not on the allowlist (or no allowlist is configured)."""

    code = 3


class ConfirmationRequired(GatewayError):
    """A destructive action was requested without ``--confirm``."""

    code = 4


class GatewayNotReady(GatewayError):
    """A capability that belongs to a later roadmap gate was requested."""

    code = 5


class RegistryError(GatewayError):
    """Topic registry problems."""

    code = 6


class RegistryMiss(RegistryError):
    """The requested subject does not exist in the registry."""


class UnboundTopic(RegistryError):
    """The subject exists but has no ``chat_id``/``thread_id`` yet (pre-G2)."""


class TransportError(GatewayError):
    """A Telegram API call failed."""

    code = 7


class RateLimited(TransportError):
    """Telegram answered 429; honour ``retry_after`` seconds."""

    def __init__(self, message: str, retry_after: float = 1.0):
        super().__init__(message)
        self.retry_after = float(retry_after)
