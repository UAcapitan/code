from fastapi import FastAPI, Query, Path, Body
from schemas import Book, BookOut
from typing import List


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

@app.post('/book', response_model=Book, response_model_exclude_unset=False)
def create_book(item: Book = Body(..., embed=True)):
    return item

@app.post('/bookOut', response_model=BookOut, response_model_exclude={'pages', 'count'})
def create_book(item: Book = Body(..., embed=True)):
    return BookOut(**item.dict(), id=3)

@app.post('/bookInclude', response_model=Book, response_model_include={'pages', 'count'})
def create_book(item: Book = Body(..., embed=True)):
    return item

@app.get('/books/book')
def get_book(q: List[str] = Query(..., description='Search book', deprecated=True)):
    return q

@app.get('/books/book/{pk}')
def get_book(pk: int = Path(..., gt=1, lt=10), pages: int = Query(None, gt=10, le=500)):
    return {pk: pages}

@app.post('/update/data')
def get_data(data: str = Body(...)):
    return {'data': data}
