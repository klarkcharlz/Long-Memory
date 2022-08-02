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


config = dotenv_values(".env")

TG_TOKEN = config['TOKEN']


bot = Bot(token=TG_TOKEN)
dp = Dispatcher(bot)


async def send_message(chat_id, message):
    await bot.send_message(chat_id, message)


@dp.message_handler(commands=['start'])
async def alarm(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет', reply_markup=kb.greet_kb)
    await message.answer(f"ID чата: {message.chat.id}")


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
                    for dic in data:
                        if len(dic["notifications"]) > 1:
                            for i in range(len(dic["notifications"])):
                                await send_message(dic['id'], f'{currentTime}, {dic["name"]}. '
                                                     f'\nВам нужно повторить сегодня: {dic["notifications"][i]["title"]},'
                                                     f'\nа именно: {dic["notifications"][i]["description"]}')

                    if queue.name in message.body.decode():
                        break


if __name__ == '__main__':
    rabbit_loop = get_event_loop()
    rabbit_loop.create_task(listen_rabbit_mq(rabbit_loop))
    executor.start_polling(dp, skip_updates=True, loop=rabbit_loop)
