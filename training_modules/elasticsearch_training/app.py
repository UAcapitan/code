from elasticsearch import Elasticsearch
import psycopg2
import keys
import random


conn = psycopg2.connect(dbname="blog", user="app", password="thisispassword")
curs = conn.cursor()

host = ''
port = 0
dbname = ''
user = ''
password = ''

es = Elasticsearch(hosts=f"http://{keys.username}:{keys.password}@localhost:9200/")

for i in range(8):

    doc = {
        'id':i,
        'name':f'Name_{i}',
        'password':'1234567',
        'age':random.randint(16,70),
        'rate':random.randint(0,10)
    }

    resp = es.index(index="post", id=i, document=doc)
    print(resp['result'])

es.indices.refresh(index="post")

resp = es.search(index="post", query={"match_all": {}})

print(resp["hits"]["hits"])

# es.info()