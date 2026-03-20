"""
Compatibility env loader.

Historically the project exposed a `config.env_loader` module. The current
implementation lives in `core.config`. This thin wrapper keeps the older
import path working while delegating to the new module.
"""

from __future__ import annotations

from core import config as core_config


def load_environment(env_name: str = "dev") -> None:
    """Proxy to `core.config.load_environment`."""
    core_config.load_environment(env_name)


def get(key: str, default: str = "") -> str:
    """Proxy to `core.config.get`."""
    return core_config.get(key, default)

