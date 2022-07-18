import ssl
import smtplib
import jinja2

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from notifications.models import Notifications
from users.models import CustomUser


def send_email(sender, password, mail_add, username, body):
    """
    Отправляет письмо по параметрам
    :param sender: почта сайта
    :param password: пароль от почты
    :param mail_add: адрес получателя
    :param username: имя получателя
    :param body: тело письма
    :return:
    """

    domain = f"smtp.{sender.split('@')[1]}"  # домен нашей почты
    msg = MIMEMultipart()
    msg['From'] = 'Long Memory App'
    msg['To'] = username
    msg['Subject'] = f'Пора повторять карточки!'
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP(domain, port=587) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(sender, password)
            server.sendmail(sender, mail_add, msg.as_string())
    except Exception as e:
        print(e)


def get_body(username, notifications):
    """
    jinja2
    :param username: имя пользователя (получателя)
    :param notifications: активные напоминания пользователя
    :return:
    """
    loader = jinja2.FileSystemLoader('templates/email')  # загружаем папку с шаблоном
    j_env = jinja2.Environment(loader=loader)
    content = {
        'username': username,
        'notifications': notifications,
    }
    tpl = j_env.get_template('email.html')
    return tpl.render(content)


def send_for_user():
    """
    определяет юзеров
        если юзер активен
            грузим его активные нотифы
        отправляем инфу на формирование тела письма, получаем тело
        отдаем тело и параметры на отправку
    """
    sender = ''  # надо доставать из env
    password = ''  # надо доставать из env
    users = CustomUser.objects.filter(is_active=True)
    for user in users:
        notifications = Notifications.objects.filter(user_id=user.pk,
                                                     is_active=True,
                                                     next_notification__lte=datetime.now())
        mail_add = user.email
        username = user.username
        body = get_body(username, notifications)
        send_email(sender, password, mail_add, username, body)


"""
Естественно будет дорабатываться, нужно изучить Rabbir, вопрос с необходимостью SSL сертификата
"""