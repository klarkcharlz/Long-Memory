from json import dumps

import pika

from settings import RABBIT_URL


def send(receiver_name, data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_URL))
    channel = connection.channel()
    channel.queue_declare(queue=receiver_name)
    channel.basic_publish(exchange='',
                          routing_key=receiver_name,
                          body=dumps(data))
    print(f"Sent data to {receiver_name}!")
    connection.close()
