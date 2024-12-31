from confluent_kafka import Consumer, KafkaError, KafkaException

print('bc')

consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # or 'host.docker.internal:9092' if inside Docker
    'group.id': 'proj2-consumer-group',
    'auto.offset.reset': 'earliest',  # Start from the earliest message if no offset is found
    'enable.auto.commit': False,  # Disable auto commit for manual offset management
}

consumer = Consumer(consumer_config)
consumer.subscribe(['product-topic'])

def consume_messages():
    try:
        print("Consumer started.")
        while True:
            msg = consumer.poll(1.0)  # Wait for a message (timeout after 1 second)
            if msg is None:
                print("No message received. Continuing to poll...")
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"End of partition reached {msg.partition}, offset: {msg.offset()}")
                    continue
                else:
                    print(f"Error: {msg.error()}")
                    raise KafkaException(msg.error())
            else:
                data = msg.value().decode('utf-8')
                print(f"Received message: {data}")

    except KeyboardInterrupt:
        print("Consumer interrupted.")
    except Exception as e:
        print(f"Error in consumer: {e}")
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages()
