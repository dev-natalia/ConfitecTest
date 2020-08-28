import boto3
import redis

# Set the redis localhost client
REDIS_DB = redis.StrictRedis(host="localhost", port=6379, db=0)

# Set the dynamodb client and resource
DYNAMO_CLIENT = boto3.client("dynamodb")
DYNAMO_RESOURCE = boto3.resource("dynamodb")

# The table name that will be used on dynamo
table_name = 'ConfitecTest'

# Check if the table exist. If it don't, create the table on dynamo
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
