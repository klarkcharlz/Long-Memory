"""
Использовался для тестирования скрипта мониторющего базу раз,
подготавливающего данные и отправляющего потребителям
"""

import os
import random

from faker import Faker
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'long_memory.settings'
django.setup()

from users.models import CustomUser
from notifications.models import Notifications

fake = Faker()


def create_superuser(username, email, password):
    CustomUser.objects.create_superuser(username=username,
                                        email=email,
                                        password=password)


def fill_test_users(total: int):
    """
    Создает рандомны[ пользователей в базе.
    :param total:
    :return:
    """
    for _ in range(total):
        CustomUser.objects.create(username=fake.user_name(),
                                  first_name=fake.first_name(),
                                  email=fake.email(),
                                  vk_id=fake.random_int(),
                                  telegram_id=fake.random_int(),
                                  email_reminders=fake.boolean(),
                                  telegram_reminders=fake.boolean(),
                                  vk_reminders=fake.boolean(),
                                  password=fake.password()
                                  )


def fill_test_notifications(total: int):
    users_id = CustomUser.objects.all()
    for _ in range(total):
        Notifications.objects.create(user_id=random.choice(users_id),
                                     title=fake.text().split(".")[0],
                                     description=fake.text().split(".")[0])


if __name__ == "__main__":
    # Раскомментировать нужное
    create_superuser('admin', 'admin@admin.ru', 'admin')
    # fill_test_users(10)
    # fill_test_notifications(100)
