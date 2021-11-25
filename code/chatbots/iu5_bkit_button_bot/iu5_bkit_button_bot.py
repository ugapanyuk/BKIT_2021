import os
import telebot
from telebot import types

# Токент бота
TOKEN = '2132353302:AAHmC1OdZXBJlj1jKeiy-AKQPKVzgquIxFI'

# Сообщения
mes_emblem = 'вывести герб'
mes_photo = 'вывести фото'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Создание бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	# Идентификатор диалога
	chat_id = message.chat.id

	# Текст, введенный пользователем, то есть текст с кнопки
	text = message.text
	
	# Проверка сообщения и вывод данных
	if text==mes_emblem:
		img = open(os.path.join(cur_path, 'img\emblem.jpg'), 'rb')
		bot.send_photo(chat_id, img)
	elif text==mes_photo:
		img = open(os.path.join(cur_path, 'img\photo.jpg'), 'rb')
		bot.send_photo(chat_id, img)
	else:
		markup = types.ReplyKeyboardMarkup(row_width=2)
		itembtn1 = types.KeyboardButton(mes_emblem)
		itembtn2 = types.KeyboardButton(mes_photo)
		markup.add(itembtn1, itembtn2)
		bot.send_message(chat_id, 'Пожалуйста, нажмите кнопку', reply_markup=markup)

bot.infinity_polling()


