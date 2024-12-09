"""Module for retrieving geographical coordinates from location names using OpenStreetMap API."""

import json
from typing import Tuple

import requests

from utils import logger


def get_coordinates(
    city: str = None, country: str = None, postal_code: str = None
) -> Tuple[float, float] | None:
    """Get geographical coordinates for a location using OpenStreetMap API.

    Args:
        city: Name of the city
        country: Name of the country
        postal_code: Postal code of the location

    Returns:
        Tuple of (latitude, longitude) or None if location not found
    """
    name = "utils.get_coordinates"

    url = "https://nominatim.openstreetmap.org/search?addressdetails=1&format=json"

    if city:
        url += f"&city={city}"
    if country:
        url += f"&country={country}"
    if postal_code:
        url += f"&postalcode={postal_code}"

    url += "&limit=1"

    response = requests.get(url, headers={"User-Agent": "Other"}, timeout=5)

    if response.status_code == 200:
        try:
            city_data = json.loads(response.text)[0]
            logger.info(
                f"{name} -> fetch data (city={city}, country={country}, postal_code={postal_code})"
            )
        except IndexError:
            logger.warning(f"{name} -> wrong input")
            return None
    else:
        logger.error(
            f"{name} -> {response.reason} (status_code={response.status_code})"
        )
        return None

    return (float(city_data["lat"]), float(city_data["lon"]))
