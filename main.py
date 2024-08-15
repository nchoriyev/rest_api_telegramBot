import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6815654045:AAHUVeZcoCmZKOKQLEqoc5tlQEv1yV5lGOE'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

API_BASE_URL = 'http://127.0.0.1:8000/api/'


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    username = message.from_user.username
    await message.reply(f""" Hi @{username}
Commands:
/artist - List all artists
/albom - List all albums
/songs - List all songs
/top_songs - Show top 3 songs
/null_listen - Show songs with 0 listens
/all_listen - Increment listen count for all songs
/to_draft - Change all songs to draft status
/to_publish - Publish all songs
/top_artists - Show top 3 artists
/artists_with_no_albums - Show artists with no albums
/activate_all_artists - Activate all artists
/deactivate_all_artists - Deactivate all artists
/top_alboms - Show top 3 albums
/alboms_with_no_songs - Show albums with no songs
/release_all_alboms - Release all albums
/unrelease_all_alboms - Unrelease all albums
    """)


@dp.message_handler(commands=['songs'])
async def send_songs(message: types.Message):
    response = requests.get(f'{API_BASE_URL}song-telegram/')
    songs = response.json()
    for song in songs:
        await message.reply(f"Song: {song['title']} - {song['listen']} listens")


@dp.message_handler(commands=['artist'])
async def send_artists(message: types.Message):
    response = requests.get(f'{API_BASE_URL}artist-telegram/')
    artists = response.json()
    for artist in artists:
        await message.reply(f"Artist: {artist['nick']}")


@dp.message_handler(commands=['albom'])
async def send_alboms(message: types.Message):
    response = requests.get(f'{API_BASE_URL}albom-telegram/')
    alboms = response.json()
    for albom in alboms:
        await message.reply(f"Album: {albom['title']}")


@dp.message_handler(commands=['top_songs'])
async def send_top_songs(message: types.Message):
    response = requests.get(f'{API_BASE_URL}song-telegram/top/')
    top_songs = response.json()
    await message.reply("Top 3 Songs:")
    for song in top_songs:
        await message.reply(f"{song['title']} - {song['listen']} listens")


@dp.message_handler(commands=['null_listen'])
async def send_null_listen_songs(message: types.Message):
    response = requests.get(f'{API_BASE_URL}song-telegram/null_listen/')
    songs = response.json()
    await message.reply("Songs with 0 listens:")
    for song in songs:
        await message.reply(song['title'])


@dp.message_handler(commands=['all_listen'])
async def increment_all_listen(message: types.Message):
    response = requests.get(f'{API_BASE_URL}song-telegram/all_listen/')
    await message.reply(response.json()['message'])


@dp.message_handler(commands=['to_draft'])
async def change_all_to_draft(message: types.Message):
    response = requests.get(f'{API_BASE_URL}song-telegram/to_draft/')
    await message.reply(response.json()['message'])


@dp.message_handler(commands=['to_publish'])
async def change_all_to_publish(message: types.Message):
    response = requests.get(f'{API_BASE_URL}song-telegram/to_publish/')
    await message.reply(response.json()['message'])


@dp.message_handler(commands=['top_artists'])
async def send_top_artists(message: types.Message):
    response = requests.get(f'{API_BASE_URL}artist-telegram/top/')
    artists = response.json()
    await message.reply("Top 3 Artists:")
    for artist in artists:
        await message.reply(f"{artist['nick']} - {artist.get('popularity', 'N/A')} popularity")


@dp.message_handler(commands=['artists_with_no_albums'])
async def send_artists_with_no_albums(message: types.Message):
    response = requests.get(f'{API_BASE_URL}artist-telegram/with_no_albums/')
    artists = response.json()
    await message.reply("Artists with no albums:")
    for artist in artists:
        await message.reply(artist['nick'])


@dp.message_handler(commands=['activate_all_artists'])
async def activate_all_artists(message: types.Message):
    response = requests.get(f'{API_BASE_URL}artist-telegram/activate_all/')
    await message.reply(response.json()['message'])


@dp.message_handler(commands=['deactivate_all_artists'])
async def deactivate_all_artists(message: types.Message):
    response = requests.get(f'{API_BASE_URL}artist-telegram/deactivate_all/')
    await message.reply(response.json()['message'])


@dp.message_handler(commands=['top_alboms'])
async def send_top_alboms(message: types.Message):
    response = requests.get(f'{API_BASE_URL}albom-telegram/top/')
    alboms = response.json()
    await message.reply("Top 3 Albums:")
    for albom in alboms:
        await message.reply(f"{albom['title']} - {albom.get('popularity', 'N/A')} popularity")


@dp.message_handler(commands=['alboms_with_no_songs'])
async def send_alboms_with_no_songs(message: types.Message):
    response = requests.get(f'{API_BASE_URL}albom-telegram/with_no_songs/')
    alboms = response.json()
    await message.reply("Albums with no songs:")
    for albom in alboms:
        await message.reply(albom['title'])


@dp.message_handler(commands=['release_all_alboms'])
async def release_all_alboms(message: types.Message):
    response = requests.get(f'{API_BASE_URL}albom-telegram/release_all/')
    await message.reply(response.json()['message'])


@dp.message_handler(commands=['unrelease_all_alboms'])
async def unrelease_all_alboms(message: types.Message):
    response = requests.get(f'{API_BASE_URL}albom-telegram/unrelease_all/')
    await message.reply(response.json()['message'])


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


# Run the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
