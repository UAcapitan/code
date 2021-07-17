# --------------------------------------
# Development start date: 16 Jul 2021
# --------------------------------------

import requests
import telebot
from bs4 import BeautifulSoup

TOKEN = '1912816248:AAFfHtIKznlhFFMC-k4OfmKEZhRwI4gK2sc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_text(message):
    url = 'https://habr.com/ru/search/?q=Python&target_type=posts&order=date'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)

