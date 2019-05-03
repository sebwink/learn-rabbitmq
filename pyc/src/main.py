import os
import pika

RABBITMQ_HOST = os.getenv('PYC_RABBITMQ_HOST', 'rabbitmq')
RABBITMQ_VHOST = os.getenv('PYC_RABBITMQ_VHOST')
RABBITMQ_USER = os.getenv('PYC_RABBITMQ_USER')
RABBITMQ_PASS = os.getenv('PYC_RABBITMQ_PASS')

def callback(ch, method, properties, body):
    print(' [x] Received %r' % body)

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
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_consume(
        callback,
        queue='hello',
        no_ack=True,
    )
    print(' [*] Waiting for messages.')
    channel.start_consuming()
