# --------------------------------------
# Development start date: 23 Apr 2021
# --------------------------------------

from tkinter import *

# App main window
root = Tk()
root.geometry("235x328")
root.title('Calculator')

# Class for realization calculator interface and functionality
class Calculator:
    def __init__(self, root):

        # List have operators and numbers from buttons
        self.main_list = []

        # Input and output field
        self.entry_main = Entry(root, width=35)
        self.entry_main.grid(row=0,column=0,pady=5,ipady=10, columnspan=4)

        # Buttons for calculator
        Button(root, text='1', width=7, height=3, command=lambda: self.add_in_list('1')).grid(column=0, row=1)
        Button(root, text='2', width=7, height=3, command=lambda: self.add_in_list('2')).grid(column=1, row=1)
        Button(root, text='3', width=7, height=3, command=lambda: self.add_in_list('3')).grid(column=2, row=1)
        Button(root, text='+', width=7, height=3, command=lambda: self.add_in_list('+')).grid(column=3, row=1)
        Button(root, text='4', width=7, height=3, command=lambda: self.add_in_list('4')).grid(column=0, row=2)
        Button(root, text='5', width=7, height=3, command=lambda: self.add_in_list('5')).grid(column=1, row=2)
        Button(root, text='6', width=7, height=3, command=lambda: self.add_in_list('6')).grid(column=2, row=2)
        Button(root, text='-', width=7, height=3, command=lambda: self.add_in_list('-')).grid(column=3, row=2)
        Button(root, text='7', width=7, height=3, command=lambda: self.add_in_list('7')).grid(column=0, row=3)
        Button(root, text='8', width=7, height=3, command=lambda: self.add_in_list('8')).grid(column=1, row=3)
        Button(root, text='9', width=7, height=3, command=lambda: self.add_in_list('9')).grid(column=2, row=3)
        Button(root, text='*', width=7, height=3, command=lambda: self.add_in_list('*')).grid(column=3, row=3)
        Button(root, text='.', width=7, height=3, command=lambda: self.add_in_list('.')).grid(column=0, row=4)
        Button(root, text='0', width=7, height=3, command=lambda: self.add_in_list('0')).grid(column=1, row=4)
        Button(root, text='=', width=7, height=3, command=self.equally).grid(column=2, row=4)
        Button(root, text='/', width=7, height=3, command=lambda: self.add_in_list('/')).grid(column=3, row=4)
        Button(root, text='C', width=7, height=3, command=self.clear).grid(column=0, row=5)
        Button(root, text='(', width=7, height=3, command=lambda: self.add_in_list('(')).grid(column=1, row=5)
        Button(root, text=')', width=7, height=3, command=lambda: self.add_in_list(')')).grid(column=2, row=5)
        Button(root, text='<', width=7, height=3, command=self.delete_last_symbol).grid(column=3, row=5)

    # Add numbers and operators to main list
    def add_in_list(self, value):
        if self.check_sym(value):
            self.main_list.append(value)
            self.set_list_in_entry()
    
    # Output data in entry
    def set_list_in_entry(self):
        self.entry_main.delete(0, END)
        self.entry_main.insert(0, ''.join(self.main_list))

    # Check for duplicate operators
    def check_sym(self, value):
        list_symbols = ['+','-','*','/','.']
        if value in list_symbols and self.main_list[-1] in list_symbols:
            return False
        return True

    # Equally
    def equally(self):
        answer = eval(''.join(self.main_list))
        del self.main_list
        self.main_list = list(str(answer))
        self.set_list_in_entry()

    # Clear main entry
    def clear(self):
        self.main_list = []
        self.set_list_in_entry()

    # Delete last symbol
    def delete_last_symbol(self):
        del self.main_list[-1]
        self.set_list_in_entry()

calculator = Calculator(root)

root.mainloop()