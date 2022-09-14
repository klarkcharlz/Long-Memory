from settings import (
    SENDER,
    PASSWORD,
    PORT,
    DOMAIN
)

from email_sender import send_email, get_body


if __name__ == "__main__":
    email_add = "klark.charlz@mail.ru"
    name = "Николай"

    notifications = [{'title': 'React hooks',
                      'description': 'useState',
                      'created_at': '2022-09-10 21:23:44.833421+00:00',
                      'next_notification': '2022-09-11 21:23:44.831450+00:00'}]
    body = get_body(name, notifications)

    send_email(SENDER, PASSWORD, DOMAIN, PORT, email_add, name, body)
