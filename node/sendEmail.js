import { SNSClient, PublishCommand } from "@aws-sdk/client-sns";

const sns = new SNSClient({});

export const handler = async (event) => {
  for (const record of event.Records) {
    const user = JSON.parse(record.body);

    await sns.send(new PublishCommand({
      TopicArn: process.env.SEND_EMAIL_TOPIC_ARN,
      Message: `Se ha creado un nuevo usuario: ${user.nombre} (${user.email})`
    }));
  }
};
