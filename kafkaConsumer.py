try:
    from kafka import KafkaConsumer
    print("Library imported")
except:
    print("kafka library not found")