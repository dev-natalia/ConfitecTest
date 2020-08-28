def artist_not_found(artist_name: str):
    message = f"The artist {artist_name} was not found. Try again with a different name."
    return message


def missing_body_parameter():
    message = f"Missing the body parameter < artist_name >."
    return message


def missing_artist_name():
    message = f"The artist name can't be empty."
    return message
