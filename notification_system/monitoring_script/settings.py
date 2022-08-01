import os

# sqlite3 develop path
cur_dir = os.path.dirname(os.path.abspath(__file__))
par = os.path.abspath(os.path.join(cur_dir, os.pardir))
par = os.path.abspath(os.path.join(par, os.pardir))
bd_path = os.path.join(par, 'backend', 'long_memory')
BD_STRING = f'sqlite:///{bd_path}/db.sqlite3'

RABBIT_URL = 'localhost'


# for docker
# RABBIT_URL = 'rabbitmq'
# BD_STRING = ''
