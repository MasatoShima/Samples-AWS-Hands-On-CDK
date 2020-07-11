from aws_cdk import (
    aws_lambda as lambda_function,
    aws_apigateway as apigw,
    core
)

from cdk_dynamo_table_viewer import TableViewer

from intro_workshop.hitcounter import HitCounter


class IntroWorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        function_hello = lambda_function.Function(
            self,
            "HelloHandler",
            function_name="Samples_CDK_HelloHandler",
            runtime=lambda_function.Runtime.PYTHON_3_7,
            code=lambda_function.Code.asset("lambda"),
            handler="hello.handler"
        )

        function_hello_with_counter = HitCounter(
            self,
            "HelloHitCounter",
            downstream=function_hello
        )

        apigw.LambdaRestApi(
            self,
            "Endpoint",
            rest_api_name="Samples_CDK_HelloApi",
            handler=function_hello_with_counter.handler
        )

        TableViewer(
            self,
            "Samples_CDK_ViewHitCounter",
            title="Hello Hits",
            table=function_hello_with_counter.table
        )

# End
