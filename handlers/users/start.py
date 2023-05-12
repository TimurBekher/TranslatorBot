from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    txt = f"Привет, {message.from_user.full_name}!" \
          f"Выбери язык, на который хочешь переводить текст(по-умолчанию я перевожу на английский)" \
          f"Нажми /lang"

    try:
        db.add_user(id= message.from_user.id, lang_code='en' )
    except sqlite3.IntegrityError as err:
        print(err)

    await message.answer(txt)
