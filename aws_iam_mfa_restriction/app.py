#!/usr/bin/env python3
"""
Name: app.py
Created by: Masato Shima
Created on: 2020/07/18
Description:
	app.py
"""

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

# End
