from tkinter import *
from tkinter import messagebox as ms
import pickle
from tkinter.filedialog import askopenfile
from Program.map import Map

global Gwalls
Gwalls = []
global number
number = 0

tk = Tk()
canvas = Canvas(tk, width=1920, height=1080)
tk.bind('<Escape>', lambda e: tk.destroy())
canvas.pack()

color = 0


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
                    Gwalls[i][j] = color
                    canvas.create_image(j * 60, i * 60, image=plant[color], anchor=NW)
                    canvas.create_line(j * 60, 0, j * 60, 840)
                    canvas.create_line(0, i * 60, 1920, i * 60)


def load():
    walls = []
    try:
        a = make(int(en.get()))
        walls = a.walls
    except FileNotFoundError:
        ms.showerror("Program", f"Program have not file {en.get()}")
    global number
    number = int(en.get()) - 1
    draw(canvas, walls, images)


def aaaa(list, word, word2):
    a = ""
    for s in list:
        if s != word:
            a += s
        else:
            a += word2
    return a


def ag(w):
    a = ""
    for i in w:
        a += "["
        for y in range(0, len(i)):
            a += str(i[y])
            if y <= len(i) - 2:
                a += ", "
        a += "] "
    return a


def save1():
    if number != 0:
        w = open(f"D:\\Python\\Games\\Game 1\\Maps\\map_{number+1}", "rb")
        m = pickle.load(w)
        print(Gwalls)
        print(m.walls)
        m.set_grass(Gwalls)
        w.close()
        g = open(f"D:\\Python\\Games\\Game 1\\Maps\\map_{number+1}", "wb")
        pickle.dump(m, g)
        ms.askokcancel("Program", "Save is complenty")
        g.close()

fon = PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Option\\fon.png")

with open("D:\\Python\\Games\\Game 1\\Maps\\number.txt", "r") as f:
    num = int(f.read())
    a = make(num)
    walls = a.walls
    Gwalls = a.grass
for x in range(0, len(walls)):
    for y in range(0, len(walls[x])):
        walls[x][y] = 4
for x in range(0, len(walls)):
    for y in range(0, len(walls[x])):
        Gwalls[x][y] = 0
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
draw(canvas, walls, images)
plant = [
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d11.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d12.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d13.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d14.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d15.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d16.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d17.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d18.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d19.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d20.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d110.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d111.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d112.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d113.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d114.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d115.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d116.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d117.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d118.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d119.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d121.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d122.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d123.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d124.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d125.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d126.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d127.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d128.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d129.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d130.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d131.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d132.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d133.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d134.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d135.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d136.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d137.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d138.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d139.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d140.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d141.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d142.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d143.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d144.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d145.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d146.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d147.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d148.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d149.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d150.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d151.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d152.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d153.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d154.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d155.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d156.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d157.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d158.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d159.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d160.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d161.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d162.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d163.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d164.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d165.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d166.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d167.png"),
    PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d168.png")

]
pm = [
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d11.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d12.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d13.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d14.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d15.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d16.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d17.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d18.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d19.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d20.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d110.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d111.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d112.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d113.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d114.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d115.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d116.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d117.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d118.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d119.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d120.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d121.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d122.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d123.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d124.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d125.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d126.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d127.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d128.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d129.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d130.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d131.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d132.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d133.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d134.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d135.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d136.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d137.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d138.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d139.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d140.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d141.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d142.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d143.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d144.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d145.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d146.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d147.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d148.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d149.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d150.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d151.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d152.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d153.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d154.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d155.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d156.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d157.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d158.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d159.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d160.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d161.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d162.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d163.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d164.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d165.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d166.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d167.png",
    "D:\\Python\\Games\\Game 1\\assets\\Decorations\\d168.png"

]
draw(canvas, walls, images)


def file_selection():
    file = askopenfile(mode='r', filetypes=[('D:\\Python\\Games\\Game 1\\assets\\Decorations', '*.png')])
    if file is not None:
        iii = False
        content = str(file.name)
        for ij in range(0, len(pm)):
            if aaaa(pm[ij], "\\", "-") == aaaa(content, "/", "-"):
                global color
                color = ij
                iii = True
            else:
                if ij == len(pm) - 1 and not iii:
                    ms.showerror("Program", "Program have not this File")
                    content = ""
                    file_selection()


# file = filedialog.askopenfiles(title="Выбор файла", initialdir="D:\\Python\\Games\\Game 1\\assets\\Decorations")
# if file is not None:
#    content = file.read()
#    print(content)
tk.bind_all("<Button-1>", change)
btn1 = Button(text="Select", command=lambda: file_selection())
btn1.place(x=100, y=950)
btn2 = Button(text="Load", command=lambda: load())
btn2.place(x=540, y=950)
btn3 = Button(text="Save", command=lambda: save1())
btn3.place(x=740, y=950)
en = Entry()
en.place(x=500, y=900)
tk.mainloop()
