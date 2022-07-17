from collections import defaultdict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import BD_STRING
from models import UsersCustomuser, NotificationsNotification


engine = create_engine(BD_STRING)
Session = sessionmaker(bind=engine)
session = Session()


def check_db():
    data = defaultdict(list)

    subscribers = session.query(UsersCustomuser.id)
    for user_id in subscribers:
        id = user_id[0]
        notifications = session.query(NotificationsNotification).filter(NotificationsNotification.user_id_id == id)
        for notification in notifications:
            data[id].append(notification.title)
    return data


if __name__ == "__main__":
    print(check_db())
