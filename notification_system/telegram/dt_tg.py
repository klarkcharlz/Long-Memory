from datetime import datetime, timedelta


def get_greeting():
    currentTime = datetime.now() + timedelta(hours=3)

    if 5 < currentTime.hour < 12:
        greeting = 'Доброе утро'
    elif 12 <= currentTime.hour < 18:
        greeting = 'Добрый день'
    elif 18 <= currentTime.hour < 23:
        greeting = 'Добрый вечер'
    else:
        greeting = 'Доброй ночи'

    return greeting
