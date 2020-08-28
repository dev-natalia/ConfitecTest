from typing import Dict
from uuid import uuid4

from Persistency import DYNAMO_RESOURCE, table_name

# The table info from dynamodb
TABLE = DYNAMO_RESOURCE.Table(table_name)


def insert_data(artist_name: str, cache: bool) -> Dict:
    """
    Insert the data on DynamoDB.

    :param artist_name: the name of the artist
    :param cache: a boolean variable with the user configuration for the cache use
    :returns: a dictionary with the ResponseMetadata from DynamoDB
    """
    uid = str(uuid4())
    response = TABLE.put_item(
       Item={
            'artistName': artist_name,
            'uid': uid,
            'cache': cache
        }
    )
    return response


def check_existence(artist_name: str) -> bool:
    """
    Check if there's already a transaction saved with the artist name on the DynamoDB

    :param artist_name: the name of the artist
    :returns: False if there isn't and True if it already exists
    """
    response = TABLE.get_item(
        Key={
            "artistName": artist_name
        }
    )
    return False if response is None else True


def update_data(artist_name: str, cache: bool) -> Dict:
    """
    Update the data on DynamoDB.

    :param artist_name: the name of the artist
    :param cache: a boolean variable with the user configuration for the cache use
    :returns: a dictionary with the ResponseMetadata from DynamoDB
    """
    response = TABLE.update_item(
        Key={
            "artistName": artist_name
        },
        UpdateExpression="set cache=:c",
        ExpressionAttributeValues={
            ":c": cache
        }
    )
    return response
