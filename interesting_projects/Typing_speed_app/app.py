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
        self.check_folder()
        self.set_variables()
        self.build_menu()
        self.build_main_field()
        self.build_labels()
        self.set_text_now()
        self.set_text_in_main_field()

        self.root.bind('<Key>', self.key_pressed)
        self.root.bind('<KeyPress-Shift_L>', self.shift_delete)

    def set_variables(self):
        self.right_answers = 0
        self.wrong_answers = 0
        self.letter_now = 0

        self.text_now = 'Hello, world!'

        self.write_flag = True

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
        self.text_field = tk.Entry(self.root, width=37, justify='left', font=('Arial', 25))
        self.text_field.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    def build_labels(self):
        self.right_label = tk.Label(self.root, text='Right: ' + str(self.right_answers), fg='#00FF00')
        self.wrong_label = tk.Label(self.root, text='Wrong: ' + str(self.wrong_answers), fg='#FF0000')
        self.right_label.place(x=10, y=260)
        self.wrong_label.place(x=10, y=280)
        self.letter_label = tk.Label(self.root, text='L', bg='#00FF00', width=5, height=2)
        self.letter_label.place(x=650, y=260)

    def open_list_of_texts_json(self):
        with open('src/texts.json', 'r') as file:
            return json.load(file)['texts']

    def set_text_in_main_field(self):
        self.text_field.config(state='normal')
        self.text_field.delete(0, tk.END)
        self.text_field.insert(0, self.text_now)
        self.text_field.config(state='disabled')

    def check_folder(self):
        path = pathlib.Path(__file__).parent.resolve()
        onlyfiles = [f for f in os.listdir(path)]
        if 'src' not in onlyfiles:
            os.mkdir(str(path) + '/src')

    def exit_from_app(self):
        sys.exit()

    def key_pressed(self, event):
        if self.write_flag:
            self.letter_label['text'] = event.char
            if event.char == self.text_now[0]:
                self.right_answers += 1
                self.right_label['text'] = 'Right: ' + str(self.right_answers)
                self.letter_label.config(bg='#00FF00')
            else:
                self.wrong_answers += 1
                self.wrong_label['text'] = 'Wrong: ' + str(self.wrong_answers)
                self.letter_label.config(bg='#FF0000')
            self.text_now = self.text_now[1:]
            self.set_text_in_main_field()
            self.check_end()

    def shift_delete(self, event):
        if self.wrong_answers != 0:
            self.wrong_answers -= 1

    def check_end(self):
        if len(self.text_now) == 0:
            # TO DO
            self.write_flag = False

    def set_text_now(self):
        self.text_now = random.choice(self.open_list_of_texts_json())

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = TSApp()
    app.run()