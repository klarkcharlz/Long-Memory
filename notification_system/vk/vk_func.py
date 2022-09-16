import random
from time import sleep

import vk_api
from sentry_sdk import capture_exception
from requests.exceptions import ReadTimeout, ConnectionError
from notification_system.vk.simple_mail_sender import send_email
from settings import TG_TOKEN

def get_vk_session():
    vk_session = vk_api.VkApi(token=TG_TOKEN)
    return vk_session.get_api()


# Авторизуемся
vk = get_vk_session()


def write_msg(user_id, message):
    global vk
    try:
        vk_data = dict(user_id=user_id,
                    peer_id=user_id,
                    random_id=random.getrandbits(32),
                    message=message)
        vk.messages.send(**vk_data)
    except (ReadTimeout, ConnectionError):
        while True:
            global vk_data
            try:
                print("Переподключение к серверам ВК.")
                vk = get_vk_session()
                vk.messages.send(**vk_data) ##############################################!
            except Exception as err:
                print("Переподключение неудачно")
                print(err)
                capture_exception(err)
                sleep(10)
            else:
                break

def is_id_valid(user_id, email):
    '''
    Проверяет валидность id пользователя VK
    '''
    try:
        return 1 if vk.users.get(user_id=user_id)[0]['id'] else 0
    except:
        print(f'Пользователя с id: {id} не существует.')
        send_email("Warning from Long Memory application", email, "mehtievaa@mail.ru",
                       "Уважаемый пользователь ты указал неверный VK_id")
        return 0


def is_member(user_id, email):
    '''
    Проверяет, состоит ли пользователь в группе Long Memory
    '''
    user_id = vk.users.get(user_id=user_id)[0]['id']
    if vk.groups.isMember(group_id=214673853, user_id=user_id, extended=0):
        return 1
    print(f'пользователь с id: {id} не является членом группы')
    send_email("Warning from Long Memory application", email, "mehtievaa@mail.ru",
               "Уважаемый пользователь ты не являешься членом нашей группы... "
               "Что ж, поспеши им стать, пока не поздно!")
    return 0


def is_allowed_msg(user_id, email):
    '''
    Проверяет, разрешил ли пользователь получать сообщения от группы
    '''
    user_id = vk.users.get(user_id=user_id)[0]['id']
    if vk.messages.isMessagesFromGroupAllowed(group_id=214673853, user_id=user_id)['is_allowed']:
        return 1
    print(f'пользователь с id: {id} запретил сообщения от группы')
    send_email("Warning from Long Memory application", email, "mehtievaa@mail.ru",
                           "Уважаемый пользователь ты запретил сообщения от нашей группы... "
                           "Что ж, тёмный властелин уже выехал к тебе!")
    return 0

if __name__ == "__main__":
    email = 'mehtievaa@mail.ru'
    print(vk.users.get(user_id=638224708))
    write_msg(232551334, 'Hello')
    print(is_id_valid(4589, email))
    print(is_member(23255133, email))
    print(is_allowed_msg(638224708, email))