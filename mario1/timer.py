import pygame as pg


class Timer:
    def __init__(self, frames, wait=100, index=0, looponce=False):
        self.frames = frames
        self.wait = wait
        self.index = index
        self.looponce = looponce

        self.finished = False
        self.lastframe = len(frames) - 1
        self.last = None

    def frame_index(self):
        now = pg.time.get_ticks()
        if self.last is None:
            self.last = now
            self.index = 0
            return 0
        elif not self.finished and now - self.last > self.wait:
            self.index += 1
            if self.looponce and self.index == self.lastframe:
                self.finished = True
            else:
                self.index %= len(self.frames)
            self.last = now
        return self.index

    def reset(self):
        self.last = None
        self.finished = False

    def imagerect(self):
        return self.frames[self.frame_index()]
