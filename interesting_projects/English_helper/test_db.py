import sqlite3

con = sqlite3.connect("english.db")
cursor = con.cursor()

cursor.execute("SELECT english, russian FROM words;")
print(cursor.fetchall())