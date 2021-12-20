import tkinter as tk
import re

class DrawApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x370")
        self.root.title("Paint app")

        self.color = '#00FF00'
        self.draw = False

        self.wide_x = 5
        self.wide_y = 5

        self.cnv = tk.Canvas(self.root, bg="white", height=300, width=700)
        self.cnv.place(x=0, y=0)
        self.f1 = tk.Text(self.root, height=1, width=10)
        self.f1.place(x=90, y=310)

        self.f_btn = tk.Button(text='Change', command=self.change_color)
        self.f_btn.place(x=190, y=307)

        self.cnv_color = tk.Canvas(self.root, bg="white", height=20, width=20)
        self.cnv_color.place(x=50, y=308)
        self.cnv_color.create_rectangle(0, 0, 20, 20, fill=self.color, outline='')

        self.erase_btn = tk.Button(text='Erase all', command=self.erase_canvas)
        self.erase_btn.place(x=40, y=337)

        self.erase_btn = tk.Button(text='Fill all', command=self.fill_canvas)
        self.erase_btn.place(x=110, y=337)

        self.erase_btn = tk.Button(text='Eraser', command=self.eraser)
        self.erase_btn.place(x=250, y=307)

        self.size_field = tk.Entry(self.root, width=10)
        self.size_field.place(x=310, y=310)

        self.set_size_btn = tk.Button(self.root, text='Set size', command=self.set_size)
        self.set_size_btn.place(x=380, y=307)

        self.root.bind('<Motion>', self.motion)
        self.root.bind('q', self.draw_flag)

    def change_color(self):
        color = self.f1.get('1.0', tk.END)[0:7]

        if re.fullmatch('^\#[0F8]{6}$', color):
            self.color = color
            self.set_color()
            self.f1.delete(1.0,"end")
        else:
            self.open_error_window()
            self.f1.delete(1.0,"end")

    def motion(self, event):
        if self.draw:
            x, y = event.x, event.y
            self.cnv.create_rectangle(x, y, x+self.wide_x, y+self.wide_y, fill=self.color, outline='')

    def draw_flag(self, event):
        if self.draw:
            self.draw = False
        else:
            self.draw = True
        self.f1.delete(1.0,"end")
        self.size_field.delete(0, tk.END)

    def erase_canvas(self):
        self.cnv.create_rectangle(0, 0, 700, 300, fill='#FFFFFF', outline='')

    def fill_canvas(self):
        self.cnv.create_rectangle(0, 0, 700, 300, fill=self.color, outline='')

    def eraser(self):
        self.wide_x = 10
        self.wide_y = 10
        self.color = '#FFFFFF'
        self.set_color()

    def set_color(self):
        self.cnv_color.create_rectangle(0, 0, 20, 20, fill=self.color, outline='')

    def set_size(self):
        try:
            size = int(self.size_field.get())
            self.wide_x = size
            self.wide_y = size
        except:
            self.open_error_window()
        self.size_field.delete(0, tk.END)

    def open_error_window(self):
        self.error_window = tk.Toplevel(self.root)
        self.error_label = tk.Label(self.error_window, text = "Error")
        self.error_label.pack()

    def app_run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = DrawApp()
    app.app_run()