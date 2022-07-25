import os
import ssl
import smtplib
from dotenv import load_dotenv

import jinja2

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
    load_dotenv()
    sender = os.getenv('SENDER')
    password = os.getenv('PASSWORD')
    domain = os.getenv('DOMAIN')
    for item in data_set:
        if len(item['notifications']) > 0:
            email_add = item['email']
            name = item['name']
            notifications = item['notifications']
            body = get_body(name, notifications)
            send_email(sender, password, domain, email_add, name, body)

            # Если напоминаний нет, нужна ли заглушка, типа
            # "вам нечего повторять сегодня, отдохните или начните изучать что-то новое
            # или почитайте статьи на нашем сайте"
            # Или просто письмо не отправлять?

    print(f'[INFO] {len(data_set)} messages sent')


if __name__ == '__main__':

    data = [
        {'email': 'stanislav.afk@gmail.com',
         'name': 'SuperMan',
         'notifications': [
             {'title': 'React Hooks',
              'description': 'UseState',
              'created_at': datetime.now(),
              'next_notification': datetime.now(),
              },
             {'title': 'React Hooks',
              'description': 'useEffect',
              'created_at': datetime.now(),
              'next_notification': datetime.now(),
              }
         ]},
        # {'email': 'skkolenov@gmail.com',
        #  'name': 'Mike',
        #  'notifications': [
        #      {'title': 'Python',
        #       'description': 'lambda function',
        #       'created_at': datetime.now(),
        #       'next_notification': datetime.now(),
        #       },
        #      {'title': 'JavaScript',
        #       'description': 'work with date',
        #       'created_at': datetime.now(),
        #       'next_notification': datetime.now(),
        #       }
        #  ]},
    ]
    send_for_user(data)
