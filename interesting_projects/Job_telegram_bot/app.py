
import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
import keys


TOKEN = keys.TOKEN

bot = telebot.TeleBot(TOKEN)

buttons = {
    'Djinni': ['Djinni Junior Python', 'Djinni Trainee Python'],
    'DOU': ['DOU Junior Python', 'DOU Trainee Python'],
    'Work': ['Work Junior Python', 'Work Trainee Python'],
}

urls = {
    "Djinni Python": "https://djinni.co/jobs/?keywords=Python",
    "Djinni Junior Python": "https://djinni.co/jobs/?keywords=Junior+Python",
    "Djinni Trainee Python": "https://djinni.co/jobs/?keywords=Trainee+Python",
    "DOU Junior Python": "https://jobs.dou.ua/vacancies/?search=junior+python",
    "DOU Trainee Python": "https://jobs.dou.ua/vacancies/?search=trainee+python",
    "Work Junior Python": "https://www.work.ua/jobs-kyiv-junior+python/",
    "Work Trainee Python": "https://www.work.ua/jobs-kyiv-trainee+python/",
}


@bot.message_handler(commands=['start', 'back'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    for i in buttons:
        markup.add(types.KeyboardButton(i))

    bot.send_message(message.chat.id, 'Main keyboard', reply_markup=markup)


def get_page(url, headers):
    return requests.get(url, headers=headers).text


def get_buttons(message, site, buttons):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for i in buttons:
        markup.add(types.KeyboardButton(i))

    markup.add(types.KeyboardButton("/back"))

    bot.send_message(message.chat.id, f"{site} buttons", reply_markup=markup)


def parse(message, site, url, many=False):
    headers = {"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"}
    soup = BeautifulSoup(get_page(url, headers), "html.parser")

    match site:
        case 'Djinni':
            list_ = parse_djinni(soup)
        case 'DOU':
            list_ = parse_dou(soup)
        case 'Work':
            list_ = parce_work(soup)

        case 'Popular':
            list_ = []

            for url in [
                "Djinni Junior Python",
                "Djinni Trainee Python",
                "DOU Junior Python",
                "DOU Trainee Python",
                "GRC Junior Python",
                "GRC Trainee Python",
                "Jobs Junior Python"
            ]:
                list_.append(parse(message, url.split()[0], urls[url]))
            print(list_)
    
    if not many:
        if not list_:
            bot.send_message(message.chat.id, 'No vacancies')
        else:
            text = "\n\n".join(["\n".join(i) for i in list_])
            bot.send_message(message.chat.id, text)


# Parsers
def parse_djinni(soup, n=10):
    vacancies = []
    results = soup.find_all("li", class_="list-jobs__item")

    for i in results[:n]:
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


def parse_dou(soup, n=10):
    vacancies = []
    results = soup.find_all("div", class_="vacancy")

    for i in results[:n]:
        vacancies.append([
            i.find("div", class_="title").find("a").text.replace("\xa0", " "),
            i.find("div", class_="title").find("a")["href"],
            i.find("div", class_="title").find("strong").find("a").text.encode("ascii", "ignore").decode(),
            i.find("div", class_="title").find("span").text
        ])

    return vacancies


def parce_work(soup, n=10):
    vacancies = []
    results = soup.find_all("div", {"class": "job-link"})

    for i in results[:n]:
        vacancies.append([
            i.find("h2").text.strip(),
            "https://www.work.ua" + i.find("h2").find("a")["href"],
            i.find("div", {"class": "add-top-xs"}).find_all("span")[0].text,
            i.find("div", {"class": "add-top-xs"}).find_all("span")[-1].text
        ])

    return vacancies


# Main bot's function
@bot.message_handler(content_types=['text'])
def main(message):
    if message.text in buttons:
        get_buttons(message, message.text, buttons[message.text])

    if message.text in urls:
        parse(message, message.text.split()[0], urls[message.text])

    if message.text == 'From popular sites':
        parse(message, 'Popular', urls, many=True)


bot.polling(none_stop=True)