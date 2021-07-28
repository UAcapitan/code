# --------------------------------------
# Development start date: 16 Jul 2021
# --------------------------------------

import urllib.request as urllib2
import telebot
from bs4 import BeautifulSoup
from telebot import types
import random

TOKEN = '1912816248:AAFfHtIKznlhFFMC-k4OfmKEZhRwI4gK2sc'

bot = telebot.TeleBot(TOKEN)

list_buttons = ['Habr News Python', 'Habr All', 'Habr Python', '/back']

projects = [
    'GUI Calculator - a calculator with a graphical interface, has both basic functions (summation, subtraction, multiplication, division) and additional functions (brackets, comma, exponentiation and further at your discretion).',
    'Weather Program - graphic program for displaying the weather in the city or any other entered settlement, which the user enters.',
    'MP3 Player - graphic program for displaying and playing music from the device, displays song titles, playback time and possibly graphic effects when playing a selected song.',
]

list_meme = []

@bot.message_handler(commands=['start'])
@bot.message_handler(commands=['back'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Habr')
    button2 = types.KeyboardButton('Random project')
    button3 = types.KeyboardButton('Meme')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text == 'Habr':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton(list_buttons[0])
        button2 = types.KeyboardButton(list_buttons[1])
        button3 = types.KeyboardButton(list_buttons[2])
        button4 = types.KeyboardButton(list_buttons[3])
        markup.add(button1)
        markup.add(button2)
        markup.add(button3)
        markup.add(button4)
        bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)
    else:
        if message.text in list_buttons:
            if message.text == list_buttons[0]:
                url = 'https://habr.com/ru/search/?q=Python&target_type=posts&order=date'
                tag = 'a'
                class_tag = 'tm-article-snippet__title-link'
                url_site = 'habr.com'
            
            elif message.text == list_buttons[1]:
                url = 'https://habr.com/ru/all/'
                tag = 'a'
                class_tag = 'tm-article-snippet__title-link'
                url_site = 'habr.com'

            elif message.text == list_buttons[2]:
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

        if message.text == 'Random project':
            bot.send_message(message.chat.id, random.choice(projects))

        if message.text == 'Meme':
            bot.send_photo(message.chat.id, 'https://inteng-storage.s3.amazonaws.com/img/iea/yrwQvLJbON/sizes/programmer-memes_md.jpg')

bot.polling(none_stop=True)

