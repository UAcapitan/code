import json
import telebot
import keys
import random
from telebot import types

TOKEN = keys.TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("/new"))

    bot.send_message(message.chat.id, 'Hi! This is bot for learning irregular verbs \
at English. For start click at button.', reply_markup=markup)

@bot.message_handler(commands=['new'])
def start_bot(message):
    with open('verbs.json', 'r') as file:
        verbs = json.load(file)
    verb = verbs[random.choice(list(verbs.keys()))]
    bot.send_message(message.chat.id, verb)

@bot.message_handler(content_types=['text'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("/new"))

    with open('verbs.json', 'r') as file:
        verbs = json.load(file)

    text = " - ".join(message.text.split()).lower()
    right_text = " - ".join(verbs[text.split()[0]]).lower()

    if text == right_text:
        result_text = f"✅ {text} ✅"
    else:
        result_text = f"❌ {text} ❌\n✅ {right_text} ✅"
    bot.send_message(message.chat.id, result_text, reply_markup=markup)

bot.polling(none_stop=True)