import time
from tkinter import *

from sprite import Sprite


class Logo(Sprite):
    def __init__(self, g, fps):
        Sprite.__init__(self, fps)
        self.frames = [
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f4.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f4.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f4.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f4.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f5.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f6.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f7.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f8.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f9.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f10.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f11.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f12.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f13.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f14.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f15.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f16.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f17.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f18.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f19.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f20.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f21.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f22.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f23.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f24.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f25.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f26.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f27.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f28.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f29.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f30.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f31.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f32.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f33.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f34.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f35.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f36.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f37.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f38.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f39.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f40.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f41.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f42.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f43.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f44.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\f45.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\1.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\2.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\3.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\4.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\5.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\6.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\7.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\8.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\9.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\10.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\11.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\12.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\13.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\14.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\15.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\16.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\17.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\18.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\19.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\20.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\21.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\22.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\23.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\24.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\25.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\26.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Logo\\Start Logo\\StartExplosion\\27.png")

        ]
        self.end = False
        self.frame = 0
        self.g = g
        self.time = time.time()
        self.rec = self.g.canvas.create_rectangle(0, 0, 1920, 1080, fill="black")
        self.image = self.g.canvas.create_image(550, 0, image=self.frames[self.frame], anchor=NW)

    def animate(self):
        if time.time() >= self.time + 0.06 and self.frame <= len(self.frames) - 1:
            self.frame += 1
            self.time = time.time()
        self.g.canvas.itemconfig(self.image, image=self.frames[self.frame])
        if self.frame == 43:
            print("aaa")
            self.rec = self.g.canvas.create_rectangle(0, 0, 1920, 1080, fill="white")
            self.image = self.g.canvas.create_image(0, 0, image=self.frames[self.frame], anchor=NW)
        if self.frame == len(self.frames) - 1:
            self.end = True
            self.g.canvas.create_rectangle(0, 0, 1920, 1080, fill="white")
            print("a")

    def move(self):
        if not self.end:
            self.animate()

    def is_end(self):
        return self.end
