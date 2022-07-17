from json import loads

import pika

SERVICE = 'vk'


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='receivers')

    def callback(ch, method, properties, body):
        body = loads(body)
        print(type(body))
        print(body)

    channel.basic_consume(queue=SERVICE, on_message_callback=callback, auto_ack=True)

    print(f'Start script {SERVICE}.\nWaiting for messages.')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    except Exception:
        channel.stop_consuming()


if __name__ == '__main__':
    main()
