import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, login TEXT, password TEXT) """
    query_2 = """INSERT INTO users(id, name, login, password) VALUES ('1', 'Ed', 'EdMix', 'edmix22')"""
    cursor.execute(query)
    cursor.execute(query_2)
    db.commit()

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS users(id INTEGER, name TEXT, login TEXT, password TEXT) """
    query_2 = """INSERT INTO users(id, name, login, password) VALUES (?,?,?,?)"""
    cursor.execute(query)
    l_t = [
        (6, 'Kiril', 'guy_good', '193422243'),
        (7, 'Michael', 'Mi', 'uiwqrehjfbji'),
        (8, 'Georgiy', 'Gi', 'iewouoiw'),
        (9, 'Li', 'li_naruto_man', '734yierw'),
    ]
    cursor.executemany(query_2, l_t)
    db.commit()

    query = """SELECT * FROM users"""
    cursor.execute(query)
    for i in cursor:
        print(i)

    print(end='\n')

    query = """SELECT login, password FROM users WHERE id > 3"""
    cursor.execute(query)
    for i in cursor:
        print(i)

    query = """DROP TABLE users"""
    cursor.execute(query)