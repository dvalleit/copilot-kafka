from confluent_kafka import Producer

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092'
}

# Create Producer instance
producer = Producer(**conf)

# Produce a message
topic = 'test_topic'
message = 'Hello, diego!'

producer.produce(topic, message.encode('utf-8'), callback=delivery_report)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
producer.poll(1)

# Wait for any outstanding messages to be delivered and delivery reports
# to be received.
producer.flush()