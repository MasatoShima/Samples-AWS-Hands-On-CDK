import os
import json

import boto3

dynamodb = boto3.resource("dynamodb")
lambda_function = boto3.client("lambda")

table = dynamodb.Table(os.environ["HITS_TABLE_NAME"])


def handler(event, context):
    print(f"request: {json.dumps(event)}")
    print(f"context: {context}")

    # Update DynamoDB item
    table.update_item(
        Key={
            "path": event["path"]
        },
        UpdateExpression="ADD hits :incr",
        ExpressionAttributeValues={":incr": 1}
    )

    # Execute Lambda Function
    response = lambda_function.invoke(
        FunctionName=os.environ["DOWNSTREAM_FUNCTION_NAME"],
        Payload=json.dumps(event),
    )

    body = response["Payload"].read()

    print(f"downstream response: {body}")

    return json.loads(body)

# End
