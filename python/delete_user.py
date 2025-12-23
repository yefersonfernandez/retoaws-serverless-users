import json
import boto3
import os
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['USERS_TABLE'])

def handler(event, context):
    try:
        user_id = event['pathParameters']['id']

        table.delete_item(
            Key={'id': user_id},
            ConditionExpression="attribute_exists(id)"
        )

        return {
            "statusCode": 204,
            "body": ""
        }

    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return {
                "statusCode": 404,
                "body": json.dumps({
                    "message": "Usuario no encontrado"
                })
            }

        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": "Error interno del servidor"
            })
        }
