from .common import *

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
