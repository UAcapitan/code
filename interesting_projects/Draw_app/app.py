import tkinter as tk

class DrawApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x370")
        self.root.title("Paint app")

        self.color = '#00FF00'
        self.draw = False

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

        self.root.bind('<Motion>', self.motion)
        self.root.bind('q', self.draw_flag)

    def change_color(self):
        color = self.f1.get('1.0', tk.END)[0:7]
        self.cnv_color.create_rectangle(0, 0, 20, 20, fill=color, outline='')
        print(color)

    def motion(self, event):
        if self.draw:
            x, y = event.x, event.y
            print('{}, {}'.format(x, y))
            self.cnv.create_rectangle(x, y, x+5, y+5, fill=self.color, outline='')

    def draw_flag(self, event):
        if self.draw:
            self.draw = False
        else:
            self.draw = True
        print(self.draw)

    def erase_canvas(self):
        self.cnv.create_rectangle(0, 0, 700, 300, fill='#FFFFFF', outline='')

    def fill_canvas(self):
        self.cnv.create_rectangle(0, 0, 700, 300, fill=self.color, outline='')

    def app_run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = DrawApp()
    app.app_run()