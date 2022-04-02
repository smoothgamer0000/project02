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

   def __init__(self, game):
       #self.sound = game.sound
       self.screen = game.screen
       self.menu_page_finished = False
       #self.highschore = game.stats.get_highscore()

       # super_mario_imgs = pg.image.load(f'images/orange_supermario.png')
       # self.screen.blit(super_mario_imgs, (30, 30))
       # pg.display.update()

       headingFont = pg.font.SysFont(None, 192)
       subheadingFont = pg.font.SysFont(None, 122)
       font = pg.font.SysFont(None, 48)

       centerx = self.screen.get_rect().centerx
       centery = self.screen.get_rect().centery

       self.play_button = Button(self.screen, "Play Game", ul=(centerx - 150, 650))
       self.high_scores = Button(self.screen, "High Scores", ul=(centerx - 150, 700))

       self.high_scores_page_change = False

   def mouse_on_play(self):
       mouse_x, mouse_y = pg.mouse.get_pos()
       return self.play_button.rect.collidepoint(mouse_x, mouse_y)
   def mouse_on_highscores(self):
       mouse_x, mouse_y = pg.mouse.get_pos()
       return self.high_scores.rect.collidepoint(mouse_x, mouse_y)

   def draw(self):
       self.screen.fill(BLACK)
       self.play_button.draw()
       self.high_scores.draw()

       scaling = (600,200)

       super_mario_imgs = pg.image.load(f'images/orange_supermario.png')
       super_mario_imgs = pg.transform.scale(super_mario_imgs, scaling)
       self.screen.blit(super_mario_imgs, (350, 50))

       duck_hunt_imgs = pg.image.load(f'images/duck_hunt.png')
       duck_hunt_imgs = pg.transform.scale(duck_hunt_imgs, scaling)
       self.screen.blit(duck_hunt_imgs, (330,330))

       pg.display.flip()

   def show(self):
       while not self.menu_page_finished:
           self.draw()
           #self.update()
           self.check_events()

   def check_events(self):
       for e in pg.event.get():
           if e.type == pg.QUIT:
               sys.exit()
           if e.type == pg.MOUSEBUTTONDOWN:
               if self.mouse_on_play():
                   self.menu_page_finished = True
               if self.mouse_on_highscores():
                   self.menu_page_finished = True
                   self.high_scores_page_change = True
