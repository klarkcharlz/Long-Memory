from dotenv import dotenv_values


config = dotenv_values(".env")

SENTRY_DSN = config['SENTRY_DSN']
BD_STRING = config['BD_STRING']
RABBIT_URL = config['RABBIT_URL']
