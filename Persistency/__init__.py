import boto3
import redis


REDIS_DB = redis.StrictRedis(host="localhost", port=6379, db=0)

DYNAMO_CLIENT = boto3.client("dynamodb", endpoint_url="http://localhost:8000")
DYNAMO_RESOURCE = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")

table_name = 'ConfitecTest'
existing_tables = DYNAMO_CLIENT.list_tables()['TableNames']
if table_name not in existing_tables:
    table = DYNAMO_CLIENT.create_table(
        TableName='ConfitecTest',
        KeySchema=[
            {
                'AttributeName': 'artistName',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'artistName',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
