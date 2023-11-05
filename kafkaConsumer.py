try:
    from s3fs import S3FileSystem
    import kafkaConsumer
    import datetime
    from datetime import datetime
    import boto3
except ImportError as e:
    print(e)

today = datetime.today()
today_date = today.strftime('%Y-%m-%d')


## setup the connection
s3_client = boto3.client(service_name='s3', aws_access_key_id='',
                                      aws_secret_access_key='')

## create a sub-folder
s3_client.put_object(Bucket='kafka-stock-market-ayush', Key='TEST')








