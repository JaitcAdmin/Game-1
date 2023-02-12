from tkinter import *
from sprite import Sprite
import time


class Knight(Sprite):
    def __init__(self, x, y, dir_x, dir_y, fps, g, speed, map, health):
        Sprite.__init__(self, fps)
        self.ItAttack = False
        self.x = x
        self.y = y
        self.f = 6
        self.atc_dir = 0
        self.texture_heads = [PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Option\\h21.png"),
                              PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Option\\h22.png")]
        self.start_health = health
        self.map = map
        self.none = PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Option\\h0.png")
        self.health_nom = 1
        self.ItFire = False
        self.IsStartDie = False
        self.IsFullDie = False
        self.die_frame = 0
        self.atc_frame = 0
        self.time_fire = 0
        self.CoordOfPurpose = [0, 0]
        self.x_dir = dir_x
        self.y_dir = dir_y
        self.speed = speed
        self.g = g
        self.health = []
        self.start_health_line = 100
        self.finish_health_line = 580
        for i in range(self.start_health_line, self.finish_health_line,
                       int((self.finish_health_line - self.start_health_line) / health)):
            self.health.append(self.g.canvas.create_image(i, 960, image=self.texture_heads[0]))
            self.health_nom += 1
        self.ItStand = False
        self.stand_left = PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\111.png")

        self.image = g.canvas.create_image(self.x, self.y, image=self.stand_left)

        self.die_images = [
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\151.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\152.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\153.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\154.png"),
        ]

        self.attack_left = [
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\111.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\112.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\113.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\114.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\115.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\116.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\117.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\118.png")
        ]
        self.attack_right = [
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\121.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\122.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\123.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\124.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\125.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\126.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\127.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\128.png")
        ]
        self.run_left = [
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\131.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\132.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\133.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\134.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\135.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\136.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\137.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\138.png"),
        ]
        self.run_right = [
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\141.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\142.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\143.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\144.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\145.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\146.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\147.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Mob\\ZHero\\ZKnight\\148.png"),
        ]
        self.frame = 0
        self.time = time.time()

    def animate(self):
        if time.time() - self.time > 0.1 / self.fps:
            self.time = time.time()
            self.frame += 1
            self.atc_frame += 1
            if self.frame >= 7:
                self.frame = 0
            if self.atc_frame >= 28:
                self.atc_frame = 0
                if self.ItAttack:
                    self.ItAttack = False

        self.g.canvas.itemconfig(self.image, image=self.run_left[self.frame])
        if self.x_dir > 0:
            self.g.canvas.itemconfig(self.image, image=self.run_right[self.frame])

        if self.ItAttack and self.x_dir * self.speed < 0:
            self.g.canvas.itemconfig(self.image, image=self.attack_left[self.frame])
        if self.ItAttack and self.x_dir * self.speed > 0:
            self.g.canvas.itemconfig(self.image, image=self.attack_right[self.frame])

        if self.ItAttack and self.atc_dir * self.speed < 0:
            self.g.canvas.itemconfig(self.image, image=self.attack_left[int(self.frame / 4)])
        elif self.ItAttack and self.atc_dir * self.speed > 0:
            self.g.canvas.itemconfig(self.image, image=self.attack_right[int(self.frame / 4)])

        if int(self.x_dir * self.speed) == 0 and int(self.y_dir * self.speed) == 0:
            self.g.canvas.itemconfig(self.image, image=self.stand_left)

        if self.start_health / 2 >= self.health_nom and self.frame % self.f == 0:
            for i in self.health:
                self.g.canvas.itemconfig(i, image=self.texture_heads[1])
        if self.start_health / 2 >= self.health_nom and self.frame % self.f != 0:
            for i in self.health:
                self.g.canvas.itemconfig(i, image=self.texture_heads[0])
        if self.start_health / 2.5 >= self.health_nom:
            self.f = 4.444444444444444
        if self.start_health / 3 >= self.health_nom:
            self.f = 1.111111111111111

        if self.IsStartDie:
            self.g.canvas.itemconfig(self.image, image=self.die_images[3])
            if not self.IsFullDie:
                if time.time() - self.time <= 1:
                    self.die_frame += 1

                if self.die_frame <= 0:
                    self.g.canvas.itemconfig(self.image, image=self.die_images[0])
                elif self.die_frame == 1:
                    self.g.canvas.itemconfig(self.image, image=self.die_images[1])
                elif self.die_frame == 2:
                    self.g.canvas.itemconfig(self.image, image=self.die_images[2])
                elif self.die_frame >= 3:
                    self.g.canvas.itemconfig(self.image, image=self.die_images[3])

                if self.die_frame >= 8:
                    self.IsFullDie = True
        if self.ItAttack:
            if self.atc_dir < 0:
                if self.atc_frame <= 0:
                    self.g.canvas.itemconfig(self.image, image=self.attack_left[0])
                if self.atc_frame == 1:
                    self.g.canvas.itemconfig(self.image, image=self.attack_left[1])
                if self.atc_frame == 2:
                    self.g.canvas.itemconfig(self.image, image=self.attack_left[2])
                if self.atc_frame == 3:
                    self.g.canvas.itemconfig(self.image, image=self.attack_left[3])
                if self.atc_frame == 4:
                    self.g.canvas.itemconfig(self.image, image=self.attack_left[4])
                if self.atc_frame == 5:
                    self.g.canvas.itemconfig(self.image, image=self.attack_left[5])
                if self.atc_frame == 6:
                    self.g.canvas.itemconfig(self.image, image=self.attack_left[6])
                if self.atc_frame >= 7:
                    self.g.canvas.itemconfig(self.image, image=self.attack_left[7])
            if self.atc_dir >= 0:
                if self.atc_frame <= 0:
                    self.g.canvas.itemconfig(self.image, image=self.attack_right[0])
                if self.atc_frame == 1:
                    self.g.canvas.itemconfig(self.image, image=self.attack_right[1])
                if self.atc_frame == 2:
                    self.g.canvas.itemconfig(self.image, image=self.attack_right[2])
                if self.atc_frame == 3:
                    self.g.canvas.itemconfig(self.image, image=self.attack_right[3])
                if self.atc_frame == 4:
                    self.g.canvas.itemconfig(self.image, image=self.attack_right[4])
                if self.atc_frame == 5:
                    self.g.canvas.itemconfig(self.image, image=self.attack_right[5])
                if self.atc_frame == 6:
                    self.g.canvas.itemconfig(self.image, image=self.attack_right[6])
                if self.atc_frame >= 7:
                    self.g.canvas.itemconfig(self.image, image=self.attack_right[7])

    def move(self):
        self.animate()
        if self.x_dir * self.speed > 1:
            self.x_dir = 1
        if self.y_dir * self.speed > 1:
            self.y_dir = 1
        if self.x_dir * self.speed < -1:
            self.x_dir = -1
        if self.y_dir * self.speed < -1:
            self.y_dir = -1
        if self.health_nom <= 1:
            self.die()
        for x in range(0, 32):
            for y in range(0, 14):
                if not (not (y * 60 - 30 <= self.y + self.y_dir * self.speed <= y * 60 + 20) or not (
                        x * 60 - 10 <= self.x + self.x_dir * self.speed <= x * 60 + 70)) and \
                        self.map[y][x] == 4:
                    self.stop()
                if not (not (y * 60 - 15 <= self.y + self.y_dir * self.speed <= y * 60 + 30) or not (
                        x * 60 - 10 <= self.x + self.x_dir * self.speed <= x * 60 + 60)) and \
                        self.map[y][x] == 3:
                    if self.ItFire:
                        if time.time() - self.time_fire >= 1 and self.health_nom >= 2:
                            self.g.canvas.itemconfig(self.health[len(self.health) - 1],
                                                     image=self.none)
                            self.health_nom -= 1
                            self.health.pop(len(self.health) - 1)
                            self.time_fire = time.time()
                    else:
                        self.ItFire = True

        if not self.ItStand and self.atc_dir <= 8:
            self.g.canvas.move(self.image, self.x_dir * self.speed, self.y_dir * self.speed)
            self.x += self.x_dir * self.speed
            self.y += self.y_dir * self.speed

        if int(self.CoordOfPurpose[0]) - 10 < int(self.x) < int(self.CoordOfPurpose[0]) + 10:
            self.x_dir = 0
        if int(self.CoordOfPurpose[1]) - 10 < int(self.y) < int(self.CoordOfPurpose[1]) + 10:
            self.y_dir = 0
        if int(self.CoordOfPurpose[0]) - 10 < int(self.y < int(self.CoordOfPurpose[0]) + 10) and int(
                self.CoordOfPurpose[1]) - 10 < int(self.y < int(self.CoordOfPurpose[1]) + 10):
            self.ItStand = True
            self.y_dir = 0
            self.x_dir = 0

    def attack(self):
        self.ItAttack = True
        self.stop()
        self.atc_frame = 0

    def stop(self):
        self.x_dir = 0
        self.y_dir = 0
        self.ItStand = True

    def die(self):
        self.stop()
        self.IsStartDie = True

    def create_purpose(self, x_pur, y_pur):
        self.ItStand = False
        x_dis = x_pur - self.x
        y_dis = y_pur - self.y

        if 0 > x_dis > y_dis:
            self.x_dir = -1 / (y_dis / x_dis)
            self.y_dir = -1

        elif x_dis < y_dis < 0:
            self.y_dir = -1 / (y_dis / x_dis)
            self.x_dir = -1

        elif x_dis > y_dis > 0:
            self.x_dir = 1
            self.y_dir = 1 / (x_dis / y_dis)

        elif 0 < x_dis < y_dis:
            self.y_dir = 1
            self.x_dir = 1 * (x_dis / y_dis)

        elif x_dis > 0 > y_dis:
            self.x_dir = 1
            self.y_dir = 1 / (x_dis / y_dis)

        elif x_dis < 0 < y_dis:
            self.y_dir = 1
            self.x_dir = 1 * (x_dis / y_dis)

        elif x_dis == 0 < y_dis:
            self.x_dir = 0
            self.y_dir = 1


        elif y_dis == 0 < x_dis:
            self.x_dir = 1
            self.y_dir = 0

        elif x_dis == y_dis and x_dis > 0 and y_dis > 0:
            self.y_dir = 1
            self.x_dir = 1
        elif x_dis == y_dis and x_dis < 0 and y_dis < 0:
            self.y_dir = -1
            self.x_dir = -1
        self.atc_dir = self.x_dir
        self.CoordOfPurpose[0] = x_pur
        self.CoordOfPurpose[1] = y_pur
