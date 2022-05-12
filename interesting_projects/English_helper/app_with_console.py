import sqlite3
import random
from colorama import Fore

print('App is working')

dir = __file__.replace('app_with_console.py', 'english.db')
con = sqlite3.connect(dir)
cur = con.cursor()

def gap():
    for i in range(3):
        print("")

stage = int(input(
"1. Translate from English\n\
2. Translate to English\n\n"
))

gap()

limit = int(input(
"1. Without limit\n\
2. Limit 30 words\n\n"
))

gap()

if stage == 1 and limit == 1:
    cur.execute("SELECT * FROM words;")
    words = cur.fetchall()
    while True:
        word_eng = random.choice(words)
        word = input(Fore.WHITE + f"{word_eng[0]} - ")
        if word == word_eng[1]:
            print(Fore.GREEN + f"{word_eng[0]} - {word}")
        else:
            print(Fore.RED + f"{word_eng[0]} - {word_eng[1]}")
        gap()

if stage == 2 and limit == 1:
    cur.execute("SELECT * FROM words;")
    words = cur.fetchall()
    while True:
        word_eng = random.choice(words)
        word = input(Fore.WHITE + f"{word_eng[1]} - ")
        if word == word_eng[0]:
            print(Fore.GREEN + f"{word_eng[1]} - {word}")
        else:
            print(Fore.RED + f"{word_eng[1]} - {word_eng[0]}")
        gap()

if stage == 1 and limit == 2:
    cur.execute("SELECT * FROM words;")
    words = cur.fetchall()[:30]
    while True:
        word_eng = random.choice(words)
        word = input(Fore.WHITE + f"{word_eng[0]} - ")
        if word == word_eng[1]:
            print(Fore.GREEN + f"{word_eng[0]} - {word}")
        else:
            print(Fore.RED + f"{word_eng[0]} - {word_eng[1]}")
        gap()

if stage == 2 and limit == 2:
    cur.execute("SELECT * FROM words;")
    words = cur.fetchall()[:30]
    while True:
        word_eng = random.choice(words)
        word = input(Fore.WHITE + f"{word_eng[1]} - ")
        if word == word_eng[0]:
            print(Fore.GREEN + f"{word_eng[1]} - {word}")
        else:
            print(Fore.RED + f"{word_eng[1]} - {word_eng[0]}")
        gap()