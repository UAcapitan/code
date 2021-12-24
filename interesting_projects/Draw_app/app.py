import tkinter as tk
import re
from PIL import ImageGrab

class DrawApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x370+300+100")
        self.root.title("Paint app")

        self.color = '#00FF00'
        self.draw = False

        self.wide_x = 5
        self.wide_y = 5

        self.cnv = tk.Canvas(self.root, bg="white", height=300, width=700)
        self.cnv.place(x=0, y=0)
        self.f1 = tk.Text(self.root, height=1, width=10)
        self.f1.place(x=160, y=310)

        self.f_btn = tk.Button(text='Change', command=self.change_color)
        self.f_btn.place(x=260, y=307)

        self.cnv_color = tk.Canvas(self.root, bg="white", height=20, width=20)
        self.cnv_color.place(x=110, y=308)
        self.cnv_color.create_rectangle(0, 0, 20, 20, fill=self.color, outline='')

        self.erase_btn = tk.Button(text='Erase all', command=self.erase_canvas)
        self.erase_btn.place(x=210, y=337)

        self.erase_btn = tk.Button(text='Fill all', command=self.fill_canvas)
        self.erase_btn.place(x=310, y=337)

        self.erase_btn = tk.Button(text='Eraser', command=self.eraser)
        self.erase_btn.place(x=340, y=307)

        self.size_field = tk.Entry(self.root, width=10)
        self.size_field.place(x=410, y=310)

        self.set_size_btn = tk.Button(self.root, text='Set size', command=self.set_size)
        self.set_size_btn.place(x=480, y=307)

        self.set_size_btn = tk.Button(self.root, text='Save', command=self.open_save_image_window)
        self.set_size_btn.place(x=390, y=337)

        self.root.resizable(False,False)

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
            self.cnv.create_rectangle(x-self.wide_x/2, y-self.wide_y/2, x+self.wide_x/2, y+self.wide_y/2, fill=self.color, outline='')

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

    def open_save_image_window(self):
        self.save_image_window = tk.Toplevel(self.root)
        self.save_image_window.geometry('200x90+95+100')
        self.save_image_window.title('Save image')
        self.save_image_window_label = tk.Label(self.save_image_window, text ='Input name of image:')
        self.save_image_window_label.place(x=20, y=10)
        self.save_image_window_entry = tk.Entry(self.save_image_window)
        self.save_image_window_entry.place(x=20, y=35)
        self.save_image_window_btn = tk.Button(self.save_image_window, command=self.save_image, text='Save image')
        self.save_image_window_btn.place(x=20, y=60)
        self.save_image_window.resizable(False,False)

    def save_image(self):
        self.name_of_image = self.save_image_window_entry.get()
        x = self.root.winfo_rootx()+self.cnv.winfo_rootx()
        y = self.root.winfo_rooty()+self.cnv.winfo_rooty()
        x1=x+self.cnv.winfo_width()
        y1=y+self.cnv.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save('saved_images/' + self.name_of_image + '.jpg')
        
    def app_run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = DrawApp()
    app.app_run()