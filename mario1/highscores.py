import pygame as pg
import sys
#from sound import Sound
from button import Button
from menu import menuPage
from enemy import Enemy
from vector import Vector


GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (130, 130, 130)
sm_pos = (100,100)
dh_pos = (500,200)

class highscorePage:

    def __init__(self, game):
        self.screen = game.screen
        self.highscores_page_finished = False
        #self.highscore = game.stats.get_highscore()

        headingFont = pg.font.SysFont(None, 192)
        subheadingFont = pg.font.SysFont(None, 122)
        font = pg.font.SysFont(None, 48)

        centerx = self.screen.get_rect().centerx
        centery = self.screen.get_rect().centery

        self.play_button = Button(self.screen, "Play Game", ul=(centerx - 150, 650))

        #highscore_string = [ (f'HIGH SCORE = {self.highscore:,}', GREY, font)]
        #self.texts = [self.get_text(msg=s[0], color=s[1], font=s[2]) for s in highscore_string]
        self.posns = [150, 230]
        #self.posns.extend(enemy)
        self.posns.append(730)

        #n = len(self.texts)
        #self.rects = [self.get_text_rect(text=self.texts[i], centerx=centerx, centery=self.posns[i]) for i in range(n)]

    def get_text(self, font, msg, color):
        return font.render(msg, True, color, BLACK)

    def get_text_rect(self, text, centerx, centery):
        rect = text.get_rect()
        rect.centerx = centerx
        rect.centery = centery
        return rect



    def mouse_on_play(self):
        mouse_x, mouse_y = pg.mouse.get_pos()
        return self.play_button.rect.collidepoint(mouse_x, mouse_y)

    def draw(self):
        self.screen.fill(BLACK)
        self.play_button.draw()
        #self.draw_text()
        pg.display.flip()

    def show(self):
        while not self.highscores_page_finished:
            self.draw()
            #self.update()
            self.check_events()

    def check_events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            if e.type == pg.MOUSEBUTTONDOWN:
                if self.mouse_on_play():
                    self.highscores_page_finished = True

    # def draw_text(self):
    #     n = len(self.texts)
    #     for i in range(n):
    #         self.screen.blit(self.texts[i], self.rects[i])

