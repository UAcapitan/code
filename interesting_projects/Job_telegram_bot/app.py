import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types

TOKEN = '5572890027:AAHql6X6xfFayP7aOIjE-2KtGmERBGrI__k'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'back'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Djinni')
    button2 = types.KeyboardButton('')
    button3 = types.KeyboardButton('')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)

def get_page(url):
    return requests.get(url).text

def parse_djinni(url, n=0):
    soup = BeautifulSoup(get_page(url), "html.parser")
    results = soup.find_all("li", class_="list-jobs__item")
    
    vacancies = []

    if n > 0:
        results = results[:n]

    for i in results:
        vacancies.append([
            i.find("div", class_="list-jobs__title")
            .find("a", class_="profile").find("span").text,

            "https://djinni.co" + i.find("div", class_="list-jobs__title")
            .find("a", class_="profile")["href"],

            i.find("div", class_="list-jobs__details")
            .find("div", class_="list-jobs__details__info").find_all("a")[1].text.strip(),

            " ".join(i.find("div", class_="list-jobs__details")
            .find("div", class_="list-jobs__details__info").find("span", "location-text").text.strip().split()),

            i.find("div", class_="list-jobs__details")
            .find("div", class_="list-jobs__details__info")
            .find_all("nobr")[0].text.strip(),

            i.find("div", class_="list-jobs__details")
            .find("div", class_="list-jobs__details__info")
            .find_all("nobr")[1].text.replace("·", "").strip(),

            i.find("div", class_="list-jobs__details")
            .find("div", class_="list-jobs__details__info").find_all("nobr")[-1].text.replace("·", "").strip(),
        ])

        if vacancies[-1][-1] == vacancies[-1][-2]:
            vacancies[-1].pop()

    return "\n\n".join(["\n".join(i) for i in vacancies])

def djinni(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Djinni Junior Python')
    button2 = types.KeyboardButton('Djinni Trainee Python')
    button3 = types.KeyboardButton('/back')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Djinni':
        djinni(message)
    elif message.text == 'Djinni Junior Python':
        bot.send_message(message.chat.id, parse_djinni("https://djinni.co/jobs/?keywords=Junior+Python", 10))
    elif message.text == 'Djinni Trainee Python':
        bot.send_message(message.chat.id, parse_djinni("https://djinni.co/jobs/?keywords=Trainee+Python"))
    
bot.polling(none_stop=True)