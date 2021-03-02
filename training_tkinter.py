from tkinter import *
from math import ceil

# Что такое Tkinter

# class Calculater:
#     def __init__(self, root):
#         self.number_1 = Entry(root, width=20)
#         self.number_2 = Entry(root, width=20)
#         self.button_add = Button(root, text='+')
#         self.button_min = Button(root, text='-')
#         self.button_mul = Button(root, text='*')
#         self.button_div = Button(root, text='/')
#         self.lab = Label(root, width=20)

#         self.button_add['command'] = self.function_add
#         self.button_min['command'] = self.function_min
#         self.button_mul['command'] = self.function_mul
#         self.button_div['command'] = self.function_div

#         self.number_1.pack()
#         self.number_2.pack()
#         self.button_add.pack()
#         self.button_min.pack()
#         self.button_mul.pack()
#         self.button_div.pack()
#         self.lab.pack()

#     def function_add(self):
#         try:
#             self.lab['text'] = float(self.number_1.get()) + float(self.number_2.get())
#         except:
#             self.lab['text'] = 'Error'
    
#     def function_min(self):
#         try:
#             self.lab['text'] = float(self.number_1.get()) - float(self.number_2.get())
#         except:
#             self.lab['text'] = 'Error'

#     def function_mul(self):
#         try:
#             self.lab['text'] = float(self.number_1.get()) * float(self.number_2.get())
#         except:
#             self.lab['text'] = 'Error'

#     def function_div(self):
#         try:
#             self.lab['text'] = round(float(self.number_1.get()) / float(self.number_2.get()),2)
#         except:
#             self.lab['text'] = 'Error'

# root = Tk()
# main_window = Calculater(root)
# root.mainloop()

# Виджеты Button, Label, Entry

# class Color:
#     def __init__(self,root):
#         self.lab = Label(root,text='-----')
#         self.text = Entry(root,width=20)
#         self.button_red = Button(root, command=self.color_button_red,bg='#ff0000', width=20)
#         self.button_orange = Button(root, command=self.color_button_orange,bg='#ff7d00', width=20)
#         self.button_yellow = Button(root, command=self.color_button_yellow,bg='#ffff00', width=20)
#         self.button_green = Button(root, command=self.color_button_green,bg='#00ff00', width=20)
#         self.button_light_blue = Button(root, command=self.color_button_light_blue,bg='#007dff', width=20)
#         self.button_blue = Button(root, command=self.color_button_blue,bg='#0000ff', width=20)
#         self.button_purple = Button(root, command=self.color_button_purple,bg='#7d00ff', width=20)

#         self.lab.pack()
#         self.text.pack()
#         self.button_red.pack()
#         self.button_orange.pack()
#         self.button_yellow.pack()
#         self.button_green.pack()
#         self.button_light_blue.pack()
#         self.button_blue.pack()
#         self.button_purple.pack()

#     def color_button_red(self):
#         self.lab['text'] = 'Red'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_red['bg'])

#     def color_button_orange(self):
#         self.lab['text'] = 'Orange'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_orange['bg'])

#     def color_button_yellow(self):
#         self.lab['text'] = 'Yellow'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_yellow['bg'])

#     def color_button_green(self):
#         self.lab['text'] = 'Green'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_green['bg'])

#     def color_button_light_blue(self):
#         self.lab['text'] = 'Light blue'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_light_blue['bg'])

#     def color_button_blue(self):
#         self.lab['text'] = 'Blue'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_blue['bg'])

#     def color_button_purple(self):
#         self.lab['text'] = 'Purple'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_purple['bg'])

# root = Tk()
# color = Color(root)
# root.mainloop()

# Метод pack

# class Color:
#     def __init__(self,root):
#         self.lab = Label(root,text='-----')
#         self.text = Entry(root,width=20)
#         self.button_red = Button(root, command=self.color_button_red,bg='#ff0000', width=3, height=1)
#         self.button_orange = Button(root, command=self.color_button_orange,bg='#ff7d00', width=3, height=1)
#         self.button_yellow = Button(root, command=self.color_button_yellow,bg='#ffff00', width=3, height=1)
#         self.button_green = Button(root, command=self.color_button_green,bg='#00ff00', width=3, height=1)
#         self.button_light_blue = Button(root, command=self.color_button_light_blue,bg='#007dff', width=3, height=1)
#         self.button_blue = Button(root, command=self.color_button_blue,bg='#0000ff', width=3, height=1)
#         self.button_purple = Button(root, command=self.color_button_purple,bg='#7d00ff', width=3, height=1)

#         self.lab.pack(side=TOP)
#         self.text.pack(side=TOP)
#         self.button_red.pack(side=LEFT)
#         self.button_orange.pack(side=LEFT)
#         self.button_yellow.pack(side=LEFT)
#         self.button_green.pack(side=LEFT)
#         self.button_light_blue.pack(side=LEFT)
#         self.button_blue.pack(side=LEFT)
#         self.button_purple.pack(side=LEFT)

#     def color_button_red(self):
#         self.lab['text'] = 'Red'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_red['bg'])

#     def color_button_orange(self):
#         self.lab['text'] = 'Orange'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_orange['bg'])

#     def color_button_yellow(self):
#         self.lab['text'] = 'Yellow'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_yellow['bg'])

#     def color_button_green(self):
#         self.lab['text'] = 'Green'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_green['bg'])

#     def color_button_light_blue(self):
#         self.lab['text'] = 'Light blue'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_light_blue['bg'])

#     def color_button_blue(self):
#         self.lab['text'] = 'Blue'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_blue['bg'])

#     def color_button_purple(self):
#         self.lab['text'] = 'Purple'
#         self.text.delete(0,END)
#         self.text.insert(0,self.button_purple['bg'])

# root = Tk()
# color = Color(root)
# root.mainloop()

# Text - многострочное текстовое поле

# class File_reader:
#     def __init__(self, root):
#         self.up_frame = Frame(root)
#         self.file_name_input = Entry(self.up_frame, width=20)
#         self.button_open = Button(self.up_frame,text='Open', command=self.open_file)
#         self.button_save = Button(self.up_frame,text='Save', command=self.save_file)
#         self.down_frame = Frame(root)
#         self.text = Text(self.down_frame)
#         self.scroller = Scrollbar(self.down_frame, command=self.text.yview)

#         self.up_frame.pack(side=TOP)
#         self.file_name_input.pack(side=LEFT)
#         self.button_open.pack(side=LEFT)
#         self.button_save.pack(side=LEFT)
#         self.down_frame.pack(side=TOP)
#         self.text.pack(side=LEFT)
#         self.scroller.pack(side=LEFT, fill=Y)
#         self.text['yscrollcommand'] = self.scroller.set

#     def open_file(self):
#         file1 = open(self.file_name_input.get(), 'r')
#         i = 1
#         self.text.delete(1.0, END)
#         for j in file1:
#             self.text.insert(float(i), j)
#             i += 1
#         file1.close()

#     def save_file(self):
#         file1 = open(self.file_name_input.get(), 'w')
#         file1.writelines(self.text.get(1.0, END))
#         file1.close()
        
# root = Tk()
# main_window = File_reader(root)
# root.mainloop()

# Radiobutton и Checkbutton. Переменные Tkinter

# class Book_users:
#     def __init__(self,root):
#         self.frame_1 = Frame(root)
#         self.radio_var = IntVar()
#         self.radio_var.set(0)

#         self.radiobutton_1 = Radiobutton(text='Vasy', variable=self.radio_var, value='0', indicatoron=0, command=self.radiobutton_active)
#         self.radiobutton_2 = Radiobutton(text='Pety', variable=self.radio_var, value='1', indicatoron=0, command=self.radiobutton_active)
#         self.radiobutton_3 = Radiobutton(text='Masha', variable=self.radio_var, value='2', indicatoron=0, command=self.radiobutton_active)
#         self.lab = Label(self.frame_1, text='...')
#         self.radiobutton_active()

#         self.radiobutton_1.pack(side=TOP)
#         self.radiobutton_2.pack(side=TOP)
#         self.radiobutton_3.pack(side=TOP)
#         self.frame_1.pack(side=LEFT)
#         self.lab.pack()

#     def radiobutton_active(self):
#         if self.radio_var.get() == 0:
#             self.lab['text'] = '+380950000000'
#         elif self.radio_var.get() == 1:
#             self.lab['text'] = '+380950000001'
#         elif self.radio_var.get() == 2:
#             self.lab['text'] = '+380950000002'

# root = Tk()
# window = Book_users(root)
# root.mainloop()

# Checkbutton

# class Checkbutton_user:
#     def __init__(self, root):
#         self.variable_ckeck = BooleanVar()
#         self.variable_ckeck.set(0)

#         self.checkbutton_1 = Checkbutton(root, text='Information', variable=self.variable_ckeck, onvalue=1, offvalue=0, command=self.information)
#         self.lab = Label(root, text='')

#         self.checkbutton_1.pack()
#         self.lab.pack()
#     def information(self):
#         if self.variable_ckeck.get() == 1:
#             self.lab['text'] = 'Worked'
#         else:
#             self.lab['text'] = ''

# root = Tk()
# window = Checkbutton_user(root)
# root.mainloop()

# Виджет Listbox

# class Listboxs:
#     def __init__(self, root):
#         self.listbox_1 = Listbox(width=15, height=8, selectmod=EXTENDED)
#         self.listbox_2 = Listbox(width=15, height=8, selectmod=EXTENDED)
#         self.frame_center = Frame(root)
#         self.button_1 = Button(self.frame_center, text='>>>', command=self.left_in_right_list)
#         self.button_2 = Button(self.frame_center, text='<<<', command=self.right_in_left_list)

#         self.listbox_1.pack(side=LEFT)
#         self.frame_center.pack(side=LEFT)
#         self.button_1.pack()
#         self.button_2.pack()
#         self.listbox_2.pack(side=LEFT)

#         for i in range(10):
#             self.listbox_1.insert(END, str(i))

#     def left_in_right_list(self):
#         select_listbox_1 = self.listbox_1.curselection()
#         for i in select_listbox_1:
#             self.listbox_2.insert(END, self.listbox_1.get(i))
#             self.listbox_1.delete(i)

#     def right_in_left_list(self):
#         select_listbox_2 = self.listbox_2.curselection()
#         for i in select_listbox_2:
#             self.listbox_1.insert(END, self.listbox_2.get(i))
#             self.listbox_2.delete(i)
        
# root = Tk()
# window = Listboxs(root)
# root.mainloop()

# Метод bind

# class Input_text:
#     def __init__(self, root):
#         self.entry = Entry(root, width=20)
#         self.listbox_1 = Listbox(width=25, height=8)

#         self.entry.pack()
#         self.listbox_1.pack()

#         self.entry.bind('<Return>', self.enter_button)
#         self.listbox_1.bind('<Double-Button-1>', self.copy_row)
#     def enter_button(self, event):
#         if self.entry.get().strip():
#             self.listbox_1.insert(END, self.entry.get().strip())
#             self.entry.delete(0,END)
#     def copy_row(self,event):
#         select = self.listbox_1.curselection()[0]
#         self.entry.delete(0,END)
#         self.entry.insert(0, self.listbox_1.get(select))

# root = Tk()
# window = Input_text(root)
# root.mainloop()

# События

# class Event_window:
#     def __init__(self, root):
#         self.frame_up = Frame(root)
#         self.frame_down = Frame(root)
#         self.frame_1 = Frame(self.frame_up)
#         self.frame_2 = Frame(self.frame_up)
#         self.entry_1 = Entry(self.frame_1)
#         self.entry_2 = Entry(self.frame_1)
#         self.button_1 = Button(self.frame_2, text='Change', command=self.size_change_button)
#         self.text_1 = Text(root, bg='#808080')

#         self.frame_up.pack()
#         self.frame_down.pack()
#         self.frame_1.pack(side=LEFT)
#         self.frame_2.pack(side=LEFT)
#         self.entry_1.pack()
#         self.entry_2.pack()
#         self.button_1.pack()
#         self.text_1.pack(side=TOP)

#         self.entry_1.bind('<Return>', self.size_change)
#         self.entry_2.bind('<Return>', self.size_change)
#         self.text_1.bind('<FocusIn>', self.focus_text)
#         self.text_1.bind('<FocusOut>', self.non_focus_text)

#     def size_change(self, event):
#         try:
#             self.text_1['width'] = self.entry_1.get()
#             self.text_1['height'] = self.entry_2.get()
#         except:
#             self.text_1['width'] = 20
#             self.text_1['height'] = 7

#     def focus_text(self, event):
#         self.text_1['bg'] = '#FFFFFF'

#     def non_focus_text(self, event):
#         self.text_1['bg'] = '#808080'

#     def size_change_button(self):
#         try:
#             self.text_1['width'] = self.entry_1.get()
#             self.text_1['height'] = self.entry_2.get()
#         except:
#             self.text_1['width'] = 20
#             self.text_1['height'] = 7

# root = Tk()
# window = Event_window(root)
# root.mainloop()

# Canvas

# class Picture:
#     def __init__(self, root):
#         self.canvas_for_picture = Canvas(root, width=180, height=115)
#         self.canvas_for_picture.pack()

#         self.canvas_for_picture.create_rectangle(45,105,115,55, fill='#00BFFF', outline='#00BFFF')
#         self.canvas_for_picture.create_polygon((30,55), (130,55), (80,15), fill='#00BFFF')
#         self.canvas_for_picture.create_oval(125,5,155,35, width=1, fill='#FF8000', outline='#FF8000')
#     def paint_the_grass(self):
#         for i in range(20):
#             x1 = i * 10
#             x2 = i * 10 + 15
#             self.canvas_for_picture.create_line(x1, 120, x2, 90, fill='#00FF00')

# root = Tk()
# window = Picture(root)
# window.paint_the_grass()
# root.mainloop()

# Canvas. Идентификаторы, теги и анимация

# class Animation_figures:
#     def __init__(self, root):
#         self.canvas_1 = Canvas(root, width=500, height=300)
#         self.canvas_1.focus_set()
#         self.canvas_1.pack()
#         self.circle = self.canvas_1.create_oval(50,10,150,110)
#         self.circle_coords = self.canvas_1.coords(self.circle)
#         self.x = 10
#         self.canvas_1.bind('<space>', self.circle_move_right)
#         self.canvas_1.bind('<Button-1>', self.circle_move_button)
#     def circle_move_right(self, event):
#         self.canvas_1.move(self.circle, self.x, 0)
#         self.circle_coords = self.canvas_1.coords(self.circle)
#         if self.circle_coords[2] >= 500:
#             self.canvas_1.coords(self.circle, 50, 10, 150, 110)
#     def circle_move_button(self, event):
#         x_mouse = event.x
#         y_mouse = event.y
#         self.circle_coords = self.canvas_1.coords(self.circle)
#         x_circle = int((self.circle_coords[0] + self.circle_coords[2]) / 2)
#         y_circle = int((self.circle_coords[1] + self.circle_coords[3]) / 2)
#         x = 0
#         y = 0

#         while True:
#             if x_mouse == x_circle and y_mouse == y_circle:
#                 break

#             if x_mouse > x_circle:
#                 x = 1
#             elif x_mouse == x_circle:
#                 x = 0
#             else:
#                 x = -1

#             if y_mouse > y_circle:
#                 y = 1
#             elif y_mouse == y_circle:
#                 y = 0
#             else:
#                 y = -1

#             self.canvas_1.after(100, lambda x=x, y=y: self.canvas_1.move(self.circle, x, y))
#             x_circle += x
#             y_circle += y

# root = Tk()
# window = Animation_figures(root)
# root.mainloop()