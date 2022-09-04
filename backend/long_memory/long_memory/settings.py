import os
from pathlib import Path
from dotenv import dotenv_values

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

config = dotenv_values(".env")

sentry_sdk.init(
    dsn=config['SENTRY_DSN'],
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'longmemory.ru', '194.58.103.211']

# Application definition

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
    # ---------------
    'rest_framework.authtoken',
    'djoser',
    # for VK auth
    'oauth2_provider',
    'social_django',
    'rest_framework_social_oauth2',
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    'rest_framework_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'long_memory.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'long_memory_db',
#         'USER': 'admin',
#         'PASSWORD': 'admin',
#         'HOST': 'localhost',  # для локального запуска localhost, для контейнера db
#         'PORT': '54326',  # для локального запуска 54326, для контейнера 5432
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
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
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# djoser
DOMAIN_NAME = config['DOMAIN_NAME']
EMAIL_HOST = config['EMAIL_HOST']
EMAIL_PORT = int(config['EMAIL_PORT'])
EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
EMAIL_USE_SSL = True if config['EMAIL_USE_SSL'] == 'True' else False
EMAIL_USE_TLS = True if config['EMAIL_USE_TLS'] == 'True' else False
SERVER_EMAIL = EMAIL_HOST_USER

# ----------------------------------------------------- для VK и google авторизации
GOOGLE_API_KEY = 'AIzaSyDT6lyKdMYuERcsUM4zvP6b0dveZ3kIQMY'
SOCIAL_AUTH_VK_OAUTH_KEY = '51393425'
SOCIAL_AUTH_VK_OAUTH_SECRET = 'L6LjlrdJ8hDRyYilmpft'
# Взято из админки, таблица applications, запись Long_Memory
CLIENT_ID = 'ITEQN4Vn0aGHzN7zvZTsYAHIhnE6tC0ATf9JTUDq'
STATIC_URL = '/static/'





DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SERIALIZERS': {},
}
