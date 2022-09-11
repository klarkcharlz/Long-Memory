import random
from time import sleep

import vk_api
from sentry_sdk import capture_exception
from requests.exceptions import ReadTimeout, ConnectionError

from settings import TG_TOKEN


# Авторизуемся
vk_session = vk_api.VkApi(token=TG_TOKEN)
vk = vk_session.get_api()


def write_msg(user_id, message):
    global vk
    try:
        data = dict(user_id=user_id,
                    peer_id=user_id,
                    random_id=random.getrandbits(32),
                    message=message)
        try:
            vk.messages.send(**data)
        except Exception as err:
            print(type(err))
            print(err)
            sleep(1)
    except (ReadTimeout, ConnectionError):
        while True:
            try:
                print("Переподключение к серверам ВК.")
                vk = vk_api.VkApi(token=TG_TOKEN)
            except Exception as err:
                print("Переподключение неудачно")
                print(err)
                capture_exception(err)
                sleep(10)
            else:
                break


if __name__ == "__main__":
    write_msg(232551334, 'Hello')
