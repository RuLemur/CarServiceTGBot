from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

from requester.user import add_user


def get_token():
    f = open("token.txt", "r")
    return f.read()


bot = Bot(token=get_token())
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    start_btn = types.KeyboardButton(text="Начать пользоваться!")
    keyboard.add(start_btn)
    await msg.answer("привет", reply_markup=keyboard)


@dp.message_handler(Text(equals="Начать пользоваться!"))
async def send_welcome(msg: types.Message):
    user_id = add_user(msg.from_user.username)
    await msg.answer(f'Вы заргестрированны с id = {user_id}')


if __name__ == '__main__':
    executor.start_polling(dp)
