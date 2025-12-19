import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['USERS_TABLE'])

def handler(event, context):
    user_id = event['pathParameters']['id']

    table.delete_item(
        Key={'id': user_id}
    )

    return {
        "statusCode": 204,
        "body": ""
    }
