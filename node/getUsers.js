import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { ScanCommand } from "@aws-sdk/lib-dynamodb";

const client = new DynamoDBClient({});

export const handler = async () => {
  const result = await client.send(
    new ScanCommand({
      TableName: process.env.USERS_TABLE
    })
  );

  return {
    statusCode: 200,
    body: JSON.stringify(result.Items ?? [])
  };
};
