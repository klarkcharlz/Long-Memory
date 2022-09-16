import random
from time import sleep

import vk_api
from vk_api.exceptions import ApiError
from sentry_sdk import capture_exception
from requests.exceptions import ReadTimeout, ConnectionError

from email_sender import send_email
from settings import VK_TOKEN, GROUP_ID


def get_vk_session():
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    return vk_session.get_api()


# Авторизуемся
vk = get_vk_session()


def write_msg(user_id, message):
    global vk
    while True:
        try:
            vk_data = dict(user_id=user_id,
                           peer_id=user_id,
                           random_id=random.getrandbits(32),
                           message=message)
            vk.messages.send(**vk_data)
        except ApiError as err:
            print(f'Некорректные данные для отправки сообщения:\n{vk_data}')
            print(err)
            capture_exception(err)
            break
        except (ReadTimeout, ConnectionError) as err:
            capture_exception(err)
            while True:
                try:
                    print("Переподключение к серверам ВК.")
                    vk = get_vk_session()
                except Exception as err:
                    print("Переподключение неудачно")
                    print(err)
                    capture_exception(err)
                    sleep(10)
                else:
                    break
        except Exception as err:
            print(f'Непредвиденная ошибка')
            capture_exception(err)
            break
        else:
            break


def is_id_valid(user_id, email):
    """
        Проверяет валидность id пользователя VK
    """
    try:
        vk.users.get(user_id=user_id)[0]['id']
    except Exception as err:
        capture_exception(err)
        print(f'Пользователя с id: {user_id} не существует.')
        send_email("Warning from Long Memory App", email, "Long Memory App",
                   f"Уважаемый пользователь Вы указали несуществующий id в VK: {user_id}.")
        return 0
    else:
        return 1


def is_member(user_id, email):
    """
    Проверяет, состоит ли пользователь в группе Long Memory
    """
    try:
        real_user_id = vk.users.get(user_id=user_id)[0]['id']
    except Exception as err:
        capture_exception(err)
        return 0
    else:
        if vk.groups.isMember(group_id=GROUP_ID, user_id=real_user_id, extended=0):
            return 1
        print(f'пользователь с id: {real_user_id} не является членом группы')
        send_email("Warning from Long Memory application", email, "Long Memory App",
                   "Уважаемый пользователь Вы не являетесь членом нашей группы.\n"
                   "Но Вы можете им стать:\nhttps://vk.com/public214673853")
        return 0


def is_allowed_msg(user_id, email):
    """
    Проверяет, разрешил ли пользователь получать сообщения от группы
    """
    try:
        real_user_id = vk.users.get(user_id=user_id)[0]['id']
    except Exception as err:
        capture_exception(err)
        return 0
    else:
        if vk.messages.isMessagesFromGroupAllowed(group_id=GROUP_ID, user_id=real_user_id)['is_allowed']:
            return 1
        print(f'пользователь с id: {real_user_id} запретил сообщения от группы')
        send_email("Warning from Long Memory application", email, "Long Memory App",
                   "Уважаемый пользователь Вы запретили сообщения от нашей группы:\nhttps://vk.com/public214673853")
        return 0


if __name__ == "__main__":
    email = 'klark.charlz@mail.ru'
    user_id = 232551335
    # print(vk.users.get(user_id=user_id))
    # write_msg(user_id, 'Hello')
    # print(is_id_valid(user_id, email))
    print(is_member(user_id, email))
    print(is_allowed_msg(user_id, email))
