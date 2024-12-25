from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, arrays_zip, col, date_format
from enum import Enum
from pathlib import Path

class MesurementType(str, Enum):
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
    def __init__(self, parquet_path: str|Path, spark_session: SparkSession = None):
        self.spark = spark_session if spark_session else SparkSession.builder.getOrCreate()
        self.parquet = self.spark.read.parquet(parquet_path)

    def transform(self, measure: MesurementType = None):
        if not measure:
            measure = MesurementType.TEMPERATURE
        p = self.parquet

        result = (p
            .withColumn("tmp", arrays_zip(p.hourly.time, p.hourly[measure]))
            .withColumn("tmp", explode("tmp"))
            .select(
                p.measure_date.alias("date"),
                col("tmp.0").alias("time"),
                p.city,
                col("tmp.1").alias(measure._name_.lower())
            )        
        )

        result = result.withColumn("time", date_format(result.time, "HH:mm"))

        return result
    
    def save(self, path: str|Path, mode: str = "overwrite"):
        self.parquet.write.mode(mode).parquet(path)