import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types

TOKEN = '5572890027:AAHql6X6xfFayP7aOIjE-2KtGmERBGrI__k'

bot = telebot.TeleBot(TOKEN)

buttons = {
    'Djinni': ['Djinni Junior Python', 'Djinni Trainee Python'],
    'DOU': ['DOU Junior Python', 'DOU Trainee Python'],
    'Jooble': ['Jooble Junior Python', 'Jooble Trainee Python']
}

urls = {
    "Djinni Junior Python": "https://djinni.co/jobs/?keywords=Junior+Python",
    "Djinni Trainee Python": "https://djinni.co/jobs/?keywords=Trainee+Python",
    "DOU Junior Python": "https://jobs.dou.ua/vacancies/?search=junior+python",
    "DOU Trainee Python": "https://jobs.dou.ua/vacancies/?search=trainee+python",
    "Jooble Junior Python": "https://ua.jooble.org/SearchResult?p=2&rgns=%D0%9A%D0%B8%D1%97%D0%B2&ukw=junior%20python",
    "Jooble Trainee Python": "https://ua.jooble.org/SearchResult?p=2&rgns=%D0%9A%D0%B8%D1%97%D0%B2&ukw=trainee%20python"
}

@bot.message_handler(commands=['start', 'back'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Djinni')
    button2 = types.KeyboardButton('DOU')
    button3 = types.KeyboardButton('Jooble')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    bot.send_message(message.chat.id, 'Main keyboard', reply_markup=markup)

def get_page(url, headers):
    return requests.get(url, headers=headers).text

def get_buttons(message, site, buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    list_ = []
    for i in buttons:
        list_.append(types.KeyboardButton(i))

    list_.append('/back')

    for i in list_:
        markup.add(i)

    bot.send_message(message.chat.id, f"{site} buttons", reply_markup=markup)

def parse(message, site, url):
    headers = {"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"}
    soup = BeautifulSoup(get_page(url, headers), "html.parser")

    match site:
        case 'Djinni':
            list_ = parse_djinni(soup)
        case 'DOU':
            list_ = parse_dou(soup)
        case 'Jooble':
            list_ = parse_jooble(soup)

    if not list_:
        bot.send_message(message.chat.id, 'No vacancies')
    else:
        text = "\n\n".join(["\n".join(i) for i in list_])
        bot.send_message(message.chat.id, text)

def parse_djinni(soup):
    vacancies = []
    results = soup.find_all("li", class_="list-jobs__item")

    for i in results[:10]:
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

    return vacancies

def parse_dou(soup):
    vacancies = []
    results = soup.find_all("div", class_="vacancy")

    for i in results[:10]:
        vacancies.append([
            i.find("div", class_="title").find("a").text.replace("\xa0", " "),
            i.find("div", class_="title").find("a")["href"],
            i.find("div", class_="title").find("strong").find("a").text.encode("ascii", "ignore").decode(),
            i.find("div", class_="title").find("span").text
        ])

    return vacancies

def parse_jooble(soup):
    vacancies = []
    results = soup.find_all("article", {"data-test-name": "_jobCard"})

    for i in results[:10]:
        vacancies.append([
            i.find("header").find("div").find("h2").find("a").text,

            i.find("header").find("div").find("h2").find("a")["href"],

            # i.find("section").find("div", class_="_15xYk4")
            # .find("div").find("div").find("div").find("p").text,

            # i.find("section").find("div", class_="_15xYk4")
            # .find("div").find_all("div")[2].find("div").text
        ])

    return vacancies

@bot.message_handler(content_types=['text'])
def main(message):
    if message.text in buttons:
        get_buttons(message, message.text, buttons[message.text])

    if message.text in urls:
        parse(message, message.text.split()[0], urls[message.text])

bot.polling(none_stop=True)