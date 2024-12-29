"""Transform weather data from Parquet files into clean format.

Provides classes for transforming raw weather data into clean, analysis-ready format:
- MesurementType: Enum of available weather measurements
- Measurement: Class for loading and transforming Parquet data
"""

from enum import Enum
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import (arrays_zip, col, date_format, explode,
                                   to_timestamp)

from schemas.json_schema import main_schema


class MesurementType(str, Enum):
    """Available weather measurement types.

    Defines all weather metrics that can be extracted from the raw data.
    Used for consistent naming across the transformation pipeline.
    """

    TEMPERATURE = "temperature_2m"
    HUMIDITY = "relative_humidity_2m"
    PRESSURE = "pressure_msl"
    WIND_SPEED = "wind_speed_10m"
    SOIL_TEMPERATURE = "soil_temperature_0cm"
    SOIL_MOISTURE = "soil_moisture_0_to_1cm"
    CLOUD_COVER_LOW = "cloud_cover_low"
    CLOUD_COVER_MID = "cloud_cover_mid"
    CLOUD_COVER_HIGH = "cloud_cover_high"
    DEW_POINT = "dew_point_2m"
    APPARENT_TEMPERATURE = "apparent_temperature"
    PRECIPITATION_PROBABILITY = "precipitation_probability"
    PRECIPITATION = "precipitation"
    RAIN = "rain"
    SNOWFALL = "snowfall"
    SNOW_DEPTH = "snow_depth"
    CLOUD_COVER = "cloud_cover"
    VISIBILITY = "visibility"


class Measurement:
    """Handle loading and transformation of weather measurement data.

    Loads Parquet files using predefined schema and provides methods
    to transform data into clean, analysis-ready format.

    Args:
        parquet_path: Path to Parquet file(s) containing weather data.
                     Can be single file or directory (will load all .parquet files).
        spark_session: Optional existing SparkSession to use.
                      If None, creates new session.
    """

    def __init__(self, parquet_path: str | Path, spark_session: SparkSession = None):
        self.spark = (
            spark_session if spark_session else SparkSession.builder.getOrCreate()
        )
        if not parquet_path.endswith(".parquet"):
            if not parquet_path.endswith("/"):
                parquet_path = parquet_path + "/"
            parquet_path = parquet_path + "*.parquet"

        self.parquet = self.spark.read.schema(main_schema).parquet(parquet_path)

    def transform(self):
        """Transform raw weather data into clean format.

        Unpacks arrays of measurements into rows, with proper timestamp handling
        and consistent column naming based on MesurementType enum.

        Returns:
            DataFrame with columns:
            - date: YYYY-MM-DD
            - time: HH:mm
            - city: City name
            - One column for each MesurementType value
        """
        result = (
            self.parquet.withColumn(
                "tmp",
                arrays_zip(
                    self.parquet.hourly.time,
                    *[self.parquet.hourly[measure] for measure in MesurementType],
                ),
            )
            .withColumn("tmp", explode("tmp"))
            .select(
                to_timestamp(col("tmp.0"), "yyyy-MM-dd'T'HH:mm").alias("date"),
                to_timestamp(col("tmp.0"), "yyyy-MM-dd'T'HH:mm").alias("time"),
                self.parquet.city,
                *[
                    col(f"tmp.{i+1}").alias(measure._name_.lower())
                    for i, measure in enumerate(MesurementType)
                ],
            )
        )

        result = result.withColumn("date", date_format(result.date, "yyyy-MM-dd"))
        result = result.withColumn("time", date_format(result.time, "HH:mm"))

        return result

    def save(self, path: str | Path, mode: str = "overwrite"):
        """Save transformed data to Parquet format.

        Args:
            path: Output path for transformed Parquet files
            mode: Spark write mode (default: "overwrite")
        """
        transformed_parquet = self.transform()
        transformed_parquet.write.mode(mode).parquet(path)
