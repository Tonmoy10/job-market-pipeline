from google.cloud import bigquery
import json,pathlib
from config import RAW_DATA_PATH

client = bigquery.Client()

table_destination = f"{client.project}.raw_job_market_data.raw_jobs"

configuration = bigquery.LoadJobConfig(autodetect=True)

with open(RAW_DATA_PATH,"r") as data:
    local_data = json.load(data)

client.load_table_from_json(local_data,table_destination,job_config=configuration).result()