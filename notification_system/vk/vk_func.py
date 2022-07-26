from random import randint
from settings import SECRET_KEY
import vk_api

# Примерный формат входящего сообщения

# external_mess = {
#     'vk': [
#         {
#             'id': '638224708',
#             'name': 'Ivan',
#             'notifications': [
#                 {
#                     'title': 'programming Python les_2',
#                     'description': 'Освоить на практике более 30 проблем программирования',
#                     'created_at': datetime(2022, 7, 20, 0, 0),
#                     'next_notifications': datetime(2022, 7, 28, 0, 0)
#                 },
#                 {
#                     'title': 'programming Python les_3',
#                     'description': 'Собрать два проекта, чтобы применить на практике новые знания',
#                     'created_at': datetime(2022, 7, 20, 0, 0),
#                     'next_notifications': datetime(2022, 7, 31, 0, 0)
#                 }
#             ]
#         },
#         {
#             'id': '638224708',
#             'name': 'Boris',
#             'notifications': [
#                 {
#                     'title': 'programming Python les_4',
#                     'description': 'Ознакомиться хотя бы с двумя фреймворками',
#                     'created_at': datetime(2022, 7, 20, 0, 0),
#                     'next_notifications': datetime(2022, 8, 3, 0, 0)
#                 }
#             ]
#         },
#         {
#             'id': '638224708',
#             'name': 'John',
#             'notifications': [
#                 {
#                     'title': 'programming Python les_1',
#                     'description': 'Ознакомиться с основными понятиями (переменная, условие, список, цикл, функция)',
#                     'created_at': datetime(2022, 7, 20, 0, 0),
#                     'next_notifications': datetime(2022, 7, 25, 0, 0)
#                 },
#                 {
#                     'title': 'programming Python les_5',
#                     'description': 'Начать работу с IDE (средой разработки), Github, хостингом, сервисами и т. д.',
#                     'created_at': datetime(2022, 7, 20, 0, 0),
#                     'next_notifications': datetime(2022, 8, 6, 0, 0)
#                 }
#             ]
#         }
#     ],
#     'telegram': [],
#     'email': []
# }


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": randint(11111, 99999)})

# Авторизуемся
vk = vk_api.VkApi(token=SECRET_KEY)





