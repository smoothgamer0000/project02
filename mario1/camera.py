from pygame import *

class Camera:
    def __init__(self, objects):
        self.back_x = 0
        self.edge = Rect(700, 0, 20, 2000)
        self.objects = objects

    def update(self, speed):
        self.back_x -= int(speed)
        for p in self.objects:
            p.x -= int(speed)