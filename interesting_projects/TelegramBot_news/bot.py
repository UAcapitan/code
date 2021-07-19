# --------------------------------------
# Development start date: 16 Jul 2021
# --------------------------------------

import urllib.request as urllib2
import telebot
from bs4 import BeautifulSoup
from telebot import types

TOKEN = '1912816248:AAFfHtIKznlhFFMC-k4OfmKEZhRwI4gK2sc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text == 'Buttons':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('News Python')
        markup.add(button1)
        bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)

    if message.text == 'News Python':
        url = 'https://habr.com/ru/search/?q=Python&target_type=posts&order=date'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        article_box = (soup.find_all('a', attrs={'class': 'tm-article-snippet__title-link'}))[:3]
        for i in article_box:
            article = i.text.strip() + '\n\n' + 'habr.com' + i['href']
            bot.send_message(message.chat.id, article)

bot.polling(none_stop=True)

