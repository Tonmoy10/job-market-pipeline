from config import API_URL,API_ID,API_KEY
import requests,json,pathlib,time

creds = {
    "app_id":API_ID,
    "app_key":API_KEY
}
data=[]
for page in range(1,6):
    response = requests.get(API_URL+f"/jobs/gb/search/{page}",params=creds)
    response = response.json()
    data.extend(response["results"])
    time.sleep(1)

save_path = pathlib.Path(__file__).resolve().parent.parent / "data" / "raw_jobs.json"

with open(save_path,"w") as jobs:
    json.dump(data,jobs,indent=4)


