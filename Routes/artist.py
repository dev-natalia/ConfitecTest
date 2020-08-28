from Logic.genius_search import get_artist
from flask import request, Blueprint

search_artist_blueprint = Blueprint('search_artist', __name__)


@search_artist_blueprint.route("/artist", methods=['POST'])
def search_artist():
    artist_name = request.json.get('artist_name')
    return get_artist(artist_name)
