from s3fs import S3FileSystem
from kafka import KafkaConsumer
import datetime
from datetime import datetime
import boto3
import json


today = datetime.today()
today_date = today.strftime('%Y-%m-%d')

consumer = KafkaConsumer(
    'demo_test',
     bootstrap_servers=[':9092'], #add your IP here
     value_deserializer=lambda x: loads(x.decode('utf-8')))

### to print the values in Kafka consumer

# for c in consumer:
#     print(c.value)

## setup the connection
s3_client = boto3.client(service_name='s3', aws_access_key_id='',
                                      aws_secret_access_key='')

for count, i in enumerate(consumer):
    with s3_client.put_object("s3://kafka-stock-market-tutorial/stock_market_{}.json".format(count), 'w') as file:
        json.dump(i.value, file) 

## another method: use s3fs library

# for count, i in enumerate(consumer):
#     with s3.open("s3://kafka-stock-market-tutorial-youtube-darshil/stock_market_{}.json".format(count), 'w') as file:
#         json.dump(i.value, file)    

## create a sub-folder
##s3_client.put_object(Bucket='kafka-stock-market-ayush', Key='TEST')








