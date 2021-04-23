from tkinter import *

# App main window
root = Tk()
root.geometry("250x300")

# Input and output field
entry_main = Entry(root, width=35)
entry_main.grid(row=0,column=0,pady=5,ipady=10, columnspan=4)

# Buttons for calculator
Button(root, text='1', width=7, height=3).grid(column=0, row=1)
Button(root, text='2', width=7, height=3).grid(column=1, row=1)
Button(root, text='3', width=7, height=3).grid(column=2, row=1)
Button(root, text='+', width=7, height=3).grid(column=3, row=1)
Button(root, text='4', width=7, height=3).grid(column=0, row=2)
Button(root, text='5', width=7, height=3).grid(column=1, row=2)
Button(root, text='6', width=7, height=3).grid(column=2, row=2)
Button(root, text='-', width=7, height=3).grid(column=3, row=2)
Button(root, text='7', width=7, height=3).grid(column=0, row=3)
Button(root, text='8', width=7, height=3).grid(column=1, row=3)
Button(root, text='9', width=7, height=3).grid(column=2, row=3)
Button(root, text='*', width=7, height=3).grid(column=3, row=3)
Button(root, text='.', width=7, height=3).grid(column=0, row=4)
Button(root, text='0', width=7, height=3).grid(column=1, row=4)
Button(root, text='=', width=7, height=3).grid(column=2, row=4)
Button(root, text='/', width=7, height=3).grid(column=3, row=4)

root.mainloop()