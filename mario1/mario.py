import pygame as pg
from pygame.sprite import Sprite
from pygame import *
from sound import Sound
from vector import Vector


class Mario(Sprite):
    def __init__(self, screen, platforms, camera):
        super(Mario, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(0, 300, 17, 16)
        self.camera = camera
        self.direction = 'r'
        self.v = Vector()
        self.max_speed = 5
        self.jump_max = 10
        self.isCrouched = False
        self.onGround = False
        self.platforms = platforms
        self.width = 17
        self.height = 16
        self.sound = Sound()

    def change(self, newMarioType):
        if newMarioType == 'big':
            self.rect = pg.Rect(self.rect[0], self.rect[1], 17, 32)
            self.height = 32
        elif newMarioType == 'small':
            self.rect = pg.Rect(self.rect[0], self.rect[1], 17, 16)
            self.height = 16

    def update(self, timer):
        timer_image = timer.imagerect()
        if int(self.v.y) == 0:
            if self.isCrouched:
                timer.index = 6
                self.image = timer_image
            elif self.v.x == 0:
                timer.index = 0
                if self.direction == 'l':
                    self.image = pg.transform.flip(timer_image, True, False)
                else:
                    self.image = timer_image
            elif self.v.x > 0:
                self.direction = 'r'
                if timer.index == 4:
                    timer.index = 1
                else:
                    timer.wait = 300 / (abs(self.v.x) / 2)
                    self.image = timer_image
            elif self.v.x < 0:
                self.direction = 'l'
                if timer.index == 4:
                    timer.index = 1
                else:
                    timer.wait = 300 / (abs(self.v.x) / 2)
                    self.image = pg.transform.flip(timer_image, True, False)
        else:
            if self.isCrouched:
                timer.index = 6
            elif not self.isCrouched:
                timer.index = 5
                if self.direction == 'l':
                    self.image = pg.transform.flip(timer_image, True, False)
                else:
                    self.image = timer_image
        pressed = pg.key.get_pressed()
        up = pressed[K_UP]
        left = pressed[K_LEFT]
        right = pressed[K_RIGHT]
        if up:
            if self.onGround and self.v.y <= self.jump_max:
                self.sound.play_super_jump()  #changed to uses the Sound class
                self.v.y -= 10
        if left and abs(self.v.x) <= self.max_speed:
            self.v.x -= 0.3
        if right and self.v.x <= self.max_speed:
            self.v.x += 0.3
        if not self.onGround:
            self.v.y += 0.3
            if self.v.y > 10:
                self.v.y = 10
        if left and self.v.x > 0:
            self.v.x -= 0.2
        if right and self.v.x < 0:
            self.v.x += 0.2
        if not right and not left:
            if self.v.x > 0.2:
                self.v.x -= 0.1
            elif self.v.x < -0.2:
                self.v.x += 0.1
            else:
                self.v.x = 0
        self.rect.x += self.v.x
        self.collide(self.v.x, 0, self.platforms)
        self.rect.y += self.v.y
        self.onGround = False
        self.collide(0, self.v.y, self.platforms)

    def collide(self, xvelocity, yvelocity, platforms):
        x = self.rect.collidelist(platforms)
        if x != -1:
            if xvelocity > 0:
                self.rect.right = platforms[x].left
                self.v.x = 0
            if xvelocity < 0:
                self.rect.left = platforms[x].right
                self.v.x = 0
            if yvelocity > 0:
                self.rect.bottom = platforms[x].top
                self.onGround = True
                self.v.y = 0
            if yvelocity < 0:
                self.rect.top = platforms[x].bottom
                self.v.y = 0
        if self.rect.colliderect(self.camera.edge):
            self.rect.right = self.camera.edge.left
            self.camera.update(xvelocity)

    def blitme(self):
        self.screen.blit(pg.transform.scale2x(self.image), self.rect.inflate(self.width, self.height))
