import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import dotenv_values

env_vars = dotenv_values('.env')
bot = Bot(env_vars["TOKEN"])
dp = Dispatcher()


@dp.message()
async def cmd_start(message: types.Message):
    app = types.web_app_info.WebAppInfo(url=env_vars["WEB_APP_URL"])
    button = types.InlineKeyboardButton(text="Открыть приложение", web_app=app)
    markup = types.InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.answer("Начнем!\nДля доступа к функционалу нажмите на кнопку ниже", reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
