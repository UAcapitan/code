from fastapi import FastAPI
from schemas import Book


app = FastAPI()

@app.get('/')
def home():
    return {'key':'test'}

@app.get('/{pk}')
def get_item(pk: int):
    return {'key': pk}

@app.get('/text/{q}')
def get_text(q: str, t: str = None):
    return {'key': q, 'text':t}

@app.get('/test/{pk}/{t}')
def get_test(pk: int, t: str):
    return {'key': pk, 'text':t}

@app.get('/user/{user}/item/{id}')
def get_user_item(user: str, id: int):
    return {'user': user, 'id':id}

@app.post('/book')
def create_book(item: Book):
    return item