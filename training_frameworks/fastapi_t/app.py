from fastapi import FastAPI


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