import boto3

DYNAMO = boto3.client("dynamodb", endpoint_url="http://localhost:8000")
DYNAMO_RESOURCE = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")

table_name = 'ConfitecTest'
existing_tables = DYNAMO.list_tables()['TableNames']
if table_name not in existing_tables:
    table = DYNAMO.create_table(
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
