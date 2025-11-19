from aiogram import Bot, Dispatcher, executor, types
from keyboards import main_kb, info_kb, menu_kb, back_kb
from states import Form
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()


API_TOKEN = "8045377064:AAGQgjsVcLQd90Bjl-Fy85PA_pCRVU_1DQ4"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(
        "Привет",
        reply_markup=main_kb
        )
@dp.message_handler(text="Меню")
async def open_menu(message: types.Message):
    await message.answer(
        "Выберите раздел:",
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
@dp.message_handler(commands="form")
async def start_form(message: types.Message):
    await Form.name.set()
    await message.answer("Как тебя зовут?")
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await Form.next()
    await message.answer("Сколько тебе лет?")
@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await Form.next()
    await message.answer("Из какого ты города?")
@dp.message_handler(state=Form.city)
async def process_city(message: types.Message, state: FSMContext):
    await state.update_data(city=message.text)
    data = await state.get_data()

    await message.answer(
        f"Анкета заполнена!\n\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Город: {data['city']}"
    )
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
