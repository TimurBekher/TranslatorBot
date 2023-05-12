from aiogram import types
from loader import dp, db, tr
from loader import bot
from aiogram.dispatcher.filters.builtin import Command
from keyboards.inline.langs import langs_keyboard


@dp.message_handler(Command("lang"))
async def lang_menu(message: types.Message):
    await bot.send_message(message.chat.id, "Выбери язык:", reply_markup=langs_keyboard)


@dp.callback_query_handler(lambda call: call.data.split(':')[-1] in ['en', 'de', 'zh-tw', 'fr'])
async def set_lang(call: types.CallbackQuery):
    lang_code = call.data.split(':')[-1]
    print(lang_code)
    db.set_lang(id=call.from_user.id, lang_code=lang_code)



