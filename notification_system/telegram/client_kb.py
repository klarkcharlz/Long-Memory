from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

btn = KeyboardButton('/start')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(btn)
