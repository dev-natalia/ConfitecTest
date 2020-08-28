from Persistency import DYNAMO_RESOURCE, table_name


def insert_data(artist_name: str, uid: str, cache: bool = True):
    table = DYNAMO_RESOURCE.Table(table_name)
    response = table.put_item(
       Item={
            'artistName': artist_name,
            'uid': uid,
            'cache': cache
        }
    )
    return response
