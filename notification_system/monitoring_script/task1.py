from datetime import datetime
from random import randint

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


# API-ключ, потом куда-нибудь спрячу подальше
token = "vk1.a.C8q2p03gCKgjKEC3FSncwX2GKUfmkddd84rQ1oMY704unb67dkb0C35sAphHX_Oz-cMFo8rzGbmTlggPw3dtO9n38955CVnHhRXsZXwE9De3QTPFXH34fLk7Q6lfN3FT8zxjmIKxvbPQ0Yss0MsZjbL8ihBZWur7-qVJWg-oHAaBkpB_9f7wlCUzGj2UEBmr"

# Авторизуемся
vk = vk_api.VkApi(token=token)

def callback(external_mess):
    vk_sender = external_mess["vk"]
    for dic in vk_sender:
        if len(dic["notifications"]) > 1:
            for i in range(len(dic["notifications"])):
                write_msg(dic['id'], f'Hey lazy asshole {dic["name"]}, '
                                     f'\nyou need to do: {dic["notifications"][i]["title"]}'
                                     f'\nspecifically: {dic["notifications"][i]["description"]}...')
        else:
            write_msg(dic['id'], f'Hey lazy asshole {dic["name"]}, '
                                 f'\nyou need to do: {dic["notifications"][0]["title"]}'
                                 f'\nspecifically: {dic["notifications"][0]["description"]}...')
# Работа с сообщениями
# Эта часть нам по сути не нужна
# мы тупо пересылаем извещения из "кролика" пользователю
# longpoll = VkLongPoll(vk)
#
# # Основной цикл
# for event in longpoll.listen():
#
#     # Если пришло новое сообщение
#     if event.type == VkEventType.MESSAGE_NEW:
#
#         # Если оно имеет метку для меня( то есть бота)
#         if event.to_me:
#
#             # Сообщение от пользователя
#             request = event.text
#
#             # Каменная логика ответа
#             if request == "привет":
#                 print(event.user_id)
#                 write_msg(event.user_id, "Хай")
#             elif request == "пока":
#                 print(event.user_id)
#                 write_msg(event.user_id, "Пока((")
#             else:
#                 write_msg(event.user_id, "Не поняла вашего ответа...")

if __name__ == '__main__':
    vk_sender = external_mess["vk"]
    for dic in vk_sender:
        if len(dic["notifications"]) > 1:
            for i in range(len(dic["notifications"])):
              write_msg(dic['id'], f'Hey lazy asshole {dic["name"]}, '
                      f'\nyou need to do: {dic["notifications"][i]["title"]}'
                      f'\nspecifically: {dic["notifications"][i]["description"]}...')
        else:
            write_msg(dic['id'], f'Hey lazy asshole {dic["name"]}, '
                  f'\nyou need to do: {dic["notifications"][0]["title"]}'
                  f'\nspecifically: {dic["notifications"][0]["description"]}...')
