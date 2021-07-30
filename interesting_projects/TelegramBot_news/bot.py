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
    'Design a Small JavaScript Game - Designing a small JavaScript game is a good test for any new developer — this is your chance to showcase what you can do with your skill set.',
    'Create a Simple Application - Creating an application is a great way to practice your coding skills. It can be hard to come up with new application ideas, but your first application doesn’t have to be complicated — it can be something as simple as a calculator or to-do list.',
    'Random Number Generator - Coding a random number generator with Python is another great programming project idea. The goal of the application is to randomly generate a number at the user’s request. This project will test a new developer’s ability to use variants, integers, random function, input/output and other concepts.',
    'Build You Own Online Store - Creating an e-commerce store is another great way to practice your coding skills. The elements required for an online store are slightly more complex than a social networking site, since this project will need more than just a user database to function. Here, you will need to design a script to allow for a product page, shopping cart, checkout and other e-commerce-related elements.'
]

list_meme = [
    'https://inteng-storage.s3.amazonaws.com/img/iea/yrwQvLJbON/sizes/programmer-memes_md.jpg',
    'https://i.pinimg.com/originals/f0/57/45/f05745097ea6273709bfe2e727989488.jpg',
    'https://i.pinimg.com/originals/4f/82/8d/4f828d05f82b8b7aedfe8be6a7d9d2a3.png',
    'https://www.testbytes.net/wp-content/uploads/2019/06/Untitled-63.png',
    'https://preview.redd.it/9u4tx0d53es11.png?auto=webp&s=dd88bf3841d5eb4885eed2d3caecc9a5da635cd5',
    'https://pbs.twimg.com/media/EXUgmSsXQAAlWg7.jpg',
    'https://miro.medium.com/max/1400/0*z1mm6izqSeDiKukb',
    'https://i.pinimg.com/originals/0e/d6/23/0ed623806cf3b9d805a8cb1e4c822daf.png',
    'https://res.cloudinary.com/practicaldev/image/fetch/s--ay343eZU--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://pics.me.me/200-line-if-else-statement-everything-in-main-undocumented-code-if-25999016.png',
    'https://i.chzbgr.com/full/9602643200/h2CFDEF7C/asked-draw-flowchart-my-code-tdev_meme-y-start-magic-end',
    'https://www.thecoderpedia.com/wp-content/uploads/2020/06/Programming-Memes-Google-Chrome-822x1024.jpg?x78691',
    'https://i.chzbgr.com/full/6349573/hB0DE8033/funny-programming-memes'
]

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
            bot.send_photo(message.chat.id, random.choice(list_meme))

bot.polling(none_stop=True)

