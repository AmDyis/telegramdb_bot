#@aiogram 2 -> рабочий

import os


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from keyboard import reply_markup
from app import sqltable as st

storage = MemoryStorage()
state = storage.get_state()
load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=storage)
class AddAnime(StatesGroup):
    anime = State()
    rating = State()
    review = State()

@dp.message_handler(commands=["start"])
async def get_start(message: types.Message):
    await message.reply("Бот работает!", reply_markup=reply_markup)

@dp.message_handler(text="Добавить Аниме")
async def add_anime(message: types.Message):
    await AddAnime.anime.set()
    await message.answer("Введите название аниме")

@dp.message_handler(state=AddAnime.anime)
async def callback_anime(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["anime_id"] = message.text
    await message.answer("Напишите рейтинг")
    await AddAnime.next()

@dp.message_handler(state=AddAnime.rating)
async def callback_rating(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["rating"] = float(message.text)
    await message.answer("Напишите отзыв")
    await AddAnime.next()

@dp.message_handler(state=AddAnime.review)
async def callback_review(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["review"] = message.text
    await st.add_anime(state)
    await message.answer("Аниме добавлено", reply_markup=reply_markup)
    await state.finish()


@dp.message_handler(commands=["Выбрать Аниме"])
async def get_start(message: types.Message):
    await message.reply("Бот работает!", reply_markup=reply_markup)

@dp.message_handler(commands=["Поставить Рейтинг"])
async def get_start(message: types.Message):
    await message.reply("Бот работает!", reply_markup=reply_markup)

@dp.message_handler(commands=["Удалить Аниме"])
async def get_start(message: types.Message):
    await message.reply("Бот работает!", reply_markup=reply_markup)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
