from confluent_kafka import Producer
import json
from weather import *

def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

if __name__ == "__main__":
    # Producer configuration
    conf = {'bootstrap.servers': 'localhost:9092'}

    # Create Producer instance
    producer = Producer(conf)

    output = weather_scraping()

    for row in output:
        # Convert the row to a JSON string
        message = json.dumps(row)
        # Send the message to a Kafka topic, with a callback for delivery reports
        producer.produce('weather_data_topic', value=message, callback=delivery_report)

        # Trigger any available delivery report callbacks from previous produce() calls
        producer.poll(0)

    # Wait for any outstanding messages to be delivered and delivery report callbacks to be triggered
    producer.flush()