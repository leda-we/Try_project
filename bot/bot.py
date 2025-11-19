from aiogram import Bot, Dispatcher, executor, types
from keyboards import main_kb, info_kb, menu_kb, back_kb

API_TOKEN = "8045377064:AAGQgjsVcLQd90Bjl-Fy85PA_pCRVU_1DQ4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(
        "Привет",
        reply_markup=main_kb
        )
@dp.message_handler(text="Меню")
async def menu(message: types.Message):
    await message.answer("Вот информация:", reply_markup=info_kb)
@dp.message_handler(text="Помощь")
async def help_cmd(message: types.Message):
    await message.answer("Я простой бот")                           
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f'Ты написал: {message.text}')
@dp.message_handler()
async def open_menu(message: types.Message):
    await message.answer(
        "Выберите раздел",
        reply_markup=menu_kb
    )
@dp.callback_query_handler(text="about")
async def about_info(call: types.CallbackQuery):
    await call.message.edit_text(
        "Этот бот создан для обучения программированию",
        reply_markup=back_kb
    )
@dp.callback_query_handler(text="contacts")
async def contacts_info(call: types.CallbackQuery):
    await call.message.edit_text(
        "GitHub: \ngithub.com/leda-we",
        reply_markup=back_kb
    )
@dp.callback_query_handler(text="back_to_menu")
async def back_to_menu(call: types.CallbackQuery):
    await call.message.edit_text(
        "Выберите раздел:",
        reply_markup=menu_kb
    )
@dp.callback_query_handler(text="back_to_main")
async def back_to_main(call: types.CallbackQuery):
    await call.message.answer(
        "Главное меню",
        reply_markup=main_kb
    )
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
