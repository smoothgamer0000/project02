import pygame as pg
from menu import menuPage
from sys import exit
from settings import Settings
from highscores import highscorePage
#import game_functions as gf
from time import sleep
from scoreboard import Scoreboard
from ball import Ball, enemyBall
from mario import Mario
from enemy import Enemy
from settings import Settings
#from sound import Sound

class Game:

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))

    def update(self): pass

    def draw(self):

        pg.display.flip()

    def play(self):
        self.finished = False
        while not self.finished:
            self.update()
            self.draw()
            #
        self.game_over()


    def game_over(self):
        #self.sound.play_game_over()
        print('\nGAME OVER!\n\n')
        exit()

    def restart(self):
        if self.stats.lives_left == 0:
          self.game_over()
        print("restarting game")
        while self.sound.busy():    # wait for explosion sound to finish
            pass
        self.lasers.empty()
        self.alien_lasers.empty()
        self.alien_fleet.empty()
        self.alien_fleet.create_fleet()
        self.ship.center_bottom()
        self.ship.reset_timer()
        self.update()
        self.draw()
        sleep(0.5)

def main():
    print("started")
    g = Game()

    mn = menuPage(game=g)
    mn.show()

    hs = highscorePage(game=g)
    if(mn.high_scores_page_change == True):
        hs.show()

    g.play()

if __name__ == '__main__':
    main()

