"""Module for converting JSON files to Parquet format.

This module provides functionality to read a JSON file, add a measure date column based on the filename,
and write the data to a Parquet file using Apache Spark.
"""

from datetime import date
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit


def convert_json_to_parquet(path: Path | str, spark_session: SparkSession = None):
    """Convert a JSON file to Parquet format.

    This function reads a JSON file, adds a measure date column based on the filename,
    and writes the data to a Parquet file.

    Args:
        path: The path to the JSON file to be converted.
        spark_session: An optional SparkSession. If not provided, a new session will be created.

    Returns:
        None: The function saves the weather data to Parquet and logs the result.
    """
    if spark_session is None:
        spark_session = SparkSession.builder.getOrCreate()

    try:
        filename = path.name
    except AttributeError:
        filename = path.split("/")[-1].split(".json")[0]

    json_data = spark_session.read.option("multiline", "true").json(path)

    json_data.write.parquet(f"results/parquets/{filename}.parquet", mode="overwrite")
