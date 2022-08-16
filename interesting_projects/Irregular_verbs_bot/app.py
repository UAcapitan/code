import telebot
import keys
import random

TOKEN = keys.TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, '')

bot.polling(none_stop=True)