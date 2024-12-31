from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

test_message = {"id": 1, "name": "Test Product"}
producer.send('product-topic', test_message)
producer.flush()
print("Test message sent to Kafka!")
