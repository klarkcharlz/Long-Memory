import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .common import *


config = dotenv_values(".env")

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'long_memory_db',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'db',  # для локального запуска localhost, для контейнера db
        'PORT': '5432',  # для локального запуска 54326, для контейнера 5432
    }
}

sentry_sdk.init(
    dsn=config['SENTRY_DSN'],
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
