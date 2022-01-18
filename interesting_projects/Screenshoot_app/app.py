import tkinter as tk
from PIL import ImageGrab
import pyautogui


class ScreenApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Screenshoot')
        self.root.geometry("180x120")

        self.entry = tk.Entry(self.root, width=15)
        self.entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

        self.btn = tk.Button(self.root, text='Screenshoot', command=self.screen)
        self.btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def screen(self):
        width, height = pyautogui.size()
        ImageGrab.grab().crop((0,0,width,height)).save('images/test/' + 'test' + '.jpg')

    def number_check(self):
        return
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = ScreenApp()
    app.run()