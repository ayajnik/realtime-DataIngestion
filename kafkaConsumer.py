try:
    #from kafka import KafkaConsumer
    from s3fs import s3FileSystem
    print("Library imported")
except:
    print("S3 library not found")