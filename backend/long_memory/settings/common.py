import os
from pathlib import Path
from dotenv import dotenv_values

config = dotenv_values(".env")

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config['SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost',
                 'longmemory.ru',
                 '194.58.103.211',
                 '0.0.0.0']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    # my applications
    'users.apps.UsersConfig',
    'notifications.apps.NotificationsConfig',
    'bug_report.apps.BugReportConfig',
    # ---------------
    'rest_framework.authtoken'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'long_memory.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'long_memory.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'
USE_TZ = True

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://localhost',
    'http://localhost:80',
    'http://longmemory.ru:8000',
    'http://longmemory.ru',

    'https://localhost:3000',
    'https://127.0.0.1:3000',
    'https://127.0.0.1:8000',
    'https://localhost:8000',
    'https://localhost',
    'https://localhost:80',
    'https://longmemory.ru:8000',
    'https://longmemory.ru',
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://localhost',
    'http://localhost:80',
    'http://longmemory.ru:8000',
    'http://longmemory.ru',

    'https://localhost:3000',
    'https://127.0.0.1:3000',
    'https://127.0.0.1:8000',
    'https://localhost:8000',
    'https://localhost',
    'https://localhost:80',
    'https://longmemory.ru:8000',
    'https://longmemory.ru'
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'www/static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'www/media')
MEDIA_URL = '/media/'

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

EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
EMAIL_HOST = config['EMAIL_HOST']
EMAIL_PORT = config['EMAIL_PORT']
DOMAIN_NAME = config['DOMAIN_NAME']
EMAIL_USE_TLS = True
