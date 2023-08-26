import asyncio
# import markup as nv
import sqlalchemy as sa
import os


from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from sqltable import Anime
from dotenv import load_dotenv
from keyboard import reply_markup

import tracemalloc
tracemalloc.start()

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot=bot)

db = Anime('anime.db')



@dp.message(Command("start"))
async def start(message: types.Message, bot: Bot):
    await message.answer("Бот работает!", reply_markup=reply_markup)

@dp.message(Command("add"))
async def add_anime(message: types.Message, bot: Bot):
    if (not await db.anime_exists(message.text[5:])):
        await db.add_anime(message.text[5:])
        await message.answer(f'Добавил{message.text[4:]}')
    else:
        await message.answer("Такое уже есть")


@dp.message(Command("rating"))
async def get_rating(message: types.Message):
    rating = message.text.split()[2]
    anime_id = message.text.split(maxsplit=2)[1]

    if anime_id.startswith("'") and anime_id.endswith("'"):
        anime_id = anime_id[1:-1]
    elif anime_id.startswith('"') and anime_id.endswith('"'):
        anime_id = anime_id[1:-1]

    if await db.anime_exists(anime_id):
        await db.add_rating(anime_id, int(rating))
        await message.answer(f"Добавил рейтинг {rating} для аниме с идентификатором {anime_id}")
    else:
        await message.answer("Такого аниме не существует")
        await message.answer(anime_id)
        await message.answer(rating)


@dp.message(Command("del"))
async def del_anime(message: types.Message, bot: Bot):
    await db.del_anime(message.text[5:])
    await message.answer(f"Удалил{message.text[4:]}")


async def start():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(start())



