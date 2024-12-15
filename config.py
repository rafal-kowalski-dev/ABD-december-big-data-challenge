"""Configuration settings for the weather data application."""

import json
import os
from pathlib import Path
from typing import List

from pydantic import BaseModel

from utils.logger import logger


class WeatherAppConfig(BaseModel):
    forecast: int = 1
    cities: List[str] = []

    def _update(self, conf: dict):
        self.forecast = conf["forecast"]
        self.cities = conf["cities"]

    def import_settings_from_json(self, path: Path | str, encoding="utf8"):
        try:
            with open(path, encoding=encoding) as f:
                cfg = json.load(f)

            self._update(cfg)
            logger.info(f"{self.__class__.__name__} -> import settings (file={path})")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} -> {e}")

    @staticmethod
    def check_nessesary_folders():
        if not os.path.exists("results/"):
            os.mkdir("results/")
        if not os.path.exists("logs/"):
            os.mkdir("logs/")


weather_app_config = WeatherAppConfig()
weather_app_config.check_nessesary_folders()
weather_app_config.import_settings_from_json("config.json")
