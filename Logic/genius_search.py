from typing import Dict, Union

import requests
import json
from urllib.parse import quote

from Persistency.dynamo import insert_data, check_existence, update_data
from Persistency.redis import create_cache, retrieve_cache, clean_cache
from Logic.error_handling import artist_not_found, missing_artist_name

# Variables with Genius configs
BASE = "https://api.genius.com/{}"
SEARCH_BY_NAME = "search?q={}"
SEARCH_BY_ID_AND_POPULARITY = "artists/{}/songs?per_page=10&sort=popularity"
CLIENT_ACCESS_TOKEN = "j0RTLKZAgEi7lbB2Ol6VFQtedYnV1-1J4LGWnCAVHqzKuYcwWWr9p0eccFPPVZl6"


def post(artist_name: str, cache: bool) -> Union[Dict, str]:
    """
    Centralize the code post method, calling functions if there's an error on
    the request or calling functions to realize the cache creation and
    database update or insertion.

    :param artist_name: the artist name
    :param cache: a boolean variable which is True if will have a cache or False if not
    :returns: a dictionary with the 10 most played songs of the artist
    :raises missing_artist_name: if the user didn't add any artist name
    """

    if len(artist_name) == 0:
        return missing_artist_name()

    existence_transaction = check_existence(artist_name=artist_name)
    if cache is False:
        response = get_artist(artist_name=artist_name)
        if existence_transaction is True:
            clean_cache(artist_name=artist_name)
            update_data(artist_name=artist_name, cache=cache)
        else:
            if isinstance(response, dict):
                insert_data(artist_name=artist_name, cache=cache)
    else:
        if existence_transaction is True:
            retrieved_cache = retrieve_cache(artist_name=artist_name)
            update_data(artist_name=artist_name, cache=cache)
            if retrieved_cache is not None:
                return {artist_name: retrieved_cache}

        response = get_artist(artist_name=artist_name)
        insert_data(artist_name=artist_name, cache=cache)
        create_cache(artist_name=artist_name, data=response)

    return {artist_name: response}


def get_artist(artist_name: str) -> Union[Dict, str]:
    """
    Make a request to the Genius API, getting firstly the artist's id and, then,
    the artist's 10 mostly played songs.

    :param artist_name: the artist name
    :returns: a dictionary with the 10 most played songs of the artist
    :raises artist_not_found: if there's no artist found
    """

    query_url = BASE.format(SEARCH_BY_NAME).format(quote(artist_name))
    headers = {"Authorization": f"Bearer {CLIENT_ACCESS_TOKEN}"}
    search_response = requests.get(url=query_url, headers=headers).content.decode("utf8")
    search_data = json.loads(search_response)

    if len(search_data.get("response").get("hits")) == 0:
        return artist_not_found(artist_name=artist_name)

    artist_id = search_data.get("response").get("hits")[0].get("result").get("primary_artist").get("id")
    query_url = BASE.format(SEARCH_BY_ID_AND_POPULARITY).format(artist_id)
    artist_response = requests.get(url=query_url, headers=headers).content.decode("utf8")
    artist_data = json.loads(artist_response)
    musics = artist_data.get("response").get("songs")
    return response_dict(artist_music_data=musics)


def response_dict(artist_music_data: Dict) -> Dict:
    """
    Create a dictionary organizing the data to be returned.

    :param artist_music_data: a dictionary with the data returned from the Genius API GET request
    :returns: a dictionary with the 10 most played songs of the artist and their respective urls
    """
    music_rank = 0
    artist_music_top_hits: Dict = {}
    for music in artist_music_data:
        music_rank += 1
        artist_music_top_hits[music_rank] = {'music_name': music.get('title'),
                                             'music_lyrics_url': music.get('url')}
    return artist_music_top_hits
