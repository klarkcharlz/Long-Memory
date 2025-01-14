from datetime import datetime
from time import sleep
import logging

from sender import send
import sentry_sdk
import schedule
from sentry_sdk import capture_exception
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from dotenv import dotenv_values

from check_db import check_db
from settings import SENTRY_DSN

config = dotenv_values(".env")

sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0,
    integrations=[
        SqlalchemyIntegration(),
    ]
)


def job():
    logging.warning('Start collect data.')
    try:
        data = check_db()
        logging.warning('Get data from db')
        for service, data in data.items():
            if data:
                logging.warning(f'{datetime.now()} - send message to {service}:')
                send(service, data)
            else:
                logging.warning(f'{datetime.now()} - empty data to {service}:')
    except Exception as err:
        logging.warning(err)
        capture_exception(err)
        sleep(10)


# schedule.every(3600).seconds.do(job)
schedule.every().day.at("05:30").do(job)

if __name__ == "__main__":
    logging.warning('Start Script.')
    job()  # ToDo для тестирования
    while True:
        schedule.run_pending()
        sleep(10)
