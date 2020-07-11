import json
import pytest

from aws_cdk import core
from intro_workshop.intro_workshop_stack import IntroWorkshopStack


def get_template():
    app = core.App()
    IntroWorkshopStack(app, "intro-workshop")
    return json.dumps(app.synth().get_stack("intro-workshop").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
