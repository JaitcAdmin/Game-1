from sprite import Sprite


class Attack(Sprite):
    def __init__(self, x, y, fps):
        Sprite.__init__(self, fps)
        self.x = x
        self.y = y
        self.IsWorkOut = False

    def work_out(self):
        pass
