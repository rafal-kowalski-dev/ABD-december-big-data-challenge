"""Logging configuration module for the application."""

import logging
from logging import Logger

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="log.txt",
    filemode="a",
)

logger: Logger = logging.getLogger(__name__)
