import psycopg2
conn = psycopg2.connect(dbname='blog', user='app', password='thisispassword')
cursor = conn.cursor()

cursor.execute("SELECT * from users;")
records = cursor.fetchall()
print(records)

cursor.execute("SELECT * from post;")
records = cursor.fetchall()
print(records)

cursor.execute("SELECT * from likes;")
records = cursor.fetchall()
print(records)