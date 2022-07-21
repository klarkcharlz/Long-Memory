import logging

from aiogram import Bot, executor, Dispatcher, types
from tgbot_db import Database


logging.basicConfig(level=logging.INFO)

bot = Bot(token="5490911968:AAFLjoW47LS68g8HF7xNLHhSFLDx-jUP16Q")
dp = Dispatcher(bot)
db = Database('database.db')


#Команда старт:
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == "private":
        # Если пользователя нет в базе:
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Добро пожаловать!")


#Команда "отправить всем":
@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':

        #############################
        if message.from_user.id == 833000525:
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)