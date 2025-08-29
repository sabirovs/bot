import os
from aiogram import Bot, Dispatcher, executor, types

# Tokenni Render Environment Variables ichida qo'yasiz
BOT_TOKEN = os.environ.get("7096771583:AAHvJK0CTU4wXvGlw2zw3S_cv9Dp2H-oVB0")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# /start komandasi
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    # Oddiy tugmalar
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["👋 Salom", "❓ Qalaysan"]
    keyboard.add(*buttons)
    await message.answer("Salom! Tugmalardan birini tanlang 👇", reply_markup=keyboard)

# Tugmalarni qayta ishlash
@dp.message_handler(lambda message: message.text in ["👋 Salom", "❓ Qalaysan"])
async def reply_buttons(message: types.Message):
    if message.text == "👋 Salom":
        await message.answer("Va alaykum assalom! 😊")
    elif message.text == "❓ Qalaysan":
        await message.answer("Zo‘rman, rahmat! Sizchi?")

if __name__ == "__main__":
    executor.start_polling(dp)
