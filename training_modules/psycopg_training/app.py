import psycopg2
conn = psycopg2.connect(dbname='blog', user='postgres')
cursor = conn.cursor()

