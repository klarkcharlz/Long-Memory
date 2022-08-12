from datetime import datetime
from time import sleep

from sender import send
import sentry_sdk
import schedule
from sentry_sdk import capture_exception
from dotenv import dotenv_values

from check_db import check_db
from settings import SENTRY_DSN


config = dotenv_values(".env")

sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0
)


def job():
    try:
        data = check_db()
        print(f'Get data from db: {data}')
        for service, data in data.items():
            if data:
                print(f'{datetime.now()} - send message to {service}:')
                send(service, data)
            else:
                print(f'{datetime.now()} - empty data to {service}:')
    except Exception as err:
        print(err)
        sleep(10)
        capture_exception(err)


# schedule.every(3600).seconds.do(job)
schedule.every().day.at("09:30").do(job)

if __name__ == "__main__":
    print('Start Script.')
    job()  # ToDo убрать на релизе
    while True:
        schedule.run_pending()
        sleep(10)
