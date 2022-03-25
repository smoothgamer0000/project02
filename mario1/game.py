import pygame as pg
from menu import menuPage
from sys import exit
from settings import Settings
#import game_functions as gf

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

def main():
    print("started")
    g = Game()
    mn = menuPage(game=g)
    mn.show()
    g.play()

if __name__ == '__main__':
    main()

