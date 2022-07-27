from json import loads
from datetime import datetime
from time import sleep
from vk_func import write_msg
import pika
from pika.exceptions import AMQPConnectionError

SERVICE = 'vk'  # тут имя вашего сервиса email, telegram или vk

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
        for dic in body:
            if len(dic["notifications"]) > 1:
                for i in range(len(dic["notifications"])):
                    write_msg(dic['id'], f'Привет {dic["name"]}, '
                                         f'\nтебе надо сделать: {dic["notifications"][i]["title"]},'
                                         f'\nа именно: {dic["notifications"][i]["description"]}...')
            else:
                write_msg(dic['id'], f'Привет {dic["name"]}, '
                                     f'\nтебе надо сделать: {dic["notifications"][0]["title"]},'
                                     f'\nа именно: {dic["notifications"][0]["description"]}...')

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