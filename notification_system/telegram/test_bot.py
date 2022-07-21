from json import loads
from asyncio import get_event_loop
from datetime import datetime

import aio_pika
from aiogram import Bot, Dispatcher, executor, types

SERVICE = 'email'  # тут имя вашего сервиса email, telegram или vk


TG_TOKEN = "5427293360:AAFd4qDNL9DD_Q5WSM4pqrDFqtdTQqNK1bs"
NAME = 'test_rabbit'
USERNAME = 'test_rabbit_lm_bot'

bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    await message.answer(f"ID чатта: {message.chat.id}")


async def listen_rabbit_mq(loop):
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@127.0.0.1/", loop=loop
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
                    print(f'{datetime.now()} receive message:')
                    data = loads(message.body)
                    print(type(data))
                    print(data)
                    if queue.name in message.body.decode():
                        break


if __name__ == '__main__':
    rabbit_loop = get_event_loop()
    rabbit_loop.create_task(listen_rabbit_mq(rabbit_loop))
    executor.start_polling(dp, skip_updates=True, loop=rabbit_loop)
