
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
    'LinkedIn': ['LinkedIn Junior Python', 'LinkedIn Trainee Python'],
    'Jooble': ['Jooble Junior Python', 'Jooble Trainee Python'],
    'GRC': ['GRC Junior Python', 'GRC Trainee Python'],
    'Work': ['Work Junior Python', 'Work Trainee Python']
}

urls = {
    "Djinni Junior Python": "https://djinni.co/jobs/?keywords=Junior+Python",
    "Djinni Trainee Python": "https://djinni.co/jobs/?keywords=Trainee+Python",
    "DOU Junior Python": "https://jobs.dou.ua/vacancies/?search=junior+python",
    "DOU Trainee Python": "https://jobs.dou.ua/vacancies/?search=trainee+python",
    "LinkedIn Junior Python": "https://www.linkedin.com/jobs/search/?geoId=90010216&keywords=junior%20python&location=Kyiv%20Metropolitan%20Area",
    "LinkedIn Trainee Python": "https://www.linkedin.com/jobs/search/?geoId=90010216&keywords=trainee%20python&location=Kyiv%20Metropolitan%20Area",
    "Jooble Junior Python": "https://ua.jooble.org/SearchResult?p=2&rgns=%D0%9A%D0%B8%D1%97%D0%B2&ukw=junior%20python",
    "Jooble Trainee Python": "https://ua.jooble.org/SearchResult?p=2&rgns=%D0%9A%D0%B8%D1%97%D0%B2&ukw=trainee%20python",
    "GRC Junior Python": "https://grc.ua/search/vacancy?text=junior+python&from=suggest_post&fromSearchLine=true&area=115",
    "GRC Trainee Python": "https://grc.ua/search/vacancy?text=trainee+python&from=suggest_post&fromSearchLine=true&area=115",
    "Work Junior Python": "https://www.work.ua/jobs-kyiv-junior+python/",
    "Work Trainee Python": "https://www.work.ua/jobs-kyiv-trainee+python/"
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


def parse(message, site, url):
    headers = {"User-Agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"}
    soup = BeautifulSoup(get_page(url, headers), "html.parser")

    match site:
        case 'Djinni':
            list_ = parse_djinni(soup)
        case 'DOU':
            list_ = parse_dou(soup)
        case 'LinkedIn':
            list_ = parse_linkedin(soup)
        case 'Jooble':
            list_ = parse_jooble(soup)
        case 'GRC':
            list_ = parce_grc(soup)
        case 'Work':
            list_ = parce_work(soup)

    if not list_:
        bot.send_message(message.chat.id, 'No vacancies')
    else:
        text = "\n\n".join(["\n".join(i) for i in list_])
        bot.send_message(message.chat.id, text)


# Parsers
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


def parse_linkedin(soup):
    vacancies = []
    results = soup.find_all("li", {"class": "ember-view jobs-search-results__list-item occludable-update p0 relative"})
    print(results)

    for i in results[:10]:
        vacancies.append([
            # i.find
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


def parce_grc(soup):
    vacancies = []
    results = soup.find_all("div", {"class": "vacancy-serp-item-body"})

    for i in results[:10]:
        vacancies.append([
            i.find_all("a", {"class": "bloko-link"})[0].text,
            i.find_all("a", {"class": "bloko-link"})[0]["href"],
            i.find_all("a", {"class": "bloko-link"})[1].text,
            i.find("div", {"data-qa": "vacancy-serp__vacancy-address"}).text
        ])

    return vacancies


def parce_work(soup):
    vacancies = []
    results = soup.find_all("li", {"class": "b-vacancy__item js-item_list"})
    print(results)

    for i in results[:10]:
        vacancies.append([
            i.find("a", {"class": "b-vacancy__top__title js-item_title"}).text,
            i.find("a", {"class": "b-vacancy__top__title js-item_title"})["href"],
            i.find("span", {"class": "b-vacancy__tech__item"}).text.strip(),
            i.find("span", {"class": "b-vacancy__tech__item b-vacancy__tech__item-city"}).text.strip()
        ])

    return vacancies


# Main bot's function
@bot.message_handler(content_types=['text'])
def main(message):
    if message.text in buttons:
        get_buttons(message, message.text, buttons[message.text])

    if message.text in urls:
        parse(message, message.text.split()[0], urls[message.text])


bot.polling(none_stop=True)