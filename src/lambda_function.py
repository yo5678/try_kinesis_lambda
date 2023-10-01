import json
import base64


def handler(event, context):
    # print the event object received by Lambda
    print(json.dumps(event))

    """
    レコードの内容は以下のイメージ
    {
    "Records": [
        {
            "kinesis": {
                "kinesisSchemaVersion": "1.0",
                "partitionKey": "cc3a663f-03a7-4a13-be73-60bf6cd04482",
                "sequenceNumber": "49645056556898101433546895687125445869366349100388188162",
                "data": "ewogICJtZXNzYWdlIjogInRoaXMgaXMgdGVzdCBtZXNzYWdlIGZyb20gQVdTIElvVCBjb25zb2xlIgp9",
                "approximateArrivalTimestamp": 1696134668.293
            },
            "eventSource": "aws:kinesis",
            "eventVersion": "1.0",
            "eventID": "shardId-000000000000:49645056556898101433546895687125445869366349100388188162",
            "eventName": "aws:kinesis:record",
            "invokeIdentityArn": "arn:aws:iam::XXXX:role/IotKinesisLambdaCdkStack-IotKinesisLambdaCdkServic",
            "awsRegion": "XXXXX",
            "eventSourceARN": "arn:aws:kinesis:ap-northeast-1:XXXX:stream/IotKinesisLambdaCdkStack-IotKinesisLambdaCdkStream"
        }
        ]
    }

    """

    # MEMO Kinesisのレコードにはbase64で格納されているので、取り出しにはデコードが必要。ここもSQSとの違いかもしれない。
    data_base64 = event["Records"][0]["kinesis"]["data"]
    decoded_data = base64.b64decode(data_base64)
    print(decoded_data)

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
