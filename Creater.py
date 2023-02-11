from tkinter import *
import numpy as np

global color
color = 1


def get_grass():
    global color
    color = 0


def get_send():
    global color
    color = 1


def get_snow():
    global color
    color = 2


def get_lava():
    global color
    color = 3


def save(w):
    a = " "
    for i in w:
        a += "["
        for y in range(0, len(i)):
            a += str(i[y])
            if y <= len(i) - 2:
                a += ", "
        a += "] "
    with open("D:\\Python\\Games\\Game 1\\Maps\\number.txt", "r") as f:
        num = int(f.read())
        with open(f"D:\\Python\\Games\\Game 1\\Maps\\{num + 1}.txt", "w") as u:
            u.write(a)
        with open("D:\\Python\\Games\\Game 1\\Maps\\number.txt", "w") as k:
            k.write(str(num + 1))



def maps(nom):
    file = open(F"D:\\Python\\Games\\Game 1\\Maps\\{nom}.txt", "r")
    a = file.read()
    b = []
    for i in a:
        if i != "]" and i != "[" and i != " " and i != ",":
            b.append(i)
    file.close()
    return b


def make(list, w):
    a = np.array(list)
    arr = np.reshape(a, (-1, w))
    arr2 = arr.tolist()
    arr3 = []
    for i in range(0, len(arr2)):
        for y in range(0, len(arr2[i])):
            arr2[i][y] = int(arr2[i][y])
    return arr2


def draw(canvas, walls, images):
    canvas.create_image(0, 840, image=fon, anchor=NW)
    for x in range(0, len(walls)):
        for y in range(0, len(walls[x])):
            canvas.create_image(y * 60, x * 60, image=images[walls[x][y]], anchor=NW)
    for x in range(0, len(walls)):
        for y in range(0, len(walls[x])):
            canvas.create_line(y * 60, 0, y * 60, 840)
            canvas.create_line(0, x * 60, 1920, x * 60)


def change(event):
    print(len(walls))
    for i in range(0, len(walls)):
        for j in range(0, len(walls[i])):
            if event.x >= j * 60 and event.x <= (j * 60) + 60 and event.y >= i * 60 and event.y <= (i * 60) + 60:
                walls[i][j] = 1
                canvas.create_image(j * 60, i * 60, image=images[color], anchor=NW)
                canvas.create_line(j * 60, 0, j * 60, 840)
                canvas.create_line(0, i * 60, 1920, i * 60)


tk = Tk()
tk.attributes("-topmost", True)
tk.attributes('-fullscreen', True)
canvas = Canvas(tk, width=1920, height=1080)
canvas.pack()
fon = PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Option\\fon.png")

with open("D:\\Python\\Games\\Game 1\\Maps\\number.txt", "r") as f:
    num = int(f.read())
    walls = make(maps(num), 32)

for x in range(0, len(walls)):
    for y in range(0, len(walls[x])):
        walls[x][y] = 0

images = [
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\1.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m2.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m3.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m4.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Walls\\2.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\6.png")
]

tk.bind_all("<Button-1>", change)

draw(canvas, walls, images)
btn = [
    Button(tk, text="Трава", command=lambda: get_grass()),
    Button(tk, text="Песок", command=lambda: get_send()),
    Button(tk, text="Снег", command=lambda: get_snow()),
    Button(tk, text="Лава", command=lambda: get_lava()),
    Button(tk, text="Сохранить", command=lambda: save(walls))
]
for i in range(470, len(btn) * 200 + 470, 200):
    btn[int((i - 470) / 200)].place(x=i, y=950)
tk.mainloop()
