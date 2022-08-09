from json import loads
from asyncio import get_event_loop
from datetime import datetime
from dt_tg import currentTime

from dotenv import dotenv_values
import aio_pika
from aiogram import Bot, Dispatcher, executor, types
import client_kb as kb

SERVICE = 'telegram'  # тут имя вашего сервиса email, telegram или vk

NAME = 'test_rabbit'
USERNAME = 'test_rabbit_lm_bot'

# RABBIT_HOST = '127.0.0.1'
RABBIT_HOST = 'rabbitmq'

config = dotenv_values(".env")

TG_TOKEN = config['TOKEN']

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


async def send_message(chat_id, message):
    await bot.send_message(chat_id, message)


@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    await bot.send_message(message.from_user.id, f'{currentTime}', reply_markup=kb.greet_kb)
    await message.answer(f"Ваш ID: {message.chat.id}")


async def listen_rabbit_mq(loop):
    connection = await aio_pika.connect_robust(
        f"amqp://guest:guest@{RABBIT_HOST}/", loop=loop
    )

    async with connection:
        queue_name = SERVICE
        channel = await connection.channel()
        queue = await channel.declare_queue(
            queue_name,
            auto_delete=False
        )
        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    data = loads(message.body)
                    for user in data:
                        mess = f'{currentTime}, '
                        name = user['name']
                        mess += name + '.\n' + "Ты должен повторить сегодня:\n"
                        id = user['id']
                        for notification in user['notifications']:
                            mess += "\U0000272A " + notification['title'] + '\n' + notification['description'] + "\n\n"
                        try:
                            await send_message(id, mess)
                        except:
                            pass

                    if queue.name in message.body.decode():
                        break


if __name__ == '__main__':
    rabbit_loop = get_event_loop()
    rabbit_loop.create_task(listen_rabbit_mq(rabbit_loop))
    executor.start_polling(dp, skip_updates=True, loop=rabbit_loop)
