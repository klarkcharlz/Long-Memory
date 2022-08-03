from datetime import datetime

data = [
    {'id': 1234567,  # для почты будет поле email
     'name': 'SuperMan',
     'notifications': [
         {'title': 'React Hooks',
          'description': 'UseState',
          'created_at': datetime.now(),
          'next_notification': datetime.now(),
          },
         {'title': 'React Hooks',
          'description': 'useEffect',
          'created_at': datetime.now(),
          'next_notification': datetime.now(),
          }
     ]},
    {'id': 432134324,
     'name': 'Mike',
     'notifications': [
         {'title': 'Python',
          'description': 'lambda function',
          'created_at': datetime.now(),
          'next_notification': datetime.now(),
          },
         {'title': 'JavaScript',
          'description': 'work with date',
          'created_at': datetime.now(),
          'next_notification': datetime.now(),
          }
     ]},
]


for user in data:
    message = "Hello "
    name = user['name']
    message += name + '.\n' + "You must repeat today:\n"
    id = user['id']  # тут будет нужный вам для рассылки id или почта
    for notification in user['notifications']:
        message += "\U0000272A " + notification['title'] + '\n'
    # send(id, message)
    print(message)
    # функция для отправки (message, id)

"""
Подумайте как вы можете использовать поля description, created_at, next_notification
что бы сообщение не выглядело громоздко и если не нужны не используйте вовсе.
"""