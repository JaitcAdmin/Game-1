from sprite import Sprite
from tkinter import *
import numpy as np


class Map(Sprite):
    def __init__(self, m, FPS):
        file_num = open("D:\\Python\\Games\\Game 1\\Maps\\number.txt", "r")
        num = file_num.read()
        file_num.close()
        self.mapa = self.make(self.maps(num), 32)
        self.y = 0
        self.canvas = m.canvas
        self.m = m
        self.FPS = FPS
        self.images = [
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\1.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m2.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m3.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Maps\\m4.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\Walls\\2.png"),
            PhotoImage(file="D:\\Python\\Games\\Game 1\\assets\\grass\\6.png")
        ]

    def maps(self, nom):
        file = open(F"D:\\Python\\Games\\Game 1\\Maps\\{nom}.txt", "r")
        a = file.read()
        b = []
        for i in a:
            if i != "]" and i != "[" and i != " " and i != ",":
                b.append(i)
        file.close()
        return b

    def make(self, list, w):
        a = np.array(list)
        arr = np.reshape(a, (-1, w))
        arr2 = arr.tolist()
        for i in range(0, len(arr2)):
            for y in range(0, len(arr2[i])):
                arr2[i][y] = int(arr2[i][y])
        return arr2
