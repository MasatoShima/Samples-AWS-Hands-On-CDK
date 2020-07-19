"""
Name: aws_iam_resources.py
Created by: Masato Shima
Created on: 2020/07/18
Description:
	以下の IAM 関連のリソースを作成する
		- IAM Group, User, Role, Policy
	作成される IAM User には以下のような制限を設ける
		- マネジメントコンソールへのログインは MFA 認証必須
		- マネジメントコンソールへログイン後, 必要な操作は全て, switch role を行った後に行う
"""

import json
from typing import *

from aws_cdk import (
	aws_iam as iam,
	core
)


class AwsIamResources(core.Construct):
	def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
		super().__init__(scope, id)

		# IAM Group
		hands_on_cdk_developers = iam.Group(
			self,
			"HandsOnCdkDevelopers",
			group_name="HandsOnCdkDevelopers"
		)

		# IAM User
		iam.User(
			self,
			"HandsOnCdkDeveloper-Guest",
			user_name="HandsOnCdkDeveloper-Guest",
			password=core.SecretValue.plain_text("password"),
			groups=[hands_on_cdk_developers]
		)

		# IAM Role
		iam.Role(
			self,
			"HandsOnCdkDevelopers-Role-PowerUserAccess",
			role_name="HandsOnCdkDevelopers-Role-PowerUserAccess",
			assumed_by=iam.AccountPrincipal(core.ScopedAws(scope).account_id),
			managed_policies=[
				iam.ManagedPolicy.from_aws_managed_policy_name("PowerUserAccess")
			]
		)

		# IAM Policy
		iam.Policy(
			self,
			"HandsOnCdkDevelopers-Policy-SourceMfaRestriction",
			policy_name="HandsOnCdkDevelopers-Policy-SourceMfaRestriction",
			force=True,
			groups=[
				hands_on_cdk_developers
			],
			statements=[
				statement for statement in read_config_source_mfa_restriction()
			]
		)

		iam.Policy(
			self,
			"HandsOnCdkDevelopers-Policy-OnlySwitchRole",
			policy_name="HandsOnCdkDevelopers-Policy-OnlySwitchRole",
			force=True,
			groups=[
				hands_on_cdk_developers
			],
			statements=[
				statement for statement in read_config_only_switch_role()
			]
		)


def read_config_source_mfa_restriction() -> Generator[iam.PolicyStatement, None, None]:
	path = "./aws_iam_mfa_restriction/aws/iam_policy_SourceMfaRestriction.json"

	with open(path, "r", encoding="utf-8") as file:
		statements = json.load(file)["Statement"]

	for statement in statements:
		yield iam.PolicyStatement.from_json(statement)

	return


def read_config_only_switch_role() -> Generator[iam.PolicyStatement, None, None]:
	path = "./aws_iam_mfa_restriction/aws/iam_policy_OnlySwitchRole.json"

	with open(path, "r", encoding="utf-8") as file:
		statements = json.load(file)["Statement"]

	for statement in statements:
		yield iam.PolicyStatement.from_json(statement)

	return


# End
