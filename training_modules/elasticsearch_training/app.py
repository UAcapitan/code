from elasticsearch import Elasticsearch
import psycopg2

def get_cursor():
    conn = psycopg2.connect(dbname="blog", user="app", password="thisispassword")
    return conn.cursor()

client = Elasticsearch("http://localhost:3000")

client.info()