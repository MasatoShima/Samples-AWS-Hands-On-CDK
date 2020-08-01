from aws_cdk.core import (
	Construct,
	SecretValue,
	Stack,
	StackProps
)

from aws_cdk import (
	aws_codepipeline,
	aws_codepipeline_actions,
	core
)

from aws_cdk.pipelines import *

git_token = "0a14488dc49f3eb6618f78f11d436d0dbe534840"


class CdkpipelinesDemoPipelineStack(core.Stack):

	def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
		super().__init__(scope, id, **kwargs)

		source_artifact = aws_codepipeline.Artifact()
		cloud_assembly_artifact = aws_codepipeline.Artifact()

		CdkPipeline(
			self,
			"cdk_pipeline",
			pipeline_name="IntroCdkpipelinesStack_Pipeline",
			cloud_assembly_artifact=cloud_assembly_artifact,
			source_action=aws_codepipeline_actions.GitHubSourceAction(
				action_name="GitHub",
				output=source_artifact,
				oauth_token=SecretValue.plain_text(git_token),
				owner="MasatoShima",
				repo="Samples-AWS-Hands-On-CDK-IntroCdkpipelines",
				trigger=aws_codepipeline_actions.GitHubTrigger.POLL
			),
			synth_action=ShellScriptActionProps(
				action_name="TEST",
				commands=["echo 'Hello !!'"]
			)
		)

# End
