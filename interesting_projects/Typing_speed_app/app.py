import tkinter as tk
import json

class TSApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Typing speed app')
        self.root.geometry('700x300')
        self.set_variables()
        self.build_main_field()
        self.build_labels()


    def set_variables(self):
        self.right_answers = 0
        self.wrong_answers = 0
        self.letter_now = 0

        self.text_now = 'Hello, world!'

    def build_main_field(self):
        self.text_field = tk.Entry(self.root)
        self.text_field.place(x=10, y=140)

    def build_labels(self):
        self.right_label = tk.Label(self.root, text='Right: 0')
        self.wrong_label = tk.Label(self.root, text='Wrong: 0')
        self.right_label.place(x=10, y=240)
        self.wrong_label.place(x=10, y=280)
        self.letter_label = tk.Label(self.root, text='L')
        self.letter_label.place(x=670, y=280)


    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = TSApp()
    app.run()