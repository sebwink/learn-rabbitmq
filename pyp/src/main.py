import os
import time
import signal
import pika

INTERVAL = int(os.getenv('PYP_INTERVAL', 5))
RABBITMQ_HOST = os.getenv('PYP_RABBITMQ_HOST', 'rabbitmq')
RABBITMQ_VHOST = os.getenv('PYP_RABBITMQ_VHOST')
RABBITMQ_USER = os.getenv('PYP_RABBITMQ_USER')
RABBITMQ_PASS = os.getenv('PYP_RABBITMQ_PASS')

if __name__ == '__main__':
    credentials = pika.PlainCredentials(
        RABBITMQ_USER,
        RABBITMQ_PASS,
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            credentials=credentials,
            virtual_host=RABBITMQ_VHOST,
        )
    )

    signal.signal(
        signal.SIGTERM,
        lambda s, f: connection.close(),
    )

    channel = connection.channel()
    channel.queue_declare(queue='hello')
    while True:
        time.sleep(INTERVAL)
        print(' [x] Sending message.')
        channel.basic_publish(
            exchange='',
            routing_key='hello',
            body='Hello World!',
        )
