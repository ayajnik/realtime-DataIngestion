try:
    from s3fs import S3FileSystem
    import kafkaConsumer
    print("Hadoop and S3 libraries imported")
except ImportError as e:
    print(e)