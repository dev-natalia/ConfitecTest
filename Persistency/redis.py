import json
from typing import Dict, Optional

from Persistency import REDIS_DB

# Redis uses seconds to control the expiration date. The variable below
# is set to 7 days in seconds
EXPIRATION_TIME = 60*60*24*7


def create_cache(artist_name: str, data: Dict) -> None:
    """
    Create the cache on Redis.

    :param artist_name: the name of the artist
    :param data: the artist data retrieved from Genius
    """
    REDIS_DB.set(name=artist_name, value=json.dumps(data), ex=EXPIRATION_TIME)
    return


def retrieve_cache(artist_name: str) -> Optional[Dict]:
    """
    Try to retrieve the cache data from Redis.

    :param artist_name: the name of the artist
    :returns: None if there isn't any data or a dictionary with the retrieved data from Redis.
    """
    cache = REDIS_DB.get(name=artist_name)

    if cache is not None:
        response = json.loads(cache)
        return response
    else:
        return cache


def clean_cache(artist_name: str) -> None:
    """
    Clean the cache data from Redis.

    :param artist_name: the name of the artist
    """
    REDIS_DB.delete(artist_name)
    return
