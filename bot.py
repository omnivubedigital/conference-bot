from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os

TELEGRAM_TOKEN = os.getenv("7491294784:AAEKWT5oyEKN44ZpqpZrsMHpRJjKnU2F-UM")
ADMIN_ID = os.getenv("970275191")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    KeyboardButton("Купить билет"),
    KeyboardButton("Купить билет с промокодом")
)
keyboard.add(
    KeyboardButton("Задать вопрос"),
    KeyboardButton("Узнать про конференцию")
)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer("Привет! Я ваш ассистент, чтобы попасть на конференцию.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Купить билет")
async def buy_ticket(message: types.Message):
    await bot.send_message(ADMIN_ID, f"Пользователь {message.from_user.full_name} хочет купить билет.")
    await message.answer("Запрос отправлен менеджеру. Ожидайте ссылку на оплату.")

# Другие кнопки можно настроить аналогично

if __name__ == "__main__":
    executor.start_polling(dp)
