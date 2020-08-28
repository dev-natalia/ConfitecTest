# ConfitecTest

### Introduction

This API uses the Genius' API to get the 10 most played songs by an given artist. It was created for a job proposal test.

### Technologies
- Python 3.6
- Flask
- Redis
- Amazon DynamoDB

### Launch
To launch the API, you'll need have the technologies pointed on the last topic, incluing an AWS Account, that can be created for free. The API use's the Web Version from AWS DynamoDB, but is simple to use it with a Local Version, with just a few changes:
- Open the file __init__.py on Persistency directory
- On lines 7 and 8, replace the code for the one below:
```sh
		DYNAMO_CLIENT = boto3.client("dynamodb", endpoint_url="http://localhost:8000")
		DYNAMO_RESOURCE = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")
```

Links to help with the technologies used:
| Technology | Link |
| ------ | ------ |
| Python 3.6 |<https://docs.python-guide.org/starting/install3/linux/> |
| Flask | <https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/> |
| Redis | <https://redis.io/topics/quickstart> |
| Free AWS Account | <https://aws.amazon.com/pt/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc> |
| DynamoDB Web Version | <https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/SettingUp.DynamoWebService.html> |
| DynamoDB Local Version | <https://docs.aws.amazon.com/pt_br/amazondynamodb/latest/developerguide/DynamoDBLocal.html> |
| Insomnia Rest | <https://support.insomnia.rest/category/9-getting-started> |

### How To Use
After setting up your ambient with the requirements, use the Insomnia Rest app - or other API Rest request app - to make the requests.
- Choose a POST requirement and add the following address in the address box:
``` sh
http://127.0.0.1:5000/artist
```
- On the body, choose JSON and add the text below:
```sh
{
	"artist_name": "Pearl Jam"
}
```
- If you don't want to use the cache, go to Query tab and add a new Query string as below:
```sh
name: cache, value: False
```
- Make your request. It'll return the 10 most played musics from the artist you've chosen
