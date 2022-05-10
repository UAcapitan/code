import sqlite3
import random
from termcolor import colored

print('App is working')

dir = __file__.replace('app_with_console.py', 'english.db')
con = sqlite3.connect(dir)
cur = con.cursor()

while True:
    cur.execute("SELECT * FROM words;")
    words = cur.fetchall()
    word_eng = random.choice(words)
    word = input(f"{word_eng[0]} - ")
    if word == word_eng[1]:
        print(colored(f"{word_eng[0]} - {word}", "green"))
    else:
        print(colored(f"{word_eng[0]} - {word_eng[1]}", "red"))
    
