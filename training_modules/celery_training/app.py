from celery import Celery

app = Celery('hello')

@app.task
def hello():
    return "Hello, world!"

@app.task
def text():
    return "Just a text"

@app.task
def for_test():
    return "For test app"