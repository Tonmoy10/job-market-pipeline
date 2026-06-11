from config import API_URL,API_ID,API_KEY
import requests,json,pathlib

creds = {
    "app_id":API_ID,
    "app_key":API_KEY
}

response = requests.get(API_URL+"/jobs/gb/search/1",params=creds)

data = response.json()
save_path = pathlib.Path(__file__).resolve().parent.parent / "data" / "raw_jobs.json"

with open(save_path,"w") as jobs:
    json.dump(data,jobs,indent=4)


