import peewee
import json
import names
import random
import tkinter as tk

data_for_generation = {
    'email_hosts': 
        ['gmail', 'email', 'text', 'uamail', 'example', 'newmail', 'mail'],
    'domains': 
        ['ua', 'ge', 'us', 'fr', 'com', 'net', 'org']
}

class DB:
    def __init__(self) -> None:
        self.db = peewee.SqliteDatabase('emails.db')

class BaseModel(peewee.Model):
    class Meta:
        database = DB().db

class EmailModule(BaseModel):
    id = peewee.AutoField()
    username = peewee.CharField(unique=True)
    user = peewee.CharField()

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()

if __name__ == '__main__':
    print('Start working') #TODO delete
    app = App()

