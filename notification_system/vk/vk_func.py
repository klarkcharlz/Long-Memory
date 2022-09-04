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
    data = dict(user_id=user_id,
                peer_id=user_id,
                random_id=random.getrandbits(32),
                message=message)
    vk.messages.send(**data)


def is_id_valid(user_id):
    '''
    Проверяет валидность id пользователя VK
    '''
    try:
        return 1 if vk.users.get(user_id=user_id)[0]['id'] else 0
    except:
        return 0

def is_member(user_id):
    '''
    Проверяет, состоит ли пользователь в группе Long Memory
    '''
    return vk.groups.isMember(group_id=214673853, user_id=user_id, extended=0)

def is_allowed_msg(user_id):
    '''
    Проверяет, разрешил ли пользователь получать сообщения от группы
    '''
    return vk.messages.isMessagesFromGroupAllowed(group_id=214673853, user_id=user_id)['is_allowed']

if __name__ == "__main__":
    print(vk.users.get(user_id=638224708))
    write_msg(232551334, 'Hello')
    print(is_id_valid(4589))
    print(is_member(23255133))
    print(is_allowed_msg(638224708))