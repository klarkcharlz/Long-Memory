from json import dumps

import pika

from settings import RABBIT_URL


def send(receiver_name, data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_URL))
    channel = connection.channel()
    channel.queue_declare(queue=receiver_name, auto_delete=False)
    channel.confirm_delivery()
    channel.basic_publish(exchange='',
                          routing_key=receiver_name,
                          body=dumps(data),
                          # properties=pika.BasicProperties(
                          #     expiration='10000'),
                          )
    print(f"Sent data to {receiver_name}!")
    connection.close()
