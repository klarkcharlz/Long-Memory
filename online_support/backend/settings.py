from dotenv import dotenv_values


config = dotenv_values(".env")
SERVICE = 'SUPPORT'  # тут имя вашего сервиса email, telegram или vk
SENTRY_DSN = config['SENTRY_DSN']
TG_TOKEN = config['TG_TOKEN']
ADMIN_CHAT = int(config['ADMIN_CHAT'])
