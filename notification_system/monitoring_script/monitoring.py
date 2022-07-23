from datetime import datetime

import schedule
from time import sleep

from sender import send
from check_db import check_db


def job():
    data = check_db()
    print(f'Get data from db: {data}')
    for service, data in data.items():
        print(f'{datetime.now()} - send message to {service}:')
        send(service, data)


schedule.every(5).seconds.do(job)
# schedule.every().day.at("10:30").do(job)


if __name__ == "__main__":
    print('Start Script.')
    while True:
        schedule.run_pending()
        sleep(1)
