import peewee
import json
import names
import random
import tkinter as tk

data_for_generation = {
    'email_hosts': 
        ['gmail', 'email', 'text', 'uamail', 'example', 'newmail', 'mail'],
    'domains': 
        ['ua', 'ge', 'us', 'fr', 'com', 'net', 'org'],
    'cities':
        ['Washington', 'New-York', 'Los Angeles']
}

# Class for database
class DB:
    def __init__(self) -> None:
        name = 'main.db'
        open(name, 'w').close()
        self.db = peewee.SqliteDatabase(name)

# Object of database
app_db: DB = DB()

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

        # TODO do it later

        # Button for generate data
        self.btn_generate = tk.Button(self.root, text='Generate', command=self.generate_data)

        # Places
        self.label_count_of_emails.place(x=10, y=20)
        self.count_of_emails.place(x=110, y=20)
        self.btn_generate.place(x=170, y=50)

        self.root.mainloop()

    def init_db(self) -> None:
        self.db.db.connect()
        self.db.db.create_tables([EmailModele], safe=True)

    def get_count(self) -> int:
        try:
            return int(self.count_of_emails.get())
        except:
            return 0

    def generate_data(self) -> None:
        n: int = self.get_count()
        self.init_db()
        name: str
        surname: str
        email: str = ''
        # --------------
        # 1. Generate name and surname
        # 2. Generate name + random year
        # 3. Generate surname + random year
        # 4. Generate name + city + some numbers
        # 5. Generate random letters
        # 6. Generate random letters + numbers
        # 7. Generate mixed all
        self.generate_name_and_surname(n)
        # --------------
        self.db.db.close()

    def generate_name_and_surname(self, n:int) -> None:
        for i in range(n):
            name, surname = names.get_full_name().split(' ')
            if random.randint(0,1) == 0:
                email = f'{name}.{surname}'
            else:
                email = f'{surname}.{name}'
            email += self.ending_of_email()
            self.create_new_mail([email, surname, name])

    def generate_name_and_year(self, n:int) -> None:
        for i in range(n):
            name, surname = names.get_full_name().split(' ')
            if random.randint(0,1) == 0:
                email = f'{name}.{random.choice(range(1950, 2005))}'
            else:
                email = f'{random.choice(range(1950, 2005))}.{name}'
            email += self.ending_of_email()
            self.create_new_mail([email, surname, name])

    def generate_surname_and_year(self, n:int) -> None:
        for i in range(n):
            name, surname = names.get_full_name().split(' ')
            if random.randint(0,1) == 0:
                email = f'{surname}.{random.choice(range(1950, 2005))}'
            else:
                email = f'{random.choice(range(1950, 2005))}.{surname}'
            email += self.ending_of_email()
            self.create_new_mail([email, surname, name])

    def ending_of_email(self) -> str:
        ending: str = ''
        ending += '@' + random.choice(data_for_generation['email_hosts']) + '.'
        ending += random.choice(data_for_generation['domains'])
        return ending

    def create_new_mail(self, email: list) -> None:
        EmailModele(email=email[0], user=f'{email[1]} {email[2]}').save()

if __name__ == '__main__':
    print('Start working') # TODO delete
    app: App = App()
    print('End working') # TODO delete