"""Main entry point for the weather data fetching application."""

import json
from datetime import date

import click

from config import weather_app_config
from get_data import get_coordinates, get_weather_data
from transform_data import Measurement, convert_json_to_parquet
from utils.logger import logger


@click.command()
@click.option(
    "-w", "--get-weather-data", is_flag=True, help="Get weather data", default=False
)
@click.option(
    "-p",
    "--convert-json-to-parquet",
    is_flag=True,
    help="Convert json to parquet",
    default=False,
)
@click.option(
    "-c", "--transform-data", is_flag=True, help="Transform data", default=False
)
@click.option("-o", "--output-path", type=str, help="Output path for clean data")
@click.option(
    "-i",
    "--input-path",
    type=str,
    help="Input path for clean data [defailt=results/parquets/]",
)
def main(**kwargs):
    """Main entry point for the weather data fetching application."""
    if kwargs["get_weather_data"]:
        get_weather_data_command()
    if kwargs["convert_json_to_parquet"]:
        convert_json_to_parquet_command()
    if kwargs["transform_data"]:
        transform_data_command(kwargs["output_path"], kwargs["input_path"])
    if not any(
        [
            kwargs["get_weather_data"],
            kwargs["convert_json_to_parquet"],
            kwargs["transform_data"],
        ]
    ):
        get_weather_data_command()
        convert_json_to_parquet_command()
        transform_data_command(kwargs["output_path"], kwargs["input_path"])


# TODO: refactor - add input_path and output_path
def get_weather_data_command():
    """Fetch and save weather data for configured cities.

    Uses weather_app_config to get list of cities and forecast settings.
    For each city:
    1. Gets coordinates using get_coordinates()
    2. Fetches weather data using get_weather_data()
    3. Adds city name to the response

    Saves combined results as JSON in results/YYYY-MM-DD.json
    """
    path = f"results/{date.today()}.json"
    results = []

    for city in weather_app_config.cities:
        coords = get_coordinates(city)
        res = get_weather_data(coordinates=coords, forecast=weather_app_config.forecast)
        res.update({"city": city})
        results.append(res)

    with open(path, mode="w", encoding="utf8") as f:
        json.dump(results, f)
        logger.info("main -> write data to file")


# TODO: refactor - add input_path and output_path
def convert_json_to_parquet_command():
    """Convert daily JSON weather data to Parquet format.

    Takes JSON file from results/YYYY-MM-DD.json and converts it to
    Parquet format using convert_json_to_parquet() function.
    Parquet files are saved in results/parquets/ directory.
    """
    path = f"results/{date.today()}.json"
    convert_json_to_parquet(path)
    logger.info("main -> convert json to parquet")


def transform_data_command(output_path: str = None, input_path: str = None):
    """Transform Parquet weather data into clean format.

    Uses Measurement class to read and transform Parquet files.
    Transformed data is saved according to MeasurementType enum values.

    Args:
        output_path: Directory for saving transformed data.
                    Defaults to 'results/clean_parquets/'.
        input_path: Directory containing Parquet files to transform.
                   Defaults to 'results/parquets/'.
    """
    if not output_path:
        output_path = f"results/clean_parquets/"
    if not input_path:
        input_path = f"results/parquets/"
    meas = Measurement(input_path)
    meas.save(f"{output_path}")
    logger.info(f"main -> transform data")


if __name__ == "__main__":
    main()
