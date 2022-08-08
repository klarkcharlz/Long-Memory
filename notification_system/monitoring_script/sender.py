from json import dumps
from time import sleep

import pika
from pika.exceptions import AMQPConnectionError

from settings import RABBIT_URL


def send(receiver_name, data):
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBIT_URL))
        except AMQPConnectionError:
            print("Нет соединения с Rabbit MQ")
            sleep(5)
        else:
            break

    channel = connection.channel()
    channel.queue_declare(queue=receiver_name, auto_delete=False)
    channel.confirm_delivery()
    channel.basic_publish(exchange='',
                          routing_key=receiver_name,
                          body=dumps(data, default=str),
                          # properties=pika.BasicProperties(
                          #     expiration='10000'),
                          )
    print(f"Sent data to {receiver_name}!")
    connection.close()
