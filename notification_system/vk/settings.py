from dotenv import dotenv_values


config = dotenv_values(".env")

SERVICE = 'vk'
VK_TOKEN = config['VK_TOKEN']
RABBIT_HOST = config['RABBIT_HOST']
SENTRY_DSN = config['SENTRY_DSN']
