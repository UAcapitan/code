import tkinter as tk
import json

class TSApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Typing speed app')
        self.root.geometry('700x300')


    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = TSApp()
    app.run()