import datetime
import os
import ssl
import smtplib
from json import loads
import pika
from dotenv import load_dotenv

import jinja2

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SERVICE = 'email'
load_dotenv()


def send_email(sender, password, domain, mail_add, name, body):
    """
    Отправляет письмо по параметрам
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
        with smtplib.SMTP(domain, port=587) as server:
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

    def datetime_format(value, format='short'):
        date = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
        if format == 'full':
            format = "%d.%m.%Y в %H:%M"
        elif format == 'short':
            format = "%d.%m.%y"

        date = date.strftime(format)
        return date

    j_env.filters["datetime_format"] = datetime_format

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

    for item in data_set:
        email_add = item['email']
        name = item['name']
        notifications = item['notifications']

        body = get_body(name, notifications)  # собираем тело письма
        send_email(sender, password, domain, email_add, name, body)  # передаем данные для отправки

        # Если напоминаний нет, нужна ли заглушка, типа
        # "вам нечего повторять сегодня, отдохните или начните изучать что-то новое
        # или почитайте статьи на нашем сайте"
        # Или просто письмо не отправлять?

    print(f'[INFO] {len(data_set)} messages sent')


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv('SERVER')))
    channel = connection.channel()
    channel.queue_declare(queue=SERVICE)

    def callback(ch, method, properties, msg):
        body = loads(msg)
        # pprint(f'--> Received message {body}')

        send_for_user(body)

    channel.basic_consume(queue=SERVICE,
                          auto_ack=True,
                          on_message_callback=callback)

    print('--- Waiting for messages --- CTRL+C for exit')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
