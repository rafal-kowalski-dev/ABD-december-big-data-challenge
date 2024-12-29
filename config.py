"""Configuration settings for the weather data application."""

import json
import os
from pathlib import Path
from typing import List

from dotenv import load_dotenv

from pydantic import BaseModel

from utils.logger import logger

load_dotenv()

class WeatherAppConfig(BaseModel):
    """Configuration model for the weather data application.

    Attributes:
        forecast (int): The number of days for which to fetch the forecast.
        cities (List[str]): A list of cities for which to fetch the weather data.
    """

    forecast: int = 1
    cities: List[str] = []

    def _update(self, conf: dict):
        """Update the configuration settings from a given dictionary.

        Args:
            conf: A dictionary containing configuration settings.
        """
        self.forecast = conf["forecast"]
        self.cities = conf["cities"]
        self.db_host = os.environ.get("POSTGRES_HOST")
        self.db_user = os.environ.get("POSTGRES_USER")
        self.db_password = os.environ.get("POSTGRES_PASSWORD")
        self.db_database = os.environ.get("POSTGRES_DB")
    

    def import_settings_from_json(self, path: Path | str, encoding="utf8"):
        """Import configuration settings from a JSON file.

        Args:
            path: The path to the JSON file containing configuration settings.
            encoding: The encoding of the JSON file (default is 'utf8').
        """
        try:
            with open(path, encoding=encoding) as f:
                cfg = json.load(f)

            self._update(cfg)
            logger.info(f"{self.__class__.__name__} -> import settings (file={path})")
        except Exception as e:
            logger.error(f"{self.__class__.__name__} -> {e}")

    @staticmethod
    def check_nessesary_folders():
        """Check and create necessary folders for results and logs."""
        if not os.path.exists("results/"):
            os.mkdir("results/")
        if not os.path.exists("logs/"):
            os.mkdir("logs/")


weather_app_config = WeatherAppConfig()
weather_app_config.check_nessesary_folders()
weather_app_config.import_settings_from_json("config.json")
