from aws_cdk import (
    aws_lambda as lambda_function,
    aws_dynamodb as dynamodb,
    core
)


class HitCounter(core.Construct):

    @property
    def handler(self):
        return self._handler

    @property
    def table(self):
        return self._table

    def __init__(self, scope: core.Construct, id: str, downstream: lambda_function.IFunction) -> None:
        super().__init__(scope, id)

        self._table = dynamodb.Table(
            self,
            "Hits",
            table_name="Samples_CDK_HitCountTable",
            partition_key=dynamodb.Attribute(
                name="path",
                type=dynamodb.AttributeType.STRING
            )
        )

        self._handler = lambda_function.Function(
            self,
            "HitCountHandler",
            function_name="Samples_CDK_HitCounter",
            runtime=lambda_function.Runtime.PYTHON_3_7,
            code=lambda_function.Code.asset("lambda"),
            handler="hitcount.handler",
            environment={
                "DOWNSTREAM_FUNCTION_NAME": downstream.function_name,
                "HITS_TABLE_NAME": self._table.table_name
            }
        )

        self.table.grant_read_write_data(self.handler)

        downstream.grant_invoke(self.handler)

# End
