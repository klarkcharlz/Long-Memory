import datetime

currentTime = datetime.datetime.now()

if currentTime.hour < 12:
    currentTime = 'Доброе утро'
elif 12 <= currentTime.hour < 18:
    currentTime = 'Добрый день'
else:
    currentTime = 'Добрый вечер'
