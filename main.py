import os
import requests
from notion_client import Client

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]
RIOT_API_KEY = os.environ["RIOT_API_KEY"]

GAME_NAME = "lebam1325"
TAG_LINE = "ryan"

notion = Client(auth=NOTION_TOKEN)

headers = {
    "X-Riot-Token": RIOT_API_KEY
}

print("GameHub Sync Started")
