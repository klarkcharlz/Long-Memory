from json import loads
from datetime import datetime
from time import sleep
from pprint import pprint

import pika
import sentry_sdk
from requests import ReadTimeout
from sentry_sdk import capture_exception
from pika.exceptions import AMQPConnectionError
from vk_api import vk_api


from vk_func import write_msg, is_id_valid, is_member, is_allowed_msg
from settings import SERVICE, HOST, SENTRY_DSN, ACCESS_TOKEN

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
        print(f'{datetime.now()} - Принял сообщение:')
        body = loads(body)
        # print(type(body))
        print(body)

        for user in body:
            id = user["id"]
            email = user['email']
            if not is_id_valid(id, email):
                continue
            if not is_allowed_msg(id, email):
                continue
            if not is_member(id, email):
                continue

            message = f'Привет {user["name"]},\n сегодня {datetime.now()} тебе нужно повторить:\n\n'
            for item in user["notifications"]:
                message += f'\u2023{item["title"]}:\n{item["description"]}\n\n'
            write_msg(id, message)




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
