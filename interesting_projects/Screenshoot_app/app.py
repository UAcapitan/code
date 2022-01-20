import tkinter as tk
from PIL import ImageGrab
import pyautogui
import os
import keyboard


class ScreenApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Screenshoot')
        self.root.geometry("300x120")

        self.entry = tk.Entry(self.root, width=15)
        self.entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.btn = tk.Button(self.root, text='Screenshoot', command=self.screen)
        self.btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.worked = False

        self.key_down()

        self.run()

    def screen(self):
        width, height = pyautogui.size()
        ImageGrab.grab().crop((0,0,width,height)).save('images/test/' + str(self.last_image_index()) + '.jpg')

    def last_image_index(self):
        self.entry.config(state='disable')
        self.root.geometry("300x150")
        self.check_folder()
        last = os.listdir(os.getcwd() + '/images/' + self.entry.get() + '/')
        last = [int(i) for i in [i.replace('.jpg', '') for i in last] if i.isdigit()]
        if last == []:
            return 1
        return max(last) + 1

    def check_folder(self):
        if self.entry.get() not in os.listdir(os.getcwd() + '/images/'):
            os.mkdir(os.getcwd() + '/images/' + self.entry.get())

    def key_down(self):
        keyboard.add_hotkey('o+p', self.screen)
    
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = ScreenApp()