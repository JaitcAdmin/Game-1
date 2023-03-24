from attack import Attack
import time
from tkinter import *


class Bullet(Attack):
    def __init__(self, x, y, fps, g, dir_x, dir_y, walls):
        Attack.__init__(self, x, y, fps)
        self.x = x
        self.walls = walls
        self.y = y
        self.dir_x = dir_x
        self.g = g
        self.dir_y = dir_y
        self.frame = 0
        self.frame_exp = 0
        self.over = False
        self.canvas = g.canvas
        self.tk = g.canvas
        self.IsWorkOut = False
        self.time = time.time()
        self.none_image = PhotoImage(file="D://Python//Games//Game 1//assets//Option//none.png")
        self.images_exp = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//31.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//32.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//33.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//34.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//35.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//36.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//37.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//38.png")
        ]
        self.images_fly_left = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//51.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//52.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//53.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//54.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//55.png")
        ]
        self.images_fly_right = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//61.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//62.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//63.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//64.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Attack//65.png")
        ]
        if self.dir_x >= 0:
            self.image = self.canvas.create_image(self.x, self.y, image=self.images_fly_left[0], anchor=S)
        else:
            self.image = self.canvas.create_image(self.x, self.y, image=self.images_fly_right[0], anchor=S)

    def animate(self):
        if not self.IsWorkOut or self.frame != 0:
            if self.frame <= len(self.images_fly_left) - 1:
                if self.dir_x >= 0:
                    self.canvas.itemconfig(self.image, image=self.images_fly_left[self.frame])
                else:
                    self.canvas.itemconfig(self.image, image=self.images_fly_right[self.frame])
                self.frame += 1
            else:
                self.frame = 0
        if self.IsWorkOut and self.frame == 0:
            if self.frame_exp <= len(self.images_exp) - 1:
                self.dir_x = 0
                self.dir_y = 0
                self.canvas.itemconfig(self.image, image=self.images_exp[self.frame_exp])
                self.frame_exp += 1
            else:
                self.canvas.itemconfig(self.image, image=self.none_image)
                self.over = True
                self = None

    def move(self):
        if self.walls[int((self.y + self.dir_y) / 60)][int((self.x + self.dir_x) / 60)] == 4 or \
                self.walls[int((self.y - self.dir_y) / 60)][int((self.x - self.dir_x) / 60)] == 4:
            self.IsWorkOut = True
        print(self.x)
        if self.walls[int((self.y + self.dir_y) / 60)][int((self.x + self.dir_x) / 60)] != 4:
            self.x += self.dir_x
            self.y += self.dir_y
            self.canvas.move(self.image, self.dir_x, self.dir_y)
        if self.time <= time.time() - 0.025:
            self.animate()
            self.time = time.time()
