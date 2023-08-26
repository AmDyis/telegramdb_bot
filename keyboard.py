from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Создаем список кнопок клавиатуры
keyboard = [
    [KeyboardButton(text="Добавить Аниме"), KeyboardButton(text="Выбрать Аниме")],
    [KeyboardButton(text="Поставить Рейтинг"), KeyboardButton(text="Удалить Аниме")]
]

# Создаем объект ReplyKeyboardMarkup с указанием списка кнопок
reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)