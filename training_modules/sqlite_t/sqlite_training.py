import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    # query = """ CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, login TEXT, password TEXT) """
    query = """INSERT INTO users(id, name, login, password) VALUES ('1', 'Ed', 'EdMix', 'edmix22')"""
    cursor.execute(query)
    db.commit()