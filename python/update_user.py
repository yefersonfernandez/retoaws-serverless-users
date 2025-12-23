import json
import boto3
import os
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['USERS_TABLE'])

def handler(event, context):
    try:
        user_id = event['pathParameters']['id']

        body = json.loads(event['body'])
        nombre = body.get('nombre')
        email = body.get('email')

        if not nombre or not email:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Los campos 'nombre' y 'email' son obligatorios"
                })
            }

        table.update_item(
            Key={'id': user_id},
            UpdateExpression="SET nombre = :n, email = :e",
            ConditionExpression="attribute_exists(id)",
            ExpressionAttributeValues={
                ':n': nombre,
                ':e': email
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Usuario actualizado correctamente"
            })
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
