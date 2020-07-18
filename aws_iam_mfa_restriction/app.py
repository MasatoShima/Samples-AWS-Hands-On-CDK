#!/usr/bin/env python3

from aws_cdk import core

from aws_iam_mfa_restriction.aws_iam_mfa_restriction_stack import AwsIamMfaRestrictionStack


app = core.App()

AwsIamMfaRestrictionStack(
	app,
	"Samples-AWS-Hands-On-CDK-aws-iam-mfa-restriction",
	env={
		"region": "ap-northeast-1"
	}
)

app.synth()
