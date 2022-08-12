from dotenv import dotenv_values

SERVICE = 'vk'

config = dotenv_values(".env")

TG_TOKEN = config['TOKEN']
HOST = 'rabbitmq'
SENTRY_DSN = config['SENTRY_DSN']
