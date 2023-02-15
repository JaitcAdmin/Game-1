from tkinter import *
import time
from tkinter import messagebox
from knight import Knight
from map import Map
import pickle


class Main:
    def __init__(self, level):
        self.level = level
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.FPS = 60
        self.tk = Tk()
        self.tk.title(f"Level: {self.level}")
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
        self.grass = [
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
        with open(f"D:\\Python\\Games\\Game 1\\Maps\\map_{self.level}", "rb") as c:
            m = pickle.load(c)
            self.lives = m.health
            self.walls = m.walls
            print(m.grasss)
            self.grass = m.grass
            print(m.grass)

        self.FullEnd = False
        self.images = [PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\1.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m2.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m3.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m4.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Walls\\2.png"),
                       PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\1.png")]
        self.plant = [
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
                print(self.grass[y][x])
                if self.grass[y][x] != 0:
                    self.canvas.create_image(x * 60, y * 60, image=self.plant[self.grass[y][x]], anchor=NW)

    def load(self):
        print("Начало сохранения")
        time.sleep(2)  # To Do #
        print("Загруска завершина")


try:
    m = Main(2)
    m.draw()
    k1 = Knight(60, 60, 1, 0, m.FPS, m, 5, m.walls, m.lives)

    for x in range(0, 32):
        for y in range(0, 14):
            if m.walls[y][x] == 5:
                k1 = Knight(x * 60 + 25, y * 60 + 25, 1, 0, m.FPS, m, 5, m.walls, m.lives)
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

# Hello GitHub
