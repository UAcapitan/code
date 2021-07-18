# --------------------------------------
# Development start date: 16 Jul 2021
# --------------------------------------

import urllib.request as urllib2
import telebot
from bs4 import BeautifulSoup

TOKEN = '1912816248:AAFfHtIKznlhFFMC-k4OfmKEZhRwI4gK2sc'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def send_text(message):
    url = 'https://habr.com/ru/search/?q=Python&target_type=posts&order=date'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    article_box = soup.find('a', attrs={'class': 'tm-article-snippet__title-link'})
    article = article_box.text.strip()
    bot.send_message(message.chat.id, article)

bot.polling(none_stop=True)

