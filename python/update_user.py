import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['USERS_TABLE'])

def handler(event, context):
    user_id = event['pathParameters']['id']
    body = json.loads(event['body'])

    table.update_item(
        Key={'id': user_id},
        UpdateExpression="SET nombre = :n, email = :e",
        ExpressionAttributeValues={
            ':n': body['nombre'],
            ':e': body['email']
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Usuario actualizado"})
    }
