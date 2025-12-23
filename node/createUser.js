import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { PutCommand } from "@aws-sdk/lib-dynamodb";
import { randomUUID } from "crypto";
import { SQSClient, SendMessageCommand } from "@aws-sdk/client-sqs";

const client = new DynamoDBClient({});
const sqs = new SQSClient({});

export const handler = async (event) => {
  const body = JSON.parse(event.body);

  const user = {
    id: randomUUID(),
    nombre: body.nombre,
    email: body.email
  };

  await client.send(
    new PutCommand({
      TableName: process.env.USERS_TABLE,
      Item: user
    })
  );

  await sqs.send(new SendMessageCommand({
    QueueUrl: process.env.CREATE_USER_QUEUE_URL,
    MessageBody: JSON.stringify(user)
  }));

  return {
    statusCode: 201,
    body: JSON.stringify(user)
  };
};
