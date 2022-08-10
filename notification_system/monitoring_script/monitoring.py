from datetime import datetime

from time import sleep

from sender import send
import sentry_sdk
import schedule
from sentry_sdk import capture_exception
from check_db import check_db

sentry_sdk.init(
    dsn="https://3d4eb3a8d99c407e964e68a2ae318ab5@o1347801.ingest.sentry.io/6630612",
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
