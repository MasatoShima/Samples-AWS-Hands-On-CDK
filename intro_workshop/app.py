#!/usr/bin/env python3

from aws_cdk import core

from intro_workshop.intro_workshop_stack import IntroWorkshopStack


app = core.App()

IntroWorkshopStack(
	app,
	"Samples-AWS-Hands-On-CDK-intro-workshop",
	env={
		"region": "ap-northeast-1"
	}
)

app.synth()
