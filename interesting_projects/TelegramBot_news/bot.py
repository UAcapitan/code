# --------------------------------------
# Development start date: 16 Jul 2021
# --------------------------------------

import urllib.request as urllib2
import telebot
from bs4 import BeautifulSoup
from telebot import types

TOKEN = '1912816248:AAFfHtIKznlhFFMC-k4OfmKEZhRwI4gK2sc'

bot = telebot.TeleBot(TOKEN)

list_buttons = ['News', 'News Python', 'News Habr']

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text == 'Buttons':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('News')
        button2 = types.KeyboardButton('News Habr')
        button3 = types.KeyboardButton('News Python')
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)
    else:
        if message.text in list_buttons:
            if message.text == 'News':
                url = 'https://habr.com/ru/search/?q=Python&target_type=posts&order=date'
                tag = 'a'
                class_tag = 'tm-article-snippet__title-link'
                url_site = 'habr.com'
            
            elif message.text == 'News Habr':
                url = 'https://habr.com/ru/all/'
                tag = 'a'
                class_tag = 'tm-article-snippet__title-link'
                url_site = 'habr.com'

            elif message.text == 'News Python':
                url = 'https://habr.com/ru/hub/python/'
                tag = 'a'
                class_tag = 'tm-article-snippet__title-link'
                url_site = 'habr.com'

            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
            article_box = (soup.find_all(tag, attrs={'class': class_tag}))[:3]
            for i in article_box:
                article = i.text.strip() + '\n\n' + url_site + i['href']
                bot.send_message(message.chat.id, article)

bot.polling(none_stop=True)

