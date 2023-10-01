import aws_cdk as core
import aws_cdk.assertions as assertions

from iot_kinesis_lambda_cdk.iot_kinesis_lambda_cdk_stack import IotKinesisLambdaStack


# example tests. To run these tests, uncomment this file along with the example
# resource in iot_kinesis_lambda/iot_kinesis_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = IotKinesisLambdaStack(app, "iot-kinesis-lambda")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
