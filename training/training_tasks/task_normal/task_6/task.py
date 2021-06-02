import random
import tkinter

coord = [random.randint(0, 300), random.randint(0, 300), random.randint(0, 300), random.randint(0, 300)]

try:
    x = int(input())
    y = int(input())
except:
    print('Error')
    exit()

root = tkinter.Tk()
root.geometry("300x300")
canvas = tkinter.Canvas(root, width=300, height=300)
canvas.pack()

canvas.create_rectangle(coord[0], coord[1], coord[2], coord[3], fill='green')

canvas.create_oval(x, y, x+10, y+10, width=1, fill='red')

if x in range(coord[0], coord[2]) and y in range(coord[1], coord[3]):
    print('Win')
else:
    print('Lose')

root.mainloop()