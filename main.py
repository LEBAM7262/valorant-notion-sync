import os
import requests
from notion_client import Client

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]
RIOT_API_KEY = os.environ["RIOT_API_KEY"]

GAME_NAME = "lebam1325"
TAG_LINE = "ryan"

notion = Client(auth=NOTION_TOKEN)

HEADERS = {
    "X-Riot-Token": RIOT_API_KEY
}
def get_account():
    url = f"https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{GAME_NAME}/{TAG_LINE}"

    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()

    return r.json()
  def get_match_ids(puuid):

    url = f"https://ap.api.riotgames.com/val/match/v1/matchlists/by-puuid/{puuid}"

    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()

    return r.json()["history"]
    def get_match(match_id):

    url=f"https://ap.api.riotgames.com/val/match/v1/matches/{match_id}"

    r=requests.get(url,headers=HEADERS)
    r.raise_for_status()

    return r.json()
    def notion_has_match(match_id):

    response = notion.databases.query(
        **{
            "database_id": DATABASE_ID,
            "filter": {
                "property": "Match ID",
                "rich_text": {
                    "equals": match_id
                }
            }
        }
    )

    return len(response["results"]) > 0
