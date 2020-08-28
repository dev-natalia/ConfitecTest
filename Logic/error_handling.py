def artist_not_found(artist_name: str) -> str:
    """
    Returns an message if the artist was not found.

    :param artist_name: the name of the artist
    """

    message = f"The artist {artist_name} was not found. Try again with a different name."
    return message


def missing_body_parameter() -> str:
    """
    Returns an message the user didn't add the mandatory body parameter.
    """

    message = f"Missing the body parameter < artist_name >."
    return message


def missing_artist_name() -> str:
    """
    Returns an message the user didn't add any artist name.
    """

    message = f"The artist name can't be empty."
    return message
