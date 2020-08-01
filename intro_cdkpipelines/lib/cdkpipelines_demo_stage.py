from aws_cdk.core import (
	CfnOutput,
	Construct,
	Stack,
	StackProps
)

from aws_cdk import (
	core
)

from intro_cdkpipelines.intro_cdkpipelines_stack import IntroCdkpipelinesStack


class CdkpipelinesDemoStage(core.Stack):

	def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
		super().__init__(scope, id, **kwargs)

		service = IntroCdkpipelinesStack(self, "WebService")

		self.output_url = service.output_url

# End
