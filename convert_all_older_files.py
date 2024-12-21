from transform_data import convert_json_to_parquet
from os import listdir
dir_to_check = "results"

filelist = [f for f in listdir(dir_to_check) if f.endswith(".json")]

parq_list = listdir(f"{dir_to_check}/parquets")

for filename in filelist:
    if filename.split(".json")[0] + ".parquet" not in parq_list:
        convert_json_to_parquet(f"{dir_to_check}/{filename}")