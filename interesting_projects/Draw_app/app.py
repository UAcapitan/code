import tkinter as tk

root = tk.Tk()
root.geometry("300x370")
root.title("Paint app")

color = '#00FF00'
draw = False

cnv = tk.Canvas(root, bg="white", height=300, width=300)
cnv.place(x=0, y=0)
f1 = tk.Text(root, height=1, width=10)
f1.place(x=90, y=310)

def change_color():
    global color
    color = f1.get('1.0', tk.END)[0:7]
    cnv_color.create_rectangle(0, 0, 20, 20, fill=color, outline='')
    print(color)

f_btn = tk.Button(text='Change', command=change_color)
f_btn.place(x=190, y=307)

def motion(event):
    if draw:
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))
        cnv.create_rectangle(x, y, x+5, y+5, fill=color, outline='')

def draw_flag(event):
    global draw
    if draw:
        draw = False
    else:
        draw = True
    print(draw)

cnv_color = tk.Canvas(root, bg="white", height=20, width=20)
cnv_color.place(x=50, y=308)
cnv_color.create_rectangle(0, 0, 20, 20, fill=color, outline='')

root.bind('<Motion>', motion)
root.bind('q', draw_flag)

root.mainloop()