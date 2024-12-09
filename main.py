"""Main entry point for the weather data fetching application."""

import json
from datetime import date

from config import weather_app_config
from get_data import get_coordinates, get_weather_data
from utils.logger import logger

if __name__ == "__main__":
    results = []
    for city in weather_app_config.cities:
        coords = get_coordinates(city)
        res = get_weather_data(coordinates=coords, forecast=weather_app_config.forecast)
        res.update({"city": city})
        results.append(res)

    with open(f"results/{date.today()}.json", mode="w", encoding="utf8") as f:
        json.dump(results, f)
        logger.info("main -> write data to file")
