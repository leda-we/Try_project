from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(
    KeyboardButton("Меню"),
    KeyboardButton("Помощь")
)

info_kb = InlineKeyboardMarkup()
info_kb.add(
    InlineKeyboardButton("Мой GitHub", url="https://github.com"),

)
info_kb.add(
    InlineKeyboardButton("Написать автору", url="https://t.me/username")

)

menu_kb = InlineKeyboardMarkup()
menu_kb.add(
    InlineKeyboardButton("О боте", callback_data="about"),
    InlineKeyboardButton("Контакты", callback_data="contacts")
)
menu_kb.add(
    InlineKeyboardButton("Назад", callback_data="back_to_main")
)
back_kb = InlineKeyboardMarkup().add(
    InlineKeyboardButton("Назад", callback_data="back_to_main")
)

