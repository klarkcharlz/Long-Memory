import random
from time import sleep

import vk_api
from sentry_sdk import capture_exception
from requests.exceptions import ReadTimeout, ConnectionError

from settings import VK_TOKEN


def get_session():
    while True:
        try:
            vk_session = vk_api.VkApi(token=VK_TOKEN)
        except Exception as err:
            capture_exception(err)
            print('Не удалось подключиться к вк')
            print('Переподключение...')
            sleep(60)
        else:
            return vk_session.get_api()


# Авторизуемся
vk = get_session()


def write_msg(user_id, message):
    global vk
    while True:
        try:
            data = dict(user_id=user_id,
                        peer_id=user_id,
                        random_id=random.getrandbits(32),
                        message=message)
            vk.messages.send(**data)
        except (ReadTimeout, ConnectionError) as err:
            print('Переподключение к вк')
            capture_exception(err)
            vk = get_session()
        else:
            break


if __name__ == "__main__":
    write_msg(232551334, 'Hello')
