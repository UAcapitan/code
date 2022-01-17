import tkinter as tk

class ScreenApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Screenshoot')
        self.root.geometry("200x300")

        self.btn = tk.Button(text='Screenshoot')
    
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = ScreenApp()
    app.run()