# BD_STRING = 'sqlite:////Users/nikolajpetrov/Documents/gb_lm/Long-Memory/backend/long_memory/db.sqlite3'
import pathlib
from pathlib import Path


RABBIT_URL = 'localhost'



# for docker
home_dir = Path.cwd().parents[1]
db_dir = home_dir / 'backend' / 'long_memory'
BD_STRING = f'sqlite:///{db_dir}/db.sqlite3'
print(BD_STRING)