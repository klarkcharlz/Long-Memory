from json import loads
from datetime import datetime
from time import sleep
import random

import vk_api
import pika
from pika.exceptions import AMQPConnectionError
from dotenv import dotenv_values

config = dotenv_values(".env")

TOKEN = config['TOKEN']
SERVICE = 'vk'  # тут имя вашего сервиса email, telegram или vk


def write_msg(vk, id_, message):
    data = dict(user_id=id_,
                peer_id=id_,
                random_id=random.getrandbits(32),
                message=message)
    vk.messages.send(**data)


# Авторизуемся
vk = vk_api.VkApi(token=TOKEN)
vk = vk.get_api()


def main():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        except AMQPConnectionError:
            print("Нет соединения с Rabbit MQ")
            sleep(5)
        else:
            break
    channel = connection.channel()

    def callback(ch, method, properties, body):
        print(f'{datetime.now()} - Принял сообщение:')
        body = loads(body)
        print(type(body))
        print(body)
        # дальше ваша логика по рассылке
        write_msg(vk, 232551334, 'Hello')

    channel.queue_declare(queue=SERVICE)
    channel.basic_consume(queue=SERVICE, on_message_callback=callback, auto_ack=True)

    print(f'Start consumer {SERVICE}.\nWaiting for messages.')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception:
        channel.stop_consuming()


if __name__ == '__main__':
    main()
