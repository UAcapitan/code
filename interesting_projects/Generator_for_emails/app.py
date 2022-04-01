import peewee
import json
import names
import random
import tkinter as tk
from typing import Type

data_for_generation = {
    'email_hosts': 
        ['gmail', 'email', 'text', 'uamail', 'example', 'newmail', 'mail'],
    'domains': 
        ['ua', 'ge', 'us', 'fr', 'com', 'net', 'org']
}

# TODO set up
# name_of_file = input('Input name of file:\n')

name_of_file = 'test'

# Class for database
class DB:
    def __init__(self) -> None:
        self.set_db_file('test')

    def set_db_file(self, name: str) -> None:
        name = name_of_file + '.db'
        open(name, 'w').close()
        self.db = peewee.SqliteDatabase(name)

app_db: Type[DB] = DB()

# Modele of email
class EmailModele(peewee.Model):
    id = peewee.AutoField()
    email = peewee.CharField(unique=True)
    user = peewee.CharField()

    class Meta:
        database = DB().db

# Class for application, all functional of app
class App:
    def __init__(self, db: Type[DB]) -> None:
        self.root = tk.Tk()

        self.root.geometry('300x250')
        self.root.title('Generating of data')
        self.db = app_db.db

        # Elements
        self.label_name_of_files = tk.Label(self.root, text='Name for db: ')
        self.name_of_file = tk.Entry(self.root)
        self.label_count_of_emails = tk.Label(self.root, text='Count of emails: ')
        self.count_of_emails = tk.Entry(self.root)
        self.btn_generate = tk.Button(self.root, text='Generate', command=self.generate_data)

        # Places
        self.label_name_of_files.place(x=10, y=10)
        self.name_of_file.place(x=110, y=10)
        self.label_count_of_emails.place(x=10, y=40)
        self.count_of_emails.place(x=110, y=40)
        self.btn_generate.place(x=170, y=80)

        self.root.mainloop()

    def init_db(self) -> None:
        self.db.connect()
        self.db.create_tables([EmailModele], safe=True)
        self.db.close()

    def set_name(self) -> None:
        if self.name_of_file.get() != '':
            print(self.name_of_file.get())
            app_db.set_db_file(self.name_of_file.get())
            DB.db = self.name_of_file.get()

    def get_count(self) -> int:
        try:
            return int(self.count_of_emails.get())
        except:
            return 0

    def generate_data(self) -> None:
        self.set_name()
        n: int = self.get_count()
        self.init_db()
        name: str
        surname: str
        email: str = ''
        for i in range(n):
            name, surname = names.get_full_name().split(' ')
            if random.randint(0,1) == 0:
                email = f'{name}_{surname}'
            else:
                email = f'{surname}_{name}'
            email += '@' + random.choice(data_for_generation['email_hosts']) + '.'
            email += random.choice(data_for_generation['domains'])
            EmailModele(email=email, user=f'{surname} {name}').save()

if __name__ == '__main__':
    print('Start working') # TODO delete
    app_db: Type[DB] = DB()
    app: Type[App] = App(app_db.db)
    print('End working') # TODO delete

