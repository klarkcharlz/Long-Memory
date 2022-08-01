import random
from settings import TG_TOKEN
import vk_api

# Авторизуемся
vk_session = vk_api.VkApi(token=TG_TOKEN)
vk = vk_session.get_api()


def write_msg(user_id, message):
    data = dict(user_id=user_id,
                peer_id=user_id,
                random_id=random.getrandbits(32),
                message=message)
    vk.messages.send(**data)


if __name__ == "__main__":
    write_msg(232551334, 'Hello')
