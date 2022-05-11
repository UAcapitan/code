import sqlite3
import random
from colorama import Fore

print('App is working')

dir = __file__.replace('app_with_console.py', 'english.db')
con = sqlite3.connect(dir)
cur = con.cursor()

while True:
    cur.execute("SELECT * FROM words;")
    words = cur.fetchall()
    word_eng = random.choice(words)
    word = input(Fore.WHITE + f"{word_eng[0]} - ")
    if word == word_eng[1]:
        print(Fore.GREEN + f"{word_eng[0]} - {word}")
    else:
        print(Fore.RED + f"{word_eng[0]} - {word_eng[1]}")
    
