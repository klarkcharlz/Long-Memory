import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint

# Примерный формат входящего сообщения
ext_mess = [{'user_id': 638224708},
            {'user_name': 'Aidyn'},
            {'title': 'Programming'},
            {'description': 'Hello guys, if you want '
                            'to learn Python in 2022 and looking for '
                            'some Free Websites and free Python tutorials '
                            'then you have come to the right place.'}]


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, "random_id": randint(11111, 99999)})


# API-ключ, потом куда-нибудь спрячу подальше
token = "vk1.a.-7JetwuZpvfBmV-LctJ3gc-0Ko79he-YZHHFjGpwwrG5eaSv1jOVXrS732ayalq_BDxEbQktcUFxCsevIBoEXl8BPjJJAqCRE1e4Ae0upvrOes0__bWESNiZn6FlZovADCUjpp4l6Pf59sef7_3cwwTmb-53etqvdwYj4tgHL1hIa2EBbjqMin9-r-oKasNN"

# Авторизуемся
vk = vk_api.VkApi(token=token)

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
    write_msg(ext_mess[0]['user_id'],
              f'Hey lazy asshole {ext_mess[1]["user_name"]}, '
              f'\nyou need to do: {ext_mess[2]["title"]}'
              f'\nspecifically: {ext_mess[3]["description"][:40:]}...')
    write_msg(638224708, "Хой")
    write_msg(638224708, "Хэй")
