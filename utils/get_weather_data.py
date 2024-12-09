"""Module for fetching weather data from Open-Meteo API."""

import json
from datetime import date, timedelta

import requests

from utils import logger

# Wroclaw
# coordinates = (51.10536196888788, 17.01631922567193)

# Szczerbice
coordinates = (50.092402238216856, 18.459952564477)
lat = coordinates[0]
lon = coordinates[0]


past_days = None
forecast = 1

url = (
    f"https://archive-api.open-meteo.com/v1/era5"
    if past_days
    else f"https://api.open-meteo.com/v1/forecast"
)
url += f"?latitude={lat}&longitude={lon}"

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

today = date.today()

if past_days:
    url += f"&start_date={today - timedelta(days=past_days)}&end_date={today}"

if forecast:
    url += f"&forecast_days={forecast}"

if len(cols):
    url += f"&hourly={','.join(cols)}"


response = requests.get(url)

if response.status_code == 200:
    with open("weather.json", mode="w", encoding="utf8") as out_file:
        out_file.write(response.text)
else:
    logger.error(f"{response.status_code} -> {json.loads(response.text)['reason']}")
