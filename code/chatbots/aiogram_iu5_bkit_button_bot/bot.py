import os
from aiogram import Bot, Dispatcher, executor, types

# Имя бота для поиска в Telegram: aiogram_iu5_bkit_button_bot

# Токент бота
TOKEN = '5067067017:AAGkOlumV1L6ZR4OvaLmopcnJThIMvXfOHs'

# Сообщения
mes_emblem = 'вывести герб'
mes_photo = 'вывести фото'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)

@dp.message_handler()
async def answer_all(message: types.Message):

	# Текст, введенный пользователем, то есть текст с кнопки
	text = message.text
	
	# Проверка сообщения и вывод данных
	if text==mes_emblem:
		img = open(os.path.join(cur_path, 'img', 'emblem.jpg'), 'rb')
		await bot.send_photo(message.from_user.id, img)
	elif text==mes_photo:
		img = open(os.path.join(cur_path, 'img', 'photo.jpg'), 'rb')
		await bot.send_photo(message.from_user.id, img)
	else:
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		buttons = [mes_emblem, mes_photo]
		keyboard.add(*buttons)
		await message.answer('Пожалуйста, нажмите кнопку', reply_markup=keyboard)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
