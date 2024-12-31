from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_product_data(product):
    data = {
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "quantity": product.quantity,
    }
    print(f"Sending data to Kafka: {data}")  # Log the data
    producer.send('product-topic', data)
    producer.flush()  # Ensure the message is sent
