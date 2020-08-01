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

from aws_cdk.pipelines import (
	CdkPipeline,
	SimpleSynthAction
)


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
				oauth_token=SecretValue.secrets_manager("github-token"),
				owner="OWNER",
				repo="REPO",
				trigger=aws_codepipeline_actions.GitHubTrigger.POLL
			),
			synth_action=SimpleSynthAction.standard_npm_synth(
				source_artifact=source_artifact,
				cloud_assembly_artifact=cloud_assembly_artifact,
				build_command="echo 'Hello !!'"
			)
		)

# End
