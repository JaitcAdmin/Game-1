from tkinter import *
import random
import time


class Map:
    def __init__(self, IsD, x_p, m, string):
        self.f = False
        self.m = m
        self.string = string
        self.map = []
        self.s = [1, 1, 1, 2, 2, 3, 4]
        self.n = 100
        self.mmcdcfs = 0
        self.Is = 0
        self.b = 0
        for i in self.s:
            self.Is += i

        self.n -= self.Is
        self.x_p = x_p
        sim = ["б", "в", "г", "д", "е", "ж", "з", "и", "к", "а"]
        self.sim = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "к"]
        for x in range(0, 10):
            a = []
            for y in range(0, 10):
                if IsD:
                    canvas.create_line(x_p + (x * 50 + 50), 50, x_p + (x * 50 + 50), 550)
                    canvas.create_line(x_p + 50, y * 50 + 50, x_p + 550, y * 50 + 50)
                a.append(0)
                if IsD and (x <= 11 or y <= 11):
                    canvas.create_text(x_p + x * 50 + 75, 25, text=sim[x - 1])
                    canvas.create_text(x_p + 25, x * 50 + 75, text=x + 1)
                if IsD:
                    canvas.create_rectangle(x_p + (x * 50 + 50), y * 50 + 50, x_p + (x * 50 + 100), x * 50 + 100,
                                            fill="white")
            self.map.append(a)

    def control(self, i):
        self.r = int(random.random() * 2)
        self.f_p_x = int(random.random() * (10 - i))
        self.f_p_y = int(random.random() * (10 - i))
        for j in range(0, i):
            if (self.map[self.f_p_x + j * self.r][self.f_p_y + j * (1 - self.r)] == 1 or
                    self.map[self.f_p_x + j * self.r][self.f_p_y + j * (1 - self.r)] == 2):
                if self.b <= 90:
                    self.control(i)
                    self.b += 1
                else:
                    return False
        return True

    def random(self):
        if not self.m.f:
            self.a = 0
            self.map = []
            for x in range(0, 10):
                mmm = []
                for y in range(0, 10):
                    mmm.append(0)
                self.map.append(mmm)
            for i in self.s:
                if self.control(i):
                    try:
                        print(f"r= {self.r} len(s)={self.string}")
                        for y in range(0, i):
                            self.map[self.f_p_x + (y * self.r)][self.f_p_y + y * (1 - self.r)] = 1

                        for xg in range(self.f_p_x - 1, self.f_p_x + (i * self.r) + 1 * (1 - self.r) + 1):
                            for yg in range(self.f_p_y - 1, (self.f_p_y + (i * (1 - self.r)) + 1 * self.r) + 1):
                                # print(self.f_p_x, "   ", self.f_p_y)
                                if self.map[xg][yg] != 1:
                                    self.map[xg][yg] = 2

                    except(IndexError):
                        pass

    def draw(self):
        for x in range(0, len(self.map)):
            for y in range(0, len(self.map)):
                if self.map[x][y] == 1:
                    canvas.create_rectangle(self.x_p + x * 50 + 50, y * 50 + 50, self.x_p + x * 50 + 100, y * 50 + 100,
                                            fill="black")
                elif self.map[x][y] == 0 or self.map[y][x] == 4:
                    canvas.create_rectangle(self.x_p + x * 50 + 50, y * 50 + 50, self.x_p + x * 50 + 100, y * 50 + 100,
                                            fill="white")
                elif self.map[x][y] == 5:
                    canvas.create_rectangle(self.x_p + x * 50 + 50, y * 50 + 50, self.x_p + x * 50 + 100, y * 50 + 100,
                                            fill="red")

    def attack(self, x, y):
        self.f = True
        if self.x_p + 50 <= x <= self.x_p + 550 and 50 <= y <= 550:
            if self.map[int(y / 50) - 1][int((x - self.x_p) / 50) - 1] == 1:
                canvas.create_rectangle(int((x - self.x_p) / 50) * 50 + self.x_p, int(y / 50) * 50,
                                        int((x - self.x_p) / 50) * 50 + 50 + self.x_p,
                                        int(y / 50) * 50 + 50, fill="red")
                if self.Is > 1:
                    self.Is -= 1
                    self.map[int(y / 50) - 1][int((x - self.x_p) / 50) - 1] = 3
                else:
                    tk.destroy()
                    print(self.string)
            elif self.map[int(y / 50) - 1][int((x - self.x_p) / 50) - 1] != 1 != 3 != 4:
                canvas.create_rectangle(int((x - self.x_p) / 50) * 50 + self.x_p, int(y / 50) * 50,
                                        int((x - self.x_p) / 50) * 50 + 50 + self.x_p,
                                        int(y / 50) * 50 + 50, fill="blue")
                self.map[int(y / 50) - 1][int((x - self.x_p) / 50) - 1] = 3
                self.generate_attack(self.m, int(random.random() * 10), int(random.random() * 10))

    def generate_attack(self, m, x, y):
        self.mmcdcfs += 1
        a = x * 10 + y

        if m.map[int(a / 10)][int(a % 10)] == 0 or m.map[int(a / 10)][int(a % 10)] == 2:
            m.map[int(a / 10)][int(a % 10)] = 3
            canvas.create_rectangle(m.x_p + int(a / 10) * 50 + 50, int(a % 10) * 50 + 50,
                                    m.x_p + int(a / 10) * 50 + 100, int(a % 10) * 50 + 100, fill="blue")
        elif m.map[int(a / 10)][int(a % 10)] == 1:
            canvas.create_rectangle(m.x_p + int(a / 10) * 50 + 50, int(a % 10) * 50 + 50,
                                    m.x_p + int(a / 10) * 50 + 100, int(a % 10) * 50 + 100, fill="red")
            if m.Is > 1:
                m.Is -= 1
                m.map[int(a / 10)][int(a % 10)] = 3
            else:
                tk.destroy()
                # print(m.string)
            self.second_attack(int(a / 10), int(a % 10))

    def q(self):
        self.random()
        self.draw()

    def second_attack(self, x, y):
        # print(f"{self.string}  {int(x)} / {int(y)}")

        xf = int(random.random() * 3) - 1
        yf = int(random.random() * 3) - 1
        self.generate_attack(self.m, x + xf + 1, y + yf + 1)
        # print(f"{x+1} + {xf} = {x+xf+1} / {y+yf+1} = {y+1} + {yf}")


def atc(event):
    m2.attack(event.x, event.y)


tk = Tk()
tk.title("Морской Бой")
canvas = Canvas(tk, width=1200, height=600)
canvas.pack()
m2 = None
m = Map(True, 0, m2, "Вы проиграли")
m2 = Map(True, 600, m, "Вы выйграли")
m.m = m2
m.random()
m2.random()
tk.bind("<Button-1>", atc)
m.draw()
tk.mainloop()
