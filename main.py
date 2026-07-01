import os
import requests

API_KEY = os.environ["HENRIK_API_KEY"]

REGION = "ap"
PLATFORM = "pc"
NAME = "lebam1325"
TAG = "ryan"

url = f"https://api.henrikdev.xyz/valorant/v4/matches/{REGION}/{PLATFORM}/{NAME}/{TAG}"

headers = {
    "Authorization": API_KEY
}

params = {
    "size": 1
}

response = requests.get(url, headers=headers, params=params)

print(response.status_code)
print(response.text)
