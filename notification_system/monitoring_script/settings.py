from dotenv import dotenv_values


config = dotenv_values(".env")

SENTRY_DSN = config['SENTRY_DSN']

# для локальной разработки
# RABBIT_URL = 'localhost'
# BD_STRING = 'postgresql://admin:admin@localhost:54326/long_memory_db'

# для докера
BD_STRING = 'postgresql://admin:admin@db:5432/long_memory_db'
RABBIT_URL = 'rabbitmq'
