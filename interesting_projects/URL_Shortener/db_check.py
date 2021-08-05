import sqlite3 as lite

con = lite.connect('blog.db')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Page")

    rows = cur.fetchall()

    for row in rows:
        print(row)