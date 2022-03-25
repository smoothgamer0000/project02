import pygame as pg
import sys
#from sound import Sound
#from vector import Vector
from button import Button

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
sm_pos = (100,100)
dh_pos = (500,200)

class menuPage:

    super_mario_imgs = pg.image.load(f'images/orange_supermario.png')
    duck_hunt_imgs = pg.image.load(f'images/duck_hunt.png')

    supermario_title = super_mario_imgs.get_rect()
    duck_hunt_title = duck_hunt_imgs.get_rect()



    def __init__(self, game):
        #self.sound = game.sound
        self.screen = game.screen
        self.menu_page_finished = False
        #self.highschore = game.stats.get_highscore()

        headingFont = pg.font.SysFont(None, 192)
        subheadingFont = pg.font.SysFont(None, 122)
        font = pg.font.SysFont(None, 48)

        centerx = self.screen.get_rect().centerx
        centery = self.screen.get_rect



    def draw(self):
        self.duck_hunt_imgss = pg.image.load(f'images/duck_hunt.png')
        self.super_mario_imgss = pg.image.load(f'images/orange_supermario.png')
        self.dk_rect = self.duck_hunt_imgss.get_rect()
        self.sm_rect = self.super_mario_imgss.get_rect()


        self.screen.fill(BLACK)
        self.screen.blit(self.duck_hunt_imgss, self.dk_rect)
        self.screen.blit(self.super_mario_imgss, self.sm_rect)
        pg.display.flip()

    def show(self):
        while not self.menu_page_finished:
            self.draw()

    def check_events(self):
        window = True
        while window:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    window = False
