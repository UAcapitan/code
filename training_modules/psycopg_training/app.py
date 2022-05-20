import psycopg2
conn = psycopg2.connect(dbname='blog', user='postgres')
cursor = conn.cursor()

cursor.execute("CREATE DATABASE online;")
records = cursor.fetchall()
print(records)