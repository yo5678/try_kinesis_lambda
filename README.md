
# kinesis-lambdaのチュートリアル

kinesis-lambdaの勉強のために、[参考URL](https://github.com/aws-samples/serverless-patterns/tree/main/iot-kinesis-lambda-cdk)通りに、環境構築を行なった。

以下はKinesisについて少し調べたメモである。

## kinesis Data Streams に関して

[Kinesis_blackbelt](https://pages.awscloud.com/rs/112-TZM-766/images/AWS-Black-Belt_2023_AmazonKinesisDataStreams_0430_v1.pdf)によると、以下のように記載されている。

従来処理はデータ生成→保管→分析の順で行うため、データ発生からデータを使えるまでに時間がかかっていた。データ生成→処理→格納という順で少量ずつ早く処理を行うこと（ストリーム処理）でタイムリーな分析が可能である。→AWSのサーバーレスなサービスでAmazon Kinesis Data Streamsがある。

## SQSとの違い

[Kinesisのよくある質問](https://aws.amazon.com/jp/kinesis/data-streams/faqs/?nc1=h_ls)、[SQSのよくある質問](https://aws.amazon.com/jp/sqs/faqs/)によると、

### Kinesis

リアルタイムデータの処理の際に使用する。

ユースケースとして、

- 複数アプリケーションが同じKinesisのデータを処理する時
- 保管期間を長く使いたい時（処理A実施8時間後に、Kinesisのデータを処理Bにかけたいなど）

などがあげられている。

### SQS

コンピューター間のデータの受け渡し、分散アプリケーション間のコンポーネントのデータ移動・コンポーネントの分離に使用する。

ユースケースとして

- キューを遅延させたい時
- メッセージレベルの確認/失敗などをSQS側で追跡して欲しい時

などがあげられている。

少し古い記事であるが、[細かい比較表がある記事](https://dev.classmethod.jp/articles/kinesis_vs_sqs/)も存在する。

