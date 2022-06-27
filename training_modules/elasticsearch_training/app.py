from elasticsearch import Elasticsearch
import psycopg2
import keys
import random

def generate_users():
    for i in range(8):
        doc = {
            'id':i,
            'name':f'Name_{i}',
            'password':'1234567',
            'age':random.randint(16,70),
            'rate':random.randint(0,10)
        }
        resp = es.index(index="test", id=i, document=doc)
        print(resp['result'])

def generate_text():
    list_for_title = [
        'Love',
        'Story',
        'Science',
        'Music',
        'Guitar',
        'Weather',
        'Kids',
        'Piano',
        'Girl',
        'Kiss',
        'Dance'
    ]

    list_for_text = [
        "I love ice cream.",
        "This is so big.",
        "This is my homeland.",
        "New history of this city",
        "I wanna it this piece of the cake",
        "This is not big ship, I have seen bigger.",
        "Interesting information about us.",
        "I guess we didn't eat it.",
        "You know this rule.",
        "This is enough information for this task."
    ]

    return {
        'title':random.choice(list_for_title),
        'text': " ".join([random.choice(list_for_text) for i in range(random.randint(2, 4))])
    }

def generate_post():
    for i in range(100):
        text = generate_text()
        doc = {
            'id': i,
            'title': text["title"],
            'article': text["text"],
            'author': random.randint(1, 99),
            'published': random.choice([True, False])
        }
        resp = es.index(index="test", id=i, document=doc)
        print(resp['result'])

if __name__ == "__main__":
    conn = psycopg2.connect(dbname="blog", user="app", password="thisispassword")
    curs = conn.cursor()
    es = Elasticsearch(hosts=f"http://{keys.username}:{keys.password}@localhost:9200/")
    # generate_post()
    # generate_users()
    # es.indices.refresh(index="test")
    query_body = {
        "query": {
            "match": {
                "article": "love"
            }
        }
    }
    resp = es.search(index="test", body=query_body)
    
    for i in resp["hits"]["hits"]:
        i = i["_source"]
        print(f"{i['id']}. {i['title']}")

    new_query_body = {
        "query": {
            "match": {
                "article": "this"
            }
        }
    }
    
    new_resp = es.search(index="test", body=new_query_body)

    list_ = resp["hits"]["hits"]

    for i in list_:
        i = i["_source"]
        print(f"{i['id']}. {i['title']}")

    # es.info()