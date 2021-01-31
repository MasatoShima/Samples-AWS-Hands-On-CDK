"""
Name: cdk_system_management_stack.py
Created by: Masato Shima
Created on: 2020/07/17
Description: IAM 関連のリソースを管理する stack
"""

from aws_cdk import core

from aws_iam_mfa_restriction.aws_iam_resources import AwsIamResources


class AwsIamMfaRestrictionStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # AWS IAM resources
        AwsIamResources(
            self,
            "AwsIamResources"
        )

# End
