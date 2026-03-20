from __future__ import annotations

import logging
import os
from typing import Optional


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
DEFAULT_LOG_DIR = os.path.join("artifacts", "logs")


def _ensure_log_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """
    Return a configured logger instance.

    - Logs to stdout for quick debugging.
    - Also writes to `artifacts/logs/framework.log` by default.
    """
    logger_name = name or "mayson-playwright"
    logger = logging.getLogger(logger_name)

    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler
    _ensure_log_dir(DEFAULT_LOG_DIR)
    file_path = os.path.join(DEFAULT_LOG_DIR, "framework.log")
    file_handler = logging.FileHandler(file_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False
    return logger
