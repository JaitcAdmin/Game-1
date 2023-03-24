from tkinter import *
from enemy import Enemy
import time
import random


class Turrel(Enemy):
    def __init__(self, x, y, fps, g, dir):
        Enemy.__init__(self, fps, x, y, g.walls, g.canvas)
        self.x = x
        self.y = y
        self.dir = dir
        self.IsStart = False
        self.IsAttack = False
        self.ToBeStart = False
        self.FPS = fps
        self.t_attack = time.time()
        self.target_x = self.dir
        self.target_y = self.dir
        self.time = time.time()
        self.canvas = g.canvas
        self.tk = g.tk
        self.frame = 0
        self.images_start_right = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//0.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//11.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//12.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//13.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//14.png")
        ]
        self.images_start_left = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//01.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//31.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//32.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//33.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//34.png")
        ]
        self.images_attack_right = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//21.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//22.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//23.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//24.png")
        ]
        self.images_attack_left = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//41.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//42.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//43.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Mob//ZHero//ZTurrel//44.png")
        ]
        if dir >= 0:
            self.image = self.canvas.create_image(self.x + 15, self.y + 25, image=self.images_start_right[0], anchor=S)
        else:
            self.image = self.canvas.create_image(self.x + 15, self.y + 25, image=self.images_start_left[0], anchor=S)

    def animate(self):
        if not self.IsStart and self.time <= time.time() - 0.1 and self.ToBeStart:
            self.time = time.time()
            if self.dir <= 0:
                self.canvas.itemconfig(self.image, image=self.images_start_left[self.frame])
            if self.dir > 0:
                self.canvas.itemconfig(self.image, image=self.images_start_right[self.frame])
            self.frame += 1
            if self.frame >= len(self.images_start_right):
                self.frame = 0
                self.IsStart = True
        if self.IsAttack and self.IsStart and self.time <= time.time() - 0.02:
            self.time = time.time()
            self.t_attack = time.time()
            if self.dir >= 0:
                self.canvas.itemconfig(self.image, image=self.images_attack_right[self.frame])
            if self.dir < 0:
                self.canvas.itemconfig(self.image, image=self.images_attack_right[self.frame])
            self.frame += 1
            if self.frame >= len(self.images_attack_left):
                self.frame = 0
                self.IsAttack = False
                print("piu1")

    def move(self):
        self.animate()

    def new_data(self, x, y):
        self.target_x = x
        self.target_y = y
