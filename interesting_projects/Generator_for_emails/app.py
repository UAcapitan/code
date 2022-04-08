import peewee
import json
import names
import random
import tkinter as tk

data_for_generation: dict = {
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
        self.db: peewee.SqliteDatabase = peewee.SqliteDatabase(name)

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

        self.root.geometry('300x290')
        self.root.title('Generating of data')
        self.db: DB = app_db

        self.val: tk.StringVar = tk.StringVar(value='7')
        self.values: dict = {
            "Name and surname" : "1",
            "Name and year" : "2",
            "Surname and year" : "3",
            "Name, city and numbers" : "4",
            "Letters" : "5",
            "Letters and numbers": "6",
            "Mix": "7"
        }

        # Elements
        self.label_count_of_emails = tk.Label(self.root, text='Count of emails: ')
        self.count_of_emails = tk.Entry(self.root)

        # Radiobuttons
        self.radio_list: list = []
        for (t, v) in self.values.items():
            self.radio_list.append(tk.Radiobutton(self.root, text=t, variable=self.val, value=v))

        x, y = 20, 70
        for i in self.radio_list:
            i.place(x=x, y=y)
            y += 30

        # Button for generate data
        self.btn_generate = tk.Button(self.root, text='Generate', command=self.generate_data)

        # Places
        self.label_count_of_emails.place(x=10, y=20)
        self.count_of_emails.place(x=110, y=20)
        self.btn_generate.place(x=170, y=70)

        tk.Button(self.root, text='Test', command=lambda: self.show_error_window('text', (200, 50)),).place(x=170, y=100)

        self.root.mainloop()

    def init_db(self) -> None:
        self.db.db.connect()
        self.db.db.create_tables([EmailModele], safe=True)

    def get_count(self) -> int:
        try:
            return int(self.count_of_emails.get())
        except:
            self.show_error_window('Wrong type input', (100, 50))
            return 0

    def generate_data(self) -> None:
        n: int = int(self.get_count())
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
        print(f"{self.val.get()} - number of val") # TODO delete later
        if self.val.get() == "1":
            self.generate_name_and_surname(n)
        elif self.val.get() == "2":
            self.generate_name_and_year(n)
        elif self.val.get() == "3":
            self.generate_surname_and_year(n)
        elif self.val.get() == "4":
            self.generate_name_city_numbers(n)
        elif self.val.get() == "5":
            self.generate_some_letters(n)
        elif self.val.get() == "6":
            self.generate_some_letters_and_numbers(n)
        elif self.val.get() == "7":
            self.generate_mixed_emails(n)
        print("It was working") # TODO delete later
        # --------------
        self.db.db.close()

    # Types of generating
    # ---------------------------
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

    def generate_name_city_numbers(self, n:int) -> None:
        for i in range(n):
            name, surname = names.get_full_name().split(' ')
            if random.randint(0,1) == 0:
                email = f'{surname}.{random.choice(data_for_generation["cities"])}{random.randint(0,10500)}'
            else:
                email = f'{random.choice(data_for_generation["cities"])}.{surname}{random.randint(0,10500)}'
            email += self.ending_of_email()
            self.create_new_mail([email, surname, name])

    def generate_some_letters(self, n:int) -> None:
        for i in range(n):
            name, surname = names.get_full_name().split(' ')
            email: str = ''
            for j in range(random.randint(0, 9)):
                email += chr(random.randint(97, 122))
            email += self.ending_of_email()
            self.create_new_mail([email, surname, name])

    def generate_some_letters_and_numbers(self, n:int) -> None:
        for i in range(n):
            name, surname = names.get_full_name().split(' ')
            email: str = ''
            for j in range(random.randint(0, 10)):
                if random.randint(0, 3) in [1,2,3]:
                    email += chr(random.randint(97, 122))
                else:
                    email += str(random.randint(0, 9))
            email += self.ending_of_email()
            self.create_new_mail([email, surname, name])

    def generate_mixed_emails(self, n: int) -> None:
        methods_list = [
            self.generate_name_and_surname,
            self.generate_name_and_year,
            self.generate_surname_and_year,
            self.generate_name_city_numbers,
            self.generate_some_letters,
            self.generate_some_letters_and_numbers
        ]
        for i in range(n):
            random.choice(methods_list)(1)

    # ---------------------------

    # Generate ending for email
    def ending_of_email(self) -> str:
        ending: str = ''
        ending += '@' + random.choice(data_for_generation['email_hosts']) + '.'
        ending += random.choice(data_for_generation['domains'])
        return ending

    def create_new_mail(self, email: list) -> None:
        EmailModele(email=email[0], user=f'{email[1]} {email[2]}').save()
    
    # Open window when will be error
    # Error types:
    # - Text instead numbers
    # - Too much data
    # - Any another problems
    def show_error_window(self, text: str, size: tuple[int]) -> None:
        self.error_window = tk.Toplevel(self.root)
        self.error_window.geometry(f"{size[0]}x{size[1]}")

        self.error_label = tk.Label(self.error_window, text=text)
        self.error_label.place(relx=.5, y=25, anchor="center")

if __name__ == '__main__':
    app: App = App()