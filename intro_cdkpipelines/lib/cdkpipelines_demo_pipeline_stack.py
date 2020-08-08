from aws_cdk.core import (
	SecretValue,
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

from lib.cdkpipelines_demo_stage import CdkpipelinesDemoStage


class CdkpipelinesDemoPipelineStack(core.Stack):

	def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
		super().__init__(scope, id, **kwargs)

		source_artifact = aws_codepipeline.Artifact()
		cloud_assembly_artifact = aws_codepipeline.Artifact()

		pipeline = CdkPipeline(
			self,
			"cdk_pipeline",
			pipeline_name="IntroCdkpipelinesStack_Pipeline",
			cloud_assembly_artifact=cloud_assembly_artifact,
			source_action=aws_codepipeline_actions.GitHubSourceAction(
				action_name="GitHub",
				output=source_artifact,
				oauth_token=SecretValue.secrets_manager(
					secret_id="github-token",
					json_field="github-token"
				),
				owner="MasatoShima",
				repo="Samples-AWS-Hands-On-CDK",
				trigger=aws_codepipeline_actions.GitHubTrigger.POLL
			),
			synth_action=SimpleSynthAction.standard_yarn_synth(
				source_artifact=source_artifact,
				cloud_assembly_artifact=cloud_assembly_artifact,
				install_command="pip install -r requirements.txt",
				subdirectory="./intro_cdkpipelines/"
			)
		)

		pipeline.add_application_stage(
			CdkpipelinesDemoStage(self, "PreProd")
		)

# End
