from pathlib import Path
from datetime import date

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit


def convert_json_to_parquet(path: Path | str, spark_session: SparkSession = None):
    if spark_session is None:
        spark_session = SparkSession.builder \
            .appName("YourAppName") \
            .config("spark.security.manager.enabled", "false") \
            .getOrCreate()
    
    try:
        filename = path.name
    except AttributeError:
        filename = path.split('/')[-1].split(".json")[0]
    y, m, d = [int(x) for x in filename.split("-")]

    json_data = spark_session.read.option("multiline", "true").json(path)
    json_data = json_data.withColumn("measure_date", lit(date(y, m, d)))

    json_data.write.parquet(f"results/parquets/{filename}.parquet", mode="overwrite")
    
    spark_session.read.parquet(f"results/parquets/{filename}.parquet")
