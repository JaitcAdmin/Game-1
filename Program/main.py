from tkinter import *
import time
from tkinter import messagebox
from knight import Knight
from map import Map
from Logo import Logo
import random


class Main:
    def __init__(self):
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.FPS = 60
        self.tk = Tk()
        self.tk.title("Assault of Desert")
        self.tk.attributes("-topmost", True)
        self.tk.attributes('-fullscreen', True)
        self.tk.resizable(0, 0)
        self.canvas = Canvas(self.tk, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        self.t = time.time()

        self.sprite = []
        self.walls = [
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4],
            [4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 0, 4, 0, 0, 4, 4, 0, 4, 4, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 0, 4, 4, 0, 4, 0, 0, 4, 0, 4, 0, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 0, 0, 0, 0, 4, 0, 4, 4, 0, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 4, 4, 0, 4, 4, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 0, 0, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 2, 3, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 0, 0, 0, 0, 0, 4, 0, 4, 4, 4, 4, 4, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 0, 4, 4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0, 3, 0, 0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 4, 4, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
        ]
        self.FullEnd = False
        self.images = [PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\1.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m2.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m3.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m4.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Walls\\2.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\1.png")]
        self.marichuana = [
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d11.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d12.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d20.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d159.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d139.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d140.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d162.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d164.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Decorations\\d127.png")
        ]

    def full_end(self):
        self.FullEnd = True

    def mainloop(self):
        i = -1
        while not self.FullEnd:
            i += 1
            # if time.time() - self.t >= 100000000000000:
            #    self.sprite[0].die()
            #    for i in range(0, len(self.sprite[0].health)):
            #       self.sprite[0].health.pop(i)
            if len(self.sprite) >= 1:
                if not self.sprite[i].end:
                    self.sprite[i].move()
            if i >= len(self.sprite) - 1:
                i = -1
            if self.tk is not None:
                self.tk.update()
                self.tk.update_idletasks()
                time.sleep(1 / self.FPS)

    def draw(self):
        self.atp_image = PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Option\\fon.png")
        self.apt = self.canvas.create_image(0, 840, image=self.atp_image, anchor=NW)
        for x in range(0, 32):
            for y in range(0, 14):
                self.canvas.create_image(x * 60, y * 60, image=self.images[self.walls[y][x]], anchor=NW)
        for x in range(0, 32):
            for y in range(0, 14):
                if int(random.random() * 20) == 9 and self.walls[y][x] != 4:
                    self.canvas.create_image(x * 60, y * 60,
                                             image=self.marichuana[int(random.random() * len(self.marichuana))],
                                             anchor=NW)

    def load(self):
        print("Начало сохранения")
        time.sleep(2)  # To Do#
        print("Загруска завершина")


try:
    m = Main()
    map = Map(m, m.FPS)
    print(map.mapa)
    print("\n" * 5)
    print(m.walls)
    m.walls = map.mapa
    m.draw()git 
    for x in range(0, 32):
        for y in range(0, 14):
            if m.walls[y][x] == 5:
                k1 = Knight(x * 60 + 25, y * 60 + 25, 1, 0, m.FPS, m, 5, m.walls, 10)
    if k1 is None:
        k1 = Knight(1200, 400, 1, 0, m.FPS, m, 5, m.walls, 10)

    m.sprite.append(k1)


    def motion1(event):
        if event.y <= 840:
            k1.create_purpose(event.x, event.y)
            print("c")


    def motion2(event):
        if event.x >= k1.x:
            k1.atc_dir = 1
        elif event.x <= k1.x:
            k1.atc_dir = -1
        k1.attack()


    m.tk.bind('<Button-1>', motion1)
    m.tk.bind('<Button-3>', motion2)
    m.tk.bind('<Escape>', lambda e: m.tk.destroy())
    m.mainloop()
except TclError:
    exit(2)
else:
    ms = messagebox
    ms.showerror("Пиратская техналогия!",
                 ("Зафиксирована попытка исследования \n" +
                  " программы или её служебных данных! \n" +
                  " Любознательным народным умельцам \n" +
                  " и даже будущему программисту Васе, \n" +
                  " рекомендуется бросить эту вонючую \n"
                  " затею и позвони на телефон поддержки!!!"))

#Hello GitHub
