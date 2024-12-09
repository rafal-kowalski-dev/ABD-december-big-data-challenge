"""Logging configuration module for the application."""

import logging
from datetime import date
from logging import Logger

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=f"logs/{date.today()}.log",
    filemode="a",
    encoding="utf8",
)

logger: Logger = logging.getLogger(__name__)
