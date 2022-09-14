from dotenv import dotenv_values


config = dotenv_values(".env")
SERVICE = 'telegram'  # тут имя вашего сервиса email, telegram или vk
RABBIT_HOST = config['RABBIT_HOST']
TG_TOKEN = config['TG_TOKEN']
SENTRY_DSN = config['SENTRY_DSN']
