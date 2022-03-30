import pygame as pg
from pygame.sprite import Sprite
from timer import Timer
from enemies import Enemies


class Goomba(Sprite):
    def __init__(self, screen, goomba_images, platforms, x, y):
        super(Goomba, self).__init__()
        self.platforms = platforms
        self.rect = pg.Rect(x, y, 32, 32)
        for i in range(3):
            goomba_images[i] = pg.transform.scale2x(goomba_images[i])
        self.goomba_timer = Timer(goomba_images, 300)
        self.screen = screen
        self.isSquished = False
        self.killme = False
        self.velocity = -1

    def update(self):
        timer_image = self.goomba_timer.imagerect()
        self.now = pg.time.get_ticks()
        if self.isSquished:
            if self.now - self.last <= 180:
                self.goomba_timer.index = 2
                timer_image = self.goomba_timer.imagerect()
                self.image = timer_image
            else:
                self.killme = True
        else:
            if self.goomba_timer.index == 2:
                self.goomba_timer.index = 0
            else:
                self.image = timer_image
        if self.rect.collidelist(self.platforms) != -1:
            self.velocity *= -1
        if not self.isSquished:
            self.rect.x += self.velocity

    def squish(self):
        self.last = self.now
        self.isSquished = True

    def blitme(self):
        self.screen.blit(pg.transform.scale2x(self.image), self.rect)
