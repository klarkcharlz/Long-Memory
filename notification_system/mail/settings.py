from dotenv import dotenv_values

config = dotenv_values(".env")

SERVICE = 'email'
SENDER = config['SENDER']
PASSWORD = config['PASSWORD']
DOMAIN = config['DOMAIN']
PORT = config['PORT']
RABBIT_HOST = config['RABBIT_HOST']
SENTRY_DSN = config['SENTRY_DSN']
