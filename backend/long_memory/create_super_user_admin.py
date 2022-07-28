import os

import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'long_memory.settings'
django.setup()

from users.models import CustomUser


def create_superuser(username, email, password):
    CustomUser.objects.create_superuser(username=username,
                                        email=email,
                                        password=password)


if __name__ == "__main__":
    create_superuser('admin', 'admin@admin.ru', 'admin')
