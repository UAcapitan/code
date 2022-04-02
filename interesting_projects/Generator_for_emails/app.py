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

# Class for database
class DB:
    def __init__(self) -> None:
        self.set_db_file('main')

    def set_db_file(self, name: str) -> None:
        print('Work set db file test')
        name = 'main.db'
        open(name, 'w').close()
        self.db = peewee.SqliteDatabase(name)

app_db: Type[DB] = DB()

# Modele of email
class EmailModele(peewee.Model):
    id = peewee.AutoField()
    email = peewee.CharField(unique=True)
    user = peewee.CharField()

    class Meta:
        database = app_db.db

# Class for application, all functional of app
class App:
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.geometry('300x250')
        self.root.title('Generating of data')
        self.db = app_db

        # Elements
        self.label_count_of_emails = tk.Label(self.root, text='Count of emails: ')
        self.count_of_emails = tk.Entry(self.root)
        self.btn_generate = tk.Button(self.root, text='Generate', command=self.generate_data)

        # Places
        self.label_count_of_emails.place(x=10, y=20)
        self.count_of_emails.place(x=110, y=20)
        self.btn_generate.place(x=170, y=50)

        self.root.mainloop()

    def init_db(self) -> None:
        self.db.db.connect()
        self.db.db.create_tables([EmailModele], safe=True)

    def set_name(self) -> None:
        if self.name_of_file.get() != '':
            self.db.set_db_file(self.name_of_file.get())

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
        self.db.db.close()

if __name__ == '__main__':
    print('Start working') # TODO delete
    app: Type[App] = App()
    print('End working') # TODO delete