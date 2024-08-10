"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6815654045:AAHUVeZcoCmZKOKQLEqoc5tlQEv1yV5lGOE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f""" Hi @{username}
    Commands
      1. /artist
      2. /albom
      3. /songs """)


@dp.message_handler(commands=['songs'])
async def send_songs(message: types.Message):
    songs = requests.get(f'http://127.0.0.1:8000/api/song-telegram/')
    for song in songs.json():
        await message.reply(song)

@dp.message_handler(commands=['artist'])
async def send_songs(message: types.Message):
    artists = requests.get(f'http://127.0.0.1:8000/api/artists-telegram/')
    for artist in artists.json():
        await message.reply(artist)


@dp.message_handler(commands=['albom'])
async def send_songs(message: types.Message):
    alboms = requests.get(f'http://127.0.0.1:8000/api/albom-telegram/')
    for albom in alboms.json():
        await message.reply(albom)


# @dp.message_handler()
# async def search_music(message: types.Message):
#     search_data = message.text
#     music = requests.get(f'http://127.0.0.1:8000/music/?search={search_data}')
#     for mus in music.json():
#         await message.reply(f"""
#
#         Name: {mus['name']}
#         Albom:
#             Title: {mus['albom']}
#
# """)


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)