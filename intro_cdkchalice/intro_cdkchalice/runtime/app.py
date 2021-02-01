"""
Name: app.py
Created by: Masato Shima
Created on: 2021/01/31
Description: Sample Chalice application.
"""

import os

import boto3
from aws_lambda_powertools import Logger
from chalice import Chalice
from chalice.app import ConvertToMiddleware


logger = Logger()

app = Chalice(app_name="cdk_intro_cdkchalice")
app.register_middleware(ConvertToMiddleware(logger.inject_lambda_context))

dynamodb = boto3.resource("dynamodb")
dynamodb_table = dynamodb.Table(os.environ["APP_TABLE_NAME"])


@app.route("/users", methods=["POST"])
def create_user():
    request = app.current_request.json_body

    logger.info({"request": request})

    item = {
        "PK": f"User#{request['username']}",
        "SK": f"Profile#{request['username']}",
    }

    item.update(request)

    dynamodb_table.put_item(Item=item)

    return {}


@app.route("/users/{username}", methods=["GET"])
def get_user(username):
    key = {
        "PK": f"User#{username}",
        "SK": f"Profile#{username}",
    }

    item = dynamodb_table.get_item(Key=key)["Item"]

    logger.info({"fetched_item": item})

    del item["PK"]
    del item["SK"]

    return item

# End
