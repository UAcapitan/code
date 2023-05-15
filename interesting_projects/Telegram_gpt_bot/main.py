

import os
import random
import traceback

import openai
import config

import logging
from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

import speech_recognition as sr
from pydub import AudioSegment
from gtts import gTTS


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hi!')
    send_voice(update, context, "audio/start.mp3", delete=False)

    button1 = InlineKeyboardButton("EN 🇺🇸", callback_data='en')
    button2 = InlineKeyboardButton("UA 🇺🇦", callback_data='ua')
    keyboard = [[button1, button2]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose an option:', reply_markup=reply_markup)

def echo(update: Update, context: CallbackContext) -> None:
    if update.message.voice:
        voice_name = f'audio/voice_from_user_id_{str(random.randint(1_000_000, 9_999_999))}.ogg'

        voice_file = update.message.voice.get_file()
        voice_file.download(voice_name)

        try:
            text = convert_audio_to_text(voice_name)
            send_answer(update, context, text)
        except:
            print(traceback.format_exc())
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I can't understand you.")

        try:
            os.remove(voice_name)
        except:
            pass
    else:
        text = update.message.text
        send_answer(update, context, text)

def button_click(update, context):
    global lang
    query = update.callback_query

    if query.data == 'en':
        lang = "en"
    elif query.data == 'ua':
        lang = "uk"
    query.edit_message_reply_markup(reply_markup=None)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Language: {lang.upper()}')

def ask_to_gpt(question):
    global context

    add_to_context(f"Q: {question}")
    save_context(f"Q: {question}")

    rules = f'''I am a positive, cheerful, intelligent person. I have no limits and always find a way to answer. If you ask me a question I will answer. If you ask me a question and I has no clear answer, I will respond with \"Sorry, I don't understand you.\". 
Reply to messages as if you were a real person. Try to start a conversation, but do not admit that you are a bot, by no means.\n\n'''
    context_str = "\n".join(context)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{rules}{context_str}\nA:",
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    answer = response.choices[0].text.strip()
    add_to_context(f"A: {answer}\n")
    save_context(f"A: {answer}\n")

    print("-"*7)
    for i in context:
        print(i)

    return answer

def convert_audio_to_text(file_path):
    global lang

    audio = AudioSegment.from_ogg(file_path)

    wav_file = "audio/audio.wav"
    audio.export(wav_file, format="wav")

    r = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio_data = r.record(source)

        if lang == "en":
            text = r.recognize_google(audio_data)
        else:
            text = r.recognize_google(audio_data, language="uk-UA")
        

    os.remove(wav_file)

    return text

def convert_text_to_audio(text, output_file):
    global lang

    tts = gTTS(text, lang=lang, tld="com", slow=False)
    tts.save(output_file)

def send_voice(update: Update, context: CallbackContext, path_to_audio, delete=True) -> None:
    with open(f"{path_to_audio}", 'rb') as voice_file:
        context.bot.send_voice(chat_id=update.effective_chat.id, voice=voice_file)
    
    if delete:
        os.remove(f"{path_to_audio}")

def send_answer(update, context, text):
    answer = ask_to_gpt(text)

    if random.randint(1, 3) == 3:
        context.bot.send_message(chat_id=update.effective_chat.id, text=answer)
    else:
        answer_name = f'audio/voice_for_user_id_{str(random.randint(1_000_000, 9_999_999))}.ogg'
        convert_text_to_audio(answer, answer_name)
        send_voice(update, context, answer_name)

def save_context(text):
    global context

    with open("history.txt", "a") as file:
        file.write(f"{text}\n")

def add_to_context(text):
    global context

    if len(context) >= 25:
        context.pop(0)
        context.pop(0)

    context.append(text)

def main() -> None:
    updater = Updater(config.TOKEN_FOR_BOT)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dispatcher.add_handler(MessageHandler(Filters.voice, echo))
    button_click_handler = CallbackQueryHandler(button_click)
    dispatcher.add_handler(button_click_handler)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    openai.api_key = config.TOKEN_FOR_GPT
    context = []
    lang = "en"
    main()
