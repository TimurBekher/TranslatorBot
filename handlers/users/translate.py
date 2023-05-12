from aiogram import types
from aiogram.dispatcher.filters.builtin import Text
from loader import dp, db, tr
from loader import bot


@dp.message_handler()
async def bot_start(message: types.Message):
    lang = db.get_lang(id=message.from_user.id)[0]
    txt = tr.translate(text=message.text, dest=lang).text
    await bot.send_message(chat_id=message.from_user.id, text=txt)
