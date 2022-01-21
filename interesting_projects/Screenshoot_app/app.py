import tkinter as tk
from PIL import ImageGrab
import pyautogui
import os
import keyboard


class ScreenApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Screenshoot')

        self.entry = tk.Entry(self.root, width=15)

        self.btn = tk.Button(self.root, text='Screenshoot', command=self.screen)

        self.set_start()

        self.key_down()

        self.run()

    def screen(self):
        self.check_worked()
        width, height = pyautogui.size()
        ImageGrab.grab().crop((0,0,width,height)).save('images/' + self.entry.get() + '/' + str(self.last_image_index()) + '.jpg')

    def last_image_index(self):
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

    def check_worked(self):
        if not self.worked:
            self.set_after_screen()

    def restart(self):
        self.entry.config(state='normal')
        self.set_start()
        self.entry.delete(0, 'end')
        self.btn_restart.place_forget()

    def set_start(self):
        self.root.geometry("300x120")
        self.entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        self.btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
        self.worked = False

    def set_after_screen(self):
        self.entry.config(state='disable')
        self.root.geometry("300x190")
        self.worked = True
        self.btn_restart = tk.Button(text='Restart', command=self.restart)
        self.entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.btn_restart.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = ScreenApp()