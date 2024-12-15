"""Module for fetching weather data from Open-Meteo API."""

import json
from datetime import date, timedelta
from typing import List, Tuple

import requests

from utils.logger import logger


def get_weather_data(
    coordinates: Tuple[float, float],
    past_days: int = None,
    forecast: int = None,
    cols: List[str] = None,
) -> dict | None:
    """Fetch weather data from Open-Meteo API and save it to a JSON file.

    Args:
        coordinates (Tuple[float, float]): A tuple containing latitude and longitude coordinates.
            First element is latitude, second element is longitude.
        past_days (int, optional): Number of past days to retrieve weather data for.
            If provided, uses historical weather data. Defaults to None.
        forecast (int, optional): Number of forecast days to retrieve.
            If provided, fetches weather forecast data. Defaults to None.
        cols (List[str], optional): List of weather parameters to retrieve.
            If None, uses a default comprehensive list of parameters.
            See https://open-meteo.com/en/docs for available parameters.

    Returns:
        None: The function saves the weather data to 'weather.json' and logs the result.

    Raises:
        Logs an error if the API request fails, including the status code and error reason.

    Note:
        The function retrieves weather data in hourly intervals. By default, it includes:
        - Temperature at various heights (2m, 80m, 120m, 180m)
        - Humidity and precipitation metrics
        - Wind conditions at different heights
        - Cloud cover and visibility
        - Soil temperature and moisture at various depths
        - Other atmospheric conditions (pressure, evapotranspiration)
    """
    lat, lon = coordinates

    name = "get_weather_data"

    url = (
        "https://archive-api.open-meteo.com/v1/era5"
        if past_days
        else "https://api.open-meteo.com/v1/forecast"
    )

    if not cols:
        cols = [
            "temperature_2m",
            "relative_humidity_2m",
            "dew_point_2m",
            "apparent_temperature",
            "precipitation_probability",
            "precipitation",
            "rain",
            "showers",
            "snowfall",
            "snow_depth",
            "weather_code",
            "pressure_msl",
            "surface_pressure",
            "cloud_cover",
            "cloud_cover_low",
            "cloud_cover_mid",
            "cloud_cover_high",
            "visibility",
            "evapotranspiration",
            "et0_fao_evapotranspiration",
            "vapour_pressure_deficit",
            "wind_speed_10m",
            "wind_speed_80m",
            "wind_speed_120m",
            "wind_speed_180m",
            "wind_direction_10m",
            "wind_direction_80m",
            "wind_direction_120m",
            "wind_direction_180m",
            "wind_gusts_10m",
            "temperature_80m",
            "temperature_120m",
            "temperature_180m",
            "soil_temperature_0cm",
            "soil_temperature_6cm",
            "soil_temperature_18cm",
            "soil_temperature_54cm",
            "soil_moisture_0_to_1cm",
            "soil_moisture_1_to_3cm",
            "soil_moisture_3_to_9cm",
            "soil_moisture_9_to_27cm",
            "soil_moisture_27_to_81cm",
        ]

    url += f"?latitude={lat}&longitude={lon}&hourly={','.join(cols)}"

    today = date.today()

    if past_days:
        url += f"&start_date={today - timedelta(days=past_days)}&end_date={today}"

    if forecast:
        url += f"&forecast_days={forecast}"

    response = requests.get(url, timeout=5)

    if response.status_code == 200:
        logger.info(f"{name} -> Fetch weather data (coordinates={coordinates})")
        return json.loads(response.text)
    else:
        logger.error(
            f"{name} -> {json.load(response.text)['reason']} (status_code={response.status_code})"
        )
