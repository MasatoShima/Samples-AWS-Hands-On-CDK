from aws_cdk.core import (
    CfnOutput,
    Construct,
    Stack,
    StackProps
)

from aws_cdk import (
    aws_apigateway as apigw,
    aws_lambda as lambda_function,
    core
)


class IntroCdkpipelinesStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        functions_hello = lambda_function.Function(
            self,
            "IntroCdkpipelinesStack_HelloHandler",
            function_name="IntroCdkpipelinesStack_HelloHandler",
            runtime=lambda_function.Runtime.PYTHON_3_7,
            code=lambda_function.Code.asset("lambda"),
            handler="hello.handler"
        )

        api_gw_hello = apigw.LambdaRestApi(
            self,
            "IntroCdkpipelinesStack_HelloApi",
            rest_api_name="IntroCdkpipelinesStack_HelloApi",
            description="Endpoint for a simple Lambda-powered web service",
            handler=functions_hello
        )

        self.output_url = CfnOutput(
            self,
            "IntroCdkpipelinesStack_HelloApi__url",
            value=api_gw_hello.url
        )

# End
