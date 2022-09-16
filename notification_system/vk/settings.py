from dotenv import dotenv_values

SERVICE = 'vk'

config = dotenv_values(".env")

VK_TOKEN = config['VK_TOKEN']
RABBIT_HOST = config['RABBIT_HOST']
SENTRY_DSN = config['SENTRY_DSN']
EMAIL = config['EMAIL_SENDER']
EMAIL_PASSWORD = config['EMAIL_PASSWORD']
DOMAIN = config['DOMAIN']
PORT = config['PORT']
GROUP_ID = config['GROUP_ID']
