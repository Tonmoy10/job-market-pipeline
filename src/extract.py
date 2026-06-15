from config import API_URL,API_ID,API_KEY,RAW_DATA_PATH
import requests,json,pathlib,time

creds = {
    "app_id":API_ID,
    "app_key":API_KEY,
    "what":"software engineering"
}
data=[]
for page in range(1,6):
    response = requests.get(API_URL+f"/jobs/gb/search/{page}",params=creds)
    response = response.json()
    data.extend(response["results"])
    time.sleep(1)

with open(RAW_DATA_PATH,"w") as jobs:
    json.dump(data,jobs,indent=4)


