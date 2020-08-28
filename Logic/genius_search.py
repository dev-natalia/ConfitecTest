from typing import Dict

import requests
import json
from urllib.parse import quote

BASE = "https://api.genius.com/{}"
SEARCH_BY_NAME = "search?q={}"
SEARCH_BY_ID_AND_POPULARITY = "artists/{}/songs?per_page=10&sort=popularity"
CLIENT_ACCESS_TOKEN = "j0RTLKZAgEi7lbB2Ol6VFQtedYnV1-1J4LGWnCAVHqzKuYcwWWr9p0eccFPPVZl6"


def get_artist(artist_name):
    query_url = BASE.format(SEARCH_BY_NAME).format(quote(artist_name.lower()))
    headers = {"Authorization": f"Bearer {CLIENT_ACCESS_TOKEN}"}
    response = requests.get(url=query_url, headers=headers).content.decode("utf8")
    data = json.loads(response)
    artist_id = data.get("response").get("hits")[0].get("result").get("primary_artist").get("id")
    query_url = BASE.format(SEARCH_BY_ID_AND_POPULARITY).format(artist_id)
    response = requests.get(url=query_url, headers=headers).content.decode("utf8")
    data = json.loads(response)
    musics = data.get("response").get("songs")

    #print data
    #check if it exists on dynamo
    #if not, save it on dynamo with the respective cache bool
    #check if cache is false
    #if not, will save it on redis
    return response_dict(artist_music_data=musics)


def response_dict(artist_music_data: Dict) -> Dict:
    music_rank = 0
    artist_music_top_hits: Dict = {}
    for music in artist_music_data:
        music_rank += 1
        artist_music_top_hits[music_rank] = {'music_name': music.get('title'),
                                             'music_lyrics_url': music.get('url')}
    return artist_music_top_hits
