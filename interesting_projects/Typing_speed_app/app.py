import tkinter as tk
import json
import sys
import random
import pathlib
import os

class TSApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Typing speed app')
        self.root.geometry('700x300')
        self.set_variables()
        self.build_menu()
        self.build_main_field()
        self.build_labels()

    def set_variables(self):
        self.right_answers = 0
        self.wrong_answers = 0
        self.letter_now = 0

        self.text_now = 'Hello, world!'

    def build_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        main_menu = tk.Menu(menu)
        main_menu.add_command(label="User")
        main_menu.add_command(label="Add")
        menu.add_cascade(label="Main", menu=main_menu)

        result_menu = tk.Menu(menu)
        result_menu.add_command(label="Table")
        result_menu.add_command(label="User")
        menu.add_cascade(label="Result", menu=result_menu)

        menu.add_command(label='Exit', command=self.exit_from_app)

    def build_main_field(self):
        self.text_field = tk.Entry(self.root, width=37, justify='right', font=('Arial', 25))
        self.text_field.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    def build_labels(self):
        self.right_label = tk.Label(self.root, text='Right: 0', fg='#00FF00')
        self.wrong_label = tk.Label(self.root, text='Wrong: 0', fg='#FF0000')
        self.right_label.place(x=10, y=260)
        self.wrong_label.place(x=10, y=280)
        self.letter_label = tk.Label(self.root, text='L', bg='#00FF00', width=5, height=2)
        self.letter_label.place(x=650, y=260)

    def open_list_of_texts_json(self):
        with open('src/texts.json', 'r') as file:
            return json.load(file)['texts']

    def set_text_in_main_field(self):
        self.text_field.delete(0, tk.END)
        self.text_field.insert(0, self.open_list_of_texts_json()[0])
        self.text_field.config(state='disabled')

    def check_folder(self):
        path = pathlib.Path(__file__).parent.resolve()
        onlyfiles = [f for f in os.listdir(path)]
        if 'src' not in onlyfiles:
            os.mkdir(str(path) + '/src')

    def exit_from_app(self):
        sys.exit()

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = TSApp()
    app.check_folder()
    app.set_text_in_main_field()
    app.run()