from my_modules import win_door
from math import ceil

class Room:
    """Class room"""
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.wd = []
        self.list_weight = []
    def add_win_door(self,w,h):
        """Function for add windows and doors"""
        self.wd.append(win_door.Win_door(w,h))
    def work_surface(self):
        new_square = self.square_for_use
        for i in self.wd:
            new_square -= i.square
        return new_square
    def change_size(self,x,y,z):
        """Function for change size"""
        """And save weight"""
        self.x = x
        self.y = y
        self.z = z
        self.save_weight()
    def save_weight(self):
        self.list_weight.append([self.x,self.y])
    def calculate_squere(self):
        self.square = 2*self.z*(self.x+self.y)
        self.square_for_use = self.square
    def number_of_rolls(self,x,y):
        """Return result square"""
        return ceil(self.square_for_use / (x*y))