from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import lang_callback
langs_keyboard = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text = "🇬🇧Английский",
                                                                   callback_data=lang_callback.new(code="en") ),
                                              InlineKeyboardButton(text = "🇩🇪Немецкий",
                                                                   callback_data=lang_callback.new(code="de") )
                                          ],
[
                                              InlineKeyboardButton(text = "🇨🇳Китайский",
                                                                   callback_data=lang_callback.new(code="zh-tw") ),
                                              InlineKeyboardButton(text = "🇫🇷Французский",
                                                                   callback_data=lang_callback.new(code="fr") )
                                          ]
                                      ])