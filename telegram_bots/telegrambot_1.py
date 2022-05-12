from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import logging
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode


TOKEN = config("CODE")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(f"Приветствую мой дорогой {message.from_user.full_name}")




@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    murcup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton('Next' , callback_data="button_1")
    murcup.add(button_1)
    ask = "Перевод слова Sunrise"
    answer = ['камень', 'солнце', 'цветы', 'рассвет']
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=ask,
        options=answer,
        is_anonymous=False,
        type='quiz' ,
        correct_option_id=3,
        explanation='это же легко',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=murcup
    )

@dp.callback_query_handler(lambda  call: call.data == "button_1" )
async def quiz_2 (call: types.CallbackQuery):

    murcup = InlineKeyboardMarkup()
    button_2 = InlineKeyboardButton('Next' , callback_data="button_2")
    murcup.add(button_2)


    ask = "кипяток горячий ?"
    answer = [
        'Да',
        'Определенно ',
        'Ещё как',
        'Определенно'
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ask,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='если что это первый вариант',
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=murcup
    )
@dp.message_handler(commands=['mem'])
async def quiz_1(message: types.Message):
    photo = open("photos/pic_1e848ca661ae53311bb74529ea0470ff.png" , "rb")
    await bot.send_photo(message.from_user.id, photo=photo)



@dp.message_handler()
async def echo(message: types.Message):
    x = message.text
    try:
        x = int(x)
        c = 1
    except:
        pass
        c = 0
    # if message == int:
    #     await bot.send_message(message.from_user.id, "its int")
    # else:
    if c == 1:
        await bot.send_message(message.from_user.id, f"{x**x}")
    elif c == 0:
        await bot.send_message(message.from_user.id,x)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
