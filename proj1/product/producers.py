# from kafka import KafkaProducer
# import json

# producer = KafkaProducer(
#     bootstrap_servers='kafka:9092',
#     value_serializer=lambda v: json.dumps(v).encode('utf-8')
# )

# def send_product_data(product):
#     print('here')
#     data = {
#         "id": product.id,
#         "name": product.name,
#     }
#     print(data)
#     producer.send('product-topic', data)

from confluent_kafka import Producer
import json

# Kafka producer configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
}

# Initialize producer
producer = Producer(producer_config)

def delivery_report(err, msg):
    """
    Callback function for message delivery reports.
    """
    if err:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_product_data(product):
    """
    Sends product data to Kafka topic.

    Args:
        product: An object or dictionary containing product data.
    """
    # Prepare product data as a dictionary
    print(producer)
    data = {
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "quantity": product.quantity,
    }

    # Serialize the data to JSON
    message_value = json.dumps(data).encode('utf-8')
    
    print(f"Sending data to Kafka: {data}")  # Log the data

    # Send message to the Kafka topic
    producer.produce(
        topic='product-topic',
        value=message_value,
        callback=delivery_report
    )

    # Flush the producer to ensure the message is sent
    producer.flush()
