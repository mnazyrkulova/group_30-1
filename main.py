from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)

# print(TOKEN)
# @dp.message_handler()
# async def echo(message: types.Message) -> None:
#    await bot.send_message(message.chat.id, message.text)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
   await bot.send_message(message.chat.id, f'Привет {message.from_user.full_name}')
   # await message.answer('This is an answer method')
   # await message.reply('This is a reply method')


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
   markup = InlineKeyboardMarkup()
   next_button = InlineKeyboardButton('NEXT', callback_data='next_button1')
   markup.add(next_button)

   question = 'Какая единственная страна граничит с Великобританией?'
   answers = [
      'Швеция',
      'Германия',
      'Австрия',
      'Ирландия',
   ]
   # await bot.send_poll()
   await message.answer_poll(
      question=question,
      options=answers,
      is_anonymous=False,
      type='quiz',
      correct_option_id=3,
      explanation='Не верный ответ',
      open_period=15,
      reply_markup=markup,
   )

@dp.callback_query_handler(text='next_button1')
async def quiz_2(callback: types.CallbackQuery):
   # await bot.send_message(callback.from_user.id, f'You pressed the button')
   question = 'Какая служба электронной почты принадлежит компании Microsoft??'
   answers = [
      'Outlook',
      'Yahoo Mail',
      'Gmail',
      'iCloud Mail',
   ]
   # await bot.send_poll()
   await callback.message.answer_poll(
      question=question,
      options=answers,
      is_anonymous=False,
      type='quiz',
      correct_option_id=0,
      explanation='Не верный ответ',
      open_period=15,
   )

@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message) -> None:
   await message.answer_photo(
      photo='https://ih1.redbubble.net/image.2595320116.9420/flat,750x,075,f-pad,750x1000,f8f8f8.jpg'
   )
   photo = open('media/mike.jpeg', 'rb')
   await bot.send_photo(
      chat_id=message.from_user.id,
      photo=photo
   )

@dp.message_handler()
async def echo_text(message: types.Message) -> None:
   if message.text.isnumeric():
      await message.answer(int(message.text) ** 2)
   else:
      await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO)
   executor.start_polling(dp, skip_updates=True)
