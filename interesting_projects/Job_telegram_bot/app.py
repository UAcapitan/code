from unittest import result
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
    button2 = types.KeyboardButton('DOU')
    button3 = types.KeyboardButton('Jooble')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)

def get_page(url, headers=''):
    if headers == '':
        return requests.get(url).text
    else:
        return requests.get(url, headers=headers).text

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
        ])

        if vacancies[-1][-1] == vacancies[-1][-2]:
            vacancies[-1].pop()

    return "\n\n".join(["\n".join(i) for i in vacancies])

def parse_dou(url, n=0):
    headers = {"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"}

    soup = BeautifulSoup(get_page(url, headers), "html.parser")
    results = soup.find_all("div", class_="vacancy")

    if not results:
        return 'No vacancies'

    vacancies = []

    if n > 0:
        results = results[:n]

    for i in results:
        vacancies.append([
            i.find("div", class_="title").find("a").text.replace("\xa0", " "),
            i.find("div", class_="title").find("a")["href"],
            i.find("div", class_="title").find("strong").find("a").text.encode("ascii", "ignore").decode(),
            i.find("div", class_="title").find("span").text
        ])

    return "\n\n".join(["\n".join(i) for i in vacancies])

def parse_jooble(url, n=0):
    soup = BeautifulSoup(get_page(url), "html.parser")
    results = soup.find_all("article", {"data-test-name": "_jobCard"})

    if not results:
        return 'No vacancies'

    vacancies = []

    if n > 0:
        results = results[:n]

    for i in results:
        vacancies.append([
            i.find("header").find("div").find("h2").find("a").text,

            i.find("header").find("div").find("h2").find("a")["href"],

            i.find("section").find("div", class_="_15xYk4")
            .find("div").find("div").find("div").find("p").text,

            i.find("section").find("div", class_="_15xYk4")
            .find("div").find_all("div")[2].find("div").text
        ])

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

def dou(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('DOU Junior Python')
    button2 = types.KeyboardButton('DOU Trainee Python')
    button3 = types.KeyboardButton('/back')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)

def jooble(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Jooble Junior Python')
    button2 = types.KeyboardButton('Jooble Trainee Python')
    button3 = types.KeyboardButton('/back')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Keyboard', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text == 'Djinni':
        djinni(message)
    elif message.text == 'DOU':
        dou(message)
    elif message.text == 'Jooble':
        jooble(message)
    elif message.text == 'Djinni Junior Python':
        bot.send_message(message.chat.id, parse_djinni("https://djinni.co/jobs/?keywords=Junior+Python", 10))
    elif message.text == 'Djinni Trainee Python':
        bot.send_message(message.chat.id, parse_djinni("https://djinni.co/jobs/?keywords=Trainee+Python"))
    elif message.text == 'DOU Junior Python':
        bot.send_message(message.chat.id, parse_dou("https://jobs.dou.ua/vacancies/?search=junior+python")),
    elif message.text == 'DOU Trainee Python':
        bot.send_message(message.chat.id, parse_dou("https://jobs.dou.ua/vacancies/?search=trainee+python"))
    elif message.text == 'Jooble Junior Python':
        bot.send_message(message.chat.id, parse_jooble("https://ua.jooble.org/SearchResult?p=2&rgns=%D0%9A%D0%B8%D1%97%D0%B2&ukw=junior%20python", 10)),
    elif message.text == 'Jooble Trainee Python':
        bot.send_message(message.chat.id, parse_jooble("https://ua.jooble.org/SearchResult?p=2&rgns=%D0%9A%D0%B8%D1%97%D0%B2&ukw=trainee%20python", 10))

bot.polling(none_stop=True)