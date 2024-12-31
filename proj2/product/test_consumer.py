from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'product-topic',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

print("Consumer started. Listening for messages...")
for message in consumer:
    print(f"Received message: {message.value}")
