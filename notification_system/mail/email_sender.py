import os
from pprint import pprint
import ssl
import smtplib
from json import loads
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pika
from dotenv import load_dotenv
import jinja2

from settings import SERVICE, HOST


load_dotenv()


def send_email(sender, password, domain, port, mail_add, name, body):
    """
    Отправляет письмо по параметрам
    :param port: порт домена почты
    :param sender: почта сайта
    :param password: пароль от почты
    :param domain: домен почты
    :param mail_add: адрес получателя
    :param name: имя получателя
    :param body: тело письма
    :return:
    """

    msg = MIMEMultipart()
    msg['From'] = 'Long Memory App'
    msg['To'] = name
    msg['Subject'] = f'Пора повторять материал!'
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP(domain, port=port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(sender, password)
            server.sendmail(sender, mail_add, msg.as_string())
    except Exception as e:
        print(e)


def get_body(name, notifications):
    """
    jinja2
    :param name: имя пользователя (получателя)
    :param notifications: активные напоминания пользователя
    :return:
    """
    loader = jinja2.FileSystemLoader('templates/email')  # загружаем папку с шаблоном
    j_env = jinja2.Environment(loader=loader)
    content = {
        'name': name,
        'notifications': notifications,
    }
    tpl = j_env.get_template('email_body.html')
    return tpl.render(content)


def send_for_user(data_set):
    """
    Раскладываем по полкам полученный массив данных из очереди относительно юзера
    Формируем тело письма
    Передаем на отправку

    :param data_set: массив данных из очереди
    """

    sender = os.getenv('SENDER')
    password = os.getenv('PASSWORD')
    domain = os.getenv('DOMAIN')
    port = os.getenv('PORT')

    for item in data_set:
        email_add = item['email']
        name = item['name']
        notifications = item['notifications']

        body = get_body(name, notifications)  # собираем тело письма
        send_email(sender, password, domain, port, email_add, name, body)  # передаем данные для отправки

        # Если напоминаний нет, нужна ли заглушка, типа
        # "вам нечего повторять сегодня, отдохните или начните изучать что-то новое
        # или почитайте статьи на нашем сайте"
        # Или просто письмо не отправлять?

    # print(f'[INFO] {len(data_set)} messages sent')


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()
    channel.queue_declare(queue=SERVICE)

    def callback(ch, method, properties, msg):
        body = loads(msg)
        pprint(f'--> Received message {body}')

        send_for_user(body)

    channel.basic_consume(queue=SERVICE,
                          auto_ack=True,
                          on_message_callback=callback)

    print(f'--- Waiting for {SERVICE} messages --- CTRL+C for exit')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
