from json import loads
from asyncio import get_event_loop, sleep
from datetime import datetime
from dt_tg import currentTime
from time import sleep as block_sleep
import aio_pika
from aiogram import Bot, Dispatcher, executor, types
import sentry_sdk
from sentry_sdk import capture_exception

import client_kb as kb

from settings import SERVICE, RABBIT_HOST, TG_TOKEN, SENTRY_DSN

sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=1.0
)

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


async def send_message(chat_id, message):
    await bot.send_message(chat_id, message)


@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    await bot.send_message(message.from_user.id, f'{currentTime}\nВаш ID: {message.chat.id}', reply_markup=kb.greet_kb)


async def listen_rabbit_mq(loop):
    while True:
        try:
            connection = await aio_pika.connect_robust(
                f"amqp://guest:guest@{RABBIT_HOST}/", loop=loop
            )
        except Exception as err:
            print(err)
            capture_exception(err)
            print('Не удалось подключиться к RabbitMQ')
            await sleep(10)
        else:
            break

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
                        except Exception as err:
                            print(err)
                            capture_exception(err)
                            print('Не удалось отправить сообщение пользователю')

                    if queue.name in message.body.decode():
                        break


if __name__ == '__main__':
    rabbit_loop = get_event_loop()
    rabbit_loop.create_task(listen_rabbit_mq(rabbit_loop))
    while True:
        try:
            executor.start_polling(dp, skip_updates=True, loop=rabbit_loop)
        except Exception as err:
            print(err)
            print('Не удалось запустить бота')
            block_sleep(10)
        else:
            break
