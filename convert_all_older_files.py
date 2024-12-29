""" Module responsible for converting older JSON files to Parquet format. """

from os import listdir

from transform_data import convert_json_to_parquet

DIR_TO_CHECK = "results"

filelist = [f for f in listdir(DIR_TO_CHECK) if f.endswith(".json")]

parq_list = listdir(f"{DIR_TO_CHECK}/parquets")

for filename in filelist:
    if filename.split(".json")[0] + ".parquet" not in parq_list:
        convert_json_to_parquet(f"{DIR_TO_CHECK}/{filename}")
