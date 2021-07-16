import telebot
from bs4 import BeautifulSoup

TOKEN = '1912816248:AAFfHtIKznlhFFMC-k4OfmKEZhRwI4gK2sc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)

