# BD_STRING = 'sqlite:////Users/nikolajpetrov/Documents/gb_lm/Long-Memory/backend/long_memory/db.sqlite3'
import os
import pathlib
from pathlib import Path


# sqlite3 develop path os
# cur_dir = os.path.dirname(os.path.abspath(__file__))
# par = os.path.abspath(os.path.join(cur_dir, os.pardir))
# par = os.path.abspath(os.path.join(par, os.pardir))
# bd_path = os.path.join(par, 'backend', 'long_memory')
# BD_STRING = f'sqlite:///{bd_path}/db.sqlite3'

# sqlite3 develop path pathlib
# home_dir = Path.cwd().parents[1]
# db_dir = home_dir / 'backend' / 'long_memory'
# BD_STRING = f'sqlite:///{db_dir}/db.sqlite3'
# RABBIT_URL = 'localhost'
# postgres
# BD_STRING = 'postgresql://admin:admin@localhost:54326/long_memory_db'

# for docker
BD_STRING = 'postgresql://admin:admin@db:5432/long_memory_db'
RABBIT_URL = 'rabbitmq'

