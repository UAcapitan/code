import tkinter as tk
import json
import sys
import random
import pathlib
import os
import time
import datetime

class TSApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Typing speed app')
        self.root.geometry('700x300+100+100')
        self.start()
        self.set_binds()

    def set_variables(self):
        self.right_answers = 0
        self.wrong_answers = 0
        self.letter_now = 0
        self.time_result = 0

        self.text_now = 'Hello, world!'

        self.write_flag = True

    def build_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        menu.add_command(label='Add', command=self.open_add_window)
        menu.add_command(label='Results', command=self.open_results_window)
        menu.add_command(label='Exit', command=self.exit_from_app)

    def build_main_field(self):
        self.text_field = tk.Entry(self.root, width=37, justify='left', font=('Arial', 25))
        self.text_field.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    def build_labels(self):
        self.right_label = tk.Label(self.root, text='Right: ' + str(self.right_answers), fg='#00FF00')
        self.wrong_label = tk.Label(self.root, text='Wrong: ' + str(self.wrong_answers), fg='#FF0000')
        self.right_label.place(x=10, y=260)
        self.wrong_label.place(x=10, y=280)
        self.letter_label = tk.Label(self.root, text='...', bg='#00FF00', width=5, height=2)
        self.letter_label.place(x=650, y=260)

    def set_binds(self):
        self.root.bind('<Key>', self.key_pressed)

        self.set_wrong_binds()

    def set_wrong_binds(self):
        self.root.bind('<Shift_L>', self.wrong_delete)
        self.root.bind('<Shift_R>', self.wrong_delete)
        self.root.bind('<Caps_Lock>', self.wrong_delete)
        self.root.bind('<Control_L>', self.wrong_delete)
        self.root.bind('<Control_R>', self.wrong_delete)

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
            if len(self.text_now) == self.len_text_now:
                self.time_begin = time.perf_counter()
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

    def wrong_delete(self, event):
        if self.wrong_answers != 0:
            self.wrong_answers -= 1

    def check_end(self):
        if len(self.text_now) == 0:
            self.time_end = time.perf_counter()
            self.count_time()
            self.write_flag = False
            self.open_end_window()
            self.restart_btn = tk.Button(self.root, text='Restart', font=('Arial', 15), command=self.restart)
            self.restart_btn.place(x=590,y=150)

    def set_text_now(self):
        self.text_now = random.choice(self.open_list_of_texts_json())
        self.len_text_now = len(self.text_now)

    def open_end_window(self):
        self.end_window = tk.Toplevel(self.root)
        self.end_window.title('Results')
        self.end_window.geometry('400x150+150+150')

        self.time_end_label = tk.Label(self.end_window, text='Time: ' + self.convert_time())
        self.time_end_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        self.right_end_label = tk.Label(self.end_window, text='Right: ' + str(self.right_answers))
        self.right_end_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.symbols_end_label = tk.Label(self.end_window, text='Symbols in one minute: ' + self.symbols_per_minute())
        self.symbols_end_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        self.save_result_in_json()

    def count_time(self):
        self.time_result = int(self.time_end) - int(self.time_begin)

    def convert_time(self):
        return str(datetime.timedelta(seconds = self.time_result))

    def symbols_per_minute(self):
        if int(self.time_result) == 0:
            self.time_result = 1
        return str(int(self.right_answers / int(self.time_result) * 60))

    def start(self):
        self.check_folder()
        self.set_variables()
        self.build_menu()
        self.build_main_field()
        self.build_labels()
        self.set_text_now()
        self.set_text_in_main_field()

    def restart(self):
        self.right_label.place_forget()
        self.wrong_label.place_forget()
        self.start()
        self.restart_btn.place_forget()

    def open_add_window(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title('Add')
        self.add_window.geometry('200x120+150+150')

        self.text_add_label = tk.Label(self.add_window, text='Add new text')
        self.field_add_entry = tk.Entry(self.add_window)
        self.save_add_button = tk.Button(self.add_window, text='Save', command=self.save_new_text_in_json)

        self.text_add_label.place(x=20, y=20)
        self.field_add_entry.place(x=20, y=50)
        self.save_add_button.place(x=20, y=80)

    def open_results_window(self):
        self.results_window = tk.Toplevel(self.root)
        self.results_window.title('Results')
        self.results_window.geometry('250x450+150+150')

        tk.Label(self.results_window, text='Id   Date   Time   Right   Per/Min').place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        list_of_results = self.open_results_in_json()[:9]
        y = 0.1
        for i in list_of_results:
            tk.Label(self.results_window, text=i).place(relx=0.5, rely=y, anchor=tk.CENTER)
            y += 0.1

    def save_new_text_in_json(self):
        texts = {
            "texts":self.open_list_of_texts_json()
        }
        texts['texts'].append(self.field_add_entry.get())
        with open('src/texts.json', 'w') as file:
            json.dump(texts, file)
        self.field_add_entry.delete(0,tk.END)
        self.add_window.destroy()

    def open_results_in_json(self):
        with open('src/results.json', 'r') as file:
            return list(reversed(json.load(file)['results']))

    def save_result_in_json(self):
        list_of_results = list(reversed(self.open_results_in_json()))
        id_article = str(len(list_of_results)+1)
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        list_of_results.append(id_article + ' ' + date + ' ' + self.convert_time() 
        + ' ' + str(self.right_answers) + ' ' + self.symbols_per_minute())
        results = {
            "results":list_of_results,
        }
        with open('src/results.json', 'w') as file:
            json.dump(results, file)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = TSApp()
    # app.open_end_window()
    # app.save_result_in_json()
    app.run()