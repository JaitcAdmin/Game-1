from tkinter import *
import pickle
from Program.map import Map
from tkinter import messagebox as ms

global color
color = 5
global lives
lives = 10
global name
name = ""
global bol
bol = True


def get_lives():
    global lives
    lives = int(en1.get())
    print(f"lives = {lives}")


def get_name():
    global name
    name = en2.get()
    tk.title(name)
    print(f"name = {name}")


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


def get_brick():
    global color
    color = 4


def get_spawnpoint(bol1=bol):
    global color
    color = 5
    btn[6].place(x=2000, y=2000)
    walls[0][0] = 4


def save(w):
    a = " "
    for i in w:
        a += "["
        for y in range(0, len(i)):
            a += str(i[y])
            if y <= len(i) - 2:
                a += ", "
        a += "] "
    walls[0][0] = 4
    draw(canvas, walls, images)
    m = Map(3)
    m.walls = walls
    m.health = lives
    m.name = name
    k = open(f"D:\\Python\\Games\\Game 1\\Maps\\number.txt", "r")
    add = int(k.read())
    print(F"add = {add}")
    add += 1
    k.close()
    f = open(f"D:\\Python\\Games\\Game 1\\Maps\\number.txt", "w")
    f.write(str(add))
    f.close()

    with open(f"D:\\Python\\Games\\Game 1\\Maps\\map_{num + 1}", "wb") as f:
        pickle.dump(m, f)

    ms.askyesno("Program", "Save is complate!Will you wont exit from program?", command=tk.destroy())

def make(nom):
    with open(f"D:\\Python\\Games\\Game 1\\Maps\\map_{nom}", "rb") as f:
        m = pickle.load(f)
    return m


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
    if event.y <= 780 and event.y >= 60 and event.x >= 60 and event.x <= 1860:
        for i in range(0, len(walls)):
            for j in range(0, len(walls[i])):
                if event.x >= j * 60 and event.x <= (j * 60) + 60 and event.y >= i * 60 and event.y <= (i * 60) + 60:
                    walls[i][j] = color
                    if color == 5:
                        canvas.create_image(j * 60 + 90, i * 60 + 60, image=images[5], anchor=SE)
                        get_grass()
                    else:
                        canvas.create_image(j * 60, i * 60, image=images[color], anchor=NW)
                    canvas.create_line(j * 60, 0, j * 60, 840)
                    canvas.create_line(0, i * 60, 1920, i * 60)


tk = Tk()
tk.attributes("-topmost", True)
tk.attributes('-fullscreen', True)
canvas = Canvas(tk, width=1920, height=1080)
canvas.pack()
fon = PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Option\\fon.png")

f = open("D:\\Python\\Games\\Game 1\\Maps\\number.txt", "r")
num = int(f.read())
m = make(num)
walls = m.walls
print(f.read())

for x in range(0, len(walls)):
    for y in range(0, len(walls[x])):
        walls[x][y] = 4
for x in range(1, len(walls) - 1):
    for y in range(1, len(walls[x]) - 1):
        walls[x][y] = 0

images = [
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\1.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m2.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m3.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m4.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Walls\\2.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m6.png")
]

tk.bind_all("<Button-1>", change)
tk.bind('<Escape>', lambda e: tk.destroy())

draw(canvas, walls, images)
btn = [
    Button(tk, text="Трава", command=lambda: get_grass()),
    Button(tk, text="Песок", command=lambda: get_send()),
    Button(tk, text="Снег", command=lambda: get_snow()),
    Button(tk, text="Лава", command=lambda: get_lava()),
    Button(tk, text="Стена", command=lambda: get_brick()),
    Button(tk, text="Название", command=lambda: get_name()),
    Button(tk, text="Спавн поинт", command=lambda: get_spawnpoint()),
    Button(tk, text="Кол-во жизней", command=lambda: get_lives()),
    Button(tk, text="Сохранить", command=lambda: save(walls))
]
en1 = Entry()
en1.place(anchor=NW, x=1533, y=900)
en2 = Entry()
en2.place(anchor=NW, x=1118, y=900)
for i in range(150, len(btn) * 200 + 150, 200):
    btn[int((i - 150) / 200)].place(x=i, y=1000)
f.close()
tk.mainloop()
