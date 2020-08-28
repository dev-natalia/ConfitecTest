from Logic.genius_search import post
from Logic.error_handling import missing_body_parameter
from flask import request, Blueprint

search_artist_blueprint = Blueprint("search_artist", __name__)


@search_artist_blueprint.route("/artist", methods=["POST"])
def search_artist():
    artist_name = request.json.get("artist_name")
    if artist_name is not None:
        artist_name = artist_name.lower()
    else:
        return missing_body_parameter()

    cache = request.args.get("cache")
    if cache != "False" and cache != "false":
        cache = True
    else:
        cache = False
    return post(artist_name, cache)
