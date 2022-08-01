from dotenv import dotenv_values

SERVICE = 'vk'

config = dotenv_values(".env")

TG_TOKEN = config['TOKEN']
HOST = 'localhost'
