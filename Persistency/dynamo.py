from uuid import uuid4

from Persistency import DYNAMO_RESOURCE, table_name

TABLE = DYNAMO_RESOURCE.Table(table_name)


def insert_data(artist_name: str, cache: bool):
    uid = str(uuid4())
    response = TABLE.put_item(
       Item={
            'artistName': artist_name,
            'uid': uid,
            'cache': cache
        }
    )
    return response


def check_existence(artist_name: str):
    response = TABLE.get_item(
        Key={
            "artistName": artist_name
        }
    )
    return False if response is None else True


def update_data(artist_name: str, cache: bool):
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
