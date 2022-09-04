from dotenv import dotenv_values

SERVICE = 'vk'

config = dotenv_values(".env")

TG_TOKEN = config['TOKEN']
# HOST = 'rabbitmq'  # для контейнеров
# HOST = 'localhost'  # для локального запуска
SENTRY_DSN = config['SENTRY_DSN']
ACCESS_TOKEN = config['token']
HOST = 'localhost'
EMAIL = config['email_sender']
EMAIL_PASSWORD = config['email_pswd']