from tkinter import *
import time


class Logo:
    def __init__(self):
        self.tk = Tk()
        self.WIDTH = 1920
        self.HEIGHT = 1080
        self.tk = Tk()
        self.tk.attributes("-topmost", True)
        self.tk.attributes('-fullscreen', True)
        self.tk.resizable(0, 0)
        self.canvas = Canvas(self.tk, width=self.WIDTH, height=self.HEIGHT)
        self.canvas.pack()
        self.start_images = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f3.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f4.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f5.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f6.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f7.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f8.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f9.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f10.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f11.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f12.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f13.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f14.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f15.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f16.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f17.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f18.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f19.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f20.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f21.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f22.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f23.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f24.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f25.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f26.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f27.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f28.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f29.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f30.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f31.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f32.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f33.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f34.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f35.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f36.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f37.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f38.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f39.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f40.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f41.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f42.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f43.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f44.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Start Logo//f45.png")
        ]
        self.main_logo = [
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_001_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_002_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_003_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_004_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_005_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_006_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_007_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_008_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_009_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_010_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_011_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_012_delay-0.04s.png"),
            PhotoImage(file="D://Python//Games//Game 1//assets//Logo//Game Logo//frame_013_delay-0.04s.png"),
        ]
        self.frame = 0
        self.end_first_logo = False
        self.term = 1
        #self.image = self.canvas.create_image(600, 0, image=self.start_images[self.frame])

    def mainloop(self):
        while 1:
            if not self.end_first_logo:
                self.canvas.itemconfig(self.image, self.start_images[self.frame])
            self.frame += self.term
            self.tk.update()
            self.tk.update_idletasks()
            time.sleep(0.05)


l = Logo()