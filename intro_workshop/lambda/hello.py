import json


def handler(event, context):
	print(f"request: {json.dumps(event)}")
	print(f"context: {context}")

	return {
		"statusCode": 200,
		"headers": {
			"Content-Type": "text/plain"
		},
		"body": f"Hello, CDK! You have hit {event['path']}\n"
	}

# End
