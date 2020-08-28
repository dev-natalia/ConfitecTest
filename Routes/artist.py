from Logic.genius_search import post
from Logic.error_handling import missing_body_parameter
from flask import request, Blueprint

search_artist_blueprint = Blueprint("search_artist", __name__)


@search_artist_blueprint.route("/artist", methods=["POST"])
def search_artist():
    """
    Get the information on the body parameter and query string, calling
    the post method to realize the user request.

    :returns: a dictionary with the 10 most played songs of the artist
    :raises missing_body_parameter: if the user didn't add the artist_name body parameter
    """
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
