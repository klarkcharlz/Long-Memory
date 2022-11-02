import os
import argparse

import django
from dotenv import dotenv_values
import sentry_sdk
from sentry_sdk import capture_exception

config = dotenv_values(".env")
sentry_sdk.init(
    dsn=config['SENTRY_DSN'],
    traces_sample_rate=1.0
)

email = config['EMAIL_HOST_USER']

parser = argparse.ArgumentParser(description='Create superuser.')
parser.add_argument('user', type=str)
parser.add_argument('password', type=str)

args = parser.parse_args()

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.prod'
django.setup()

from users.models import CustomUser


def create_superuser(username, email, password):
    user = CustomUser.objects.create_superuser(username=username,
                                               email=email,
                                               password=password)
    user.is_active = True
    user.save()


if __name__ == "__main__":
    try:
        create_superuser(args.user, email, args.password)
    except Exception as err:
        capture_exception(err)
        print(err)
