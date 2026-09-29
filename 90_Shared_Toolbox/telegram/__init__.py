"""Master Studio Telegram gateway — offline core (roadmap gate G1).

Design doctrines (see 00_STUDIO_HUB/proposals/FEATURE_TELEGRAM_GATEWAY_ROADMAP.md):
  * Bot-first, outbound-only: no ``getUpdates`` loop anywhere.
  * Fail closed: permissions live in :mod:`telegram.acl`, secrets in ``.env``.
  * Gate G1 is deliberately network-free: the only transport is a mock, and
    requesting a live transport raises :class:`~telegram.errors.GatewayNotReady`
    until gate G2 lands.

Import surface used by the CLI, the agents (via ``tools/tg.py``) and tests::

    from telegram import parse_action, ACL, Registry, Store, execute, plan
"""

__version__ = "0.1.0+g1"

from .errors import (  # noqa: F401
    AccessDenied,
    ActionValidationError,
    ConfirmationRequired,
    GatewayError,
    GatewayNotReady,
    RateLimited,
    RegistryError,
    RegistryMiss,
    TransportError,
    UnboundTopic,
)
from .acl import ACL  # noqa: F401
from .registry import Registry  # noqa: F401
from .store import ChatRateLimiter, Store, backoff_delay  # noqa: F401
from .schema import Action, parse_action  # noqa: F401
from .transport import MockTransport, build_transport  # noqa: F401
from .executor import build_call, execute, plan  # noqa: F401
