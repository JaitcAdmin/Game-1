from sprite import Sprite
import random

class Enemy(Sprite):
    def __init__(self, fps, x, y, walls, c):
        Sprite.__init__(self, fps)
        self.dir = 1
        self.x = x
        self.y = y
        self.c = c
        self.dis = 0
        self.x_check = x
        self.y_check = y
        self.walls = walls
        print(f"{x}/{y}")
        self.IsStart = False
        self.IsAttack = False
        self.ToBeStart = False
        self.FPS = fps
        self.target_x = 0
        self.target_y = 0
        self.line = 0
        self.visibility_range = 1900

    def check(self, target_x, target_y):
        x = self.x
        y = self.y
        self.dis = (((target_y - y) ** 2) + ((target_x - x) ** 2)) ** 0.5
        target_y = target_y + random.randint(0, 55)
        if x > target_x:
            max_x = x
            min_x = target_x
        else:
            max_x = target_x
            min_x = x
        a = (target_y - y) / (target_x - x)
        b = y - ((target_y - y) / (target_x - x))*x
        if y > target_y:
            max_y = y
            min_y = target_y
        else:
            max_y = target_y
            min_y = y
        if x == target_x and self.dis <= self.visibility_range:
            for i in range(min_y, max_y):
                y = a * x + b
                self.x_check = x
                self.y_check = y
                if self.walls[int(y/60)][int(x/60)] == 4:
                    return False
        elif self.dis <= self.visibility_range:
            for x in range(int(min_x), int(max_x)):
                y = a * x + b
                self.x_check = x
                self.y_check = y
                if self.walls[int(y/60)][int(x/60)] == 4:
                    return False
        else:
            return False
        return True

    def new_data(self, x, y):
        self.target_x = x
        self.target_y = y
