from Logic.genius_search import post
from flask import request, Blueprint

search_artist_blueprint = Blueprint('search_artist', __name__)


@search_artist_blueprint.route("/artist", methods=['POST'])
def search_artist():
    artist_name = request.json.get('artist_name').lower()
    return post(artist_name)
