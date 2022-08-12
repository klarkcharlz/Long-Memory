from dotenv import dotenv_values


config = dotenv_values(".env")
SERVICE = 'telegram'  # тут имя вашего сервиса email, telegram или vk

BOT_NAME = 'test_rabbit'
BOT_USERNAME = 'test_rabbit_lm_bot'

# RABBIT_HOST = 'localhost'  # для локального запуска
RABBIT_HOST = 'rabbitmq'  # для docker

TG_TOKEN = config['TOKEN']

SENTRY_DSN = config['SENTRY_DSN']
