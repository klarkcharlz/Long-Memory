from json import loads
from datetime import datetime
from time import sleep
from pprint import pprint

import pika
import sentry_sdk
from sentry_sdk import capture_exception
from pika.exceptions import AMQPConnectionError

from vk_func import write_msg
from settings import SERVICE, HOST, SENTRY_DSN


sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0
)


def main():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
        except AMQPConnectionError as err:
            capture_exception(err)
            print("Нет соединения с Rabbit MQ")
            sleep(5)
        else:
            break
    channel = connection.channel()

    def callback(ch, method, properties, body):
        # pprint(f'{datetime.now()} - Принял сообщение:')
        body = loads(body)
        # pprint(type(body))
        # pprint(body)
        for user in body:
            message = f'Привет {user["name"]}!\nСегодня {datetime.now().date()} тебе нужно повторить:\n\n'
            id = int(user['id'])
            for notification in user["notifications"]:
                message += f"\U0000272A {notification['title']}:\n{notification['description']}\n\n"
            write_msg(id, message.rstrip())

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
