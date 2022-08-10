from pprint import pprint
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import BD_STRING
from models import UsersCustomuser, NotificationsNotification

engine = create_engine(BD_STRING)
Session = sessionmaker(bind=engine)
session = Session()


def check_db():
    """Сбор данных для потребителей-отправителей"""
    telegram_data = []
    vk_data = []
    email_data = []

    # сбор всех кто подписался хоть на одну рассылку
    subscribers = session.query(UsersCustomuser).filter(
        (UsersCustomuser.vk_reminders == True)
        | (UsersCustomuser.telegram_reminders == True)
        | (UsersCustomuser.email_reminders == True))
    for user in subscribers:
        id = user.id
        name = user.first_name if user.first_name else user.username

        notifications = session.query(NotificationsNotification).\
            filter((NotificationsNotification.user_id_id == id)
                   & (NotificationsNotification.next_notifications <= datetime.now())).\
            order_by(NotificationsNotification.next_notifications)
        notifications_list = []
        for notification in notifications:
            notifications_list.append({'title': notification.title,
                                       'description': notification.description,
                                       'created_at': notification.created_at,
                                       'next_notification': notification.next_notifications,
                                       })
        if notifications_list:
            if user.vk_reminders:
                vk_data.append({'id': user.vk_id,
                                'name': name,
                                'notifications': notifications_list})
            if user.telegram_reminders:
                telegram_data.append({'id': user.telegram_id,
                                      'name': name,
                                      'notifications': notifications_list})
            if user.email_reminders:
                email_data.append({'email': user.email,
                                   'name': name,
                                   'notifications': notifications_list})

    services_data = {
        'vk': vk_data,
        'telegram': telegram_data,
        'email': email_data
    }
    # with open('test.json', 'w') as f:
    #     dump(services_data, f, indent=4, sort_keys=True, default=str)

    return services_data


if __name__ == "__main__":
    data = check_db()
    pprint(check_db())
    for services, users in data.items():
        print(f'{services} subscribe {len(users)} users.')
