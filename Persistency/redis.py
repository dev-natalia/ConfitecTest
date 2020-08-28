import json
from typing import Dict, Optional

from Persistency import REDIS_DB

EXPIRATION_TIME = 60*60*24*7


def create_cache(artist_name: str, data: Dict) -> None:
    REDIS_DB.set(name=artist_name, value=json.dumps(data), ex=EXPIRATION_TIME)
    return


def retrieve_cache(artist_name: str) -> Optional[Dict]:
    cache = REDIS_DB.get(name=artist_name)

    if cache is not None:
        response = json.loads(cache)
        return response
    else:
        return cache


def clean_cache(artist_name: str) -> None:
    REDIS_DB.delete(artist_name)
    return
