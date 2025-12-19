import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { PutCommand } from "@aws-sdk/lib-dynamodb";
import { randomUUID } from "crypto";

const client = new DynamoDBClient({});

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

  return {
    statusCode: 201,
    body: JSON.stringify(user)
  };
};
