from tkinter import *

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