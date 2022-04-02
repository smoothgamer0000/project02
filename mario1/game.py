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
from stats import Stats
from goomba import Goomba
from koopa import Koopa
from timer import Timer
from mario import Mario
from camera import Camera
from object_functions import from_sprite_sheet, strip_objects
from sound import Sound
import sys

#from sound import Sound

class Game:

    def __init__(self):
        pg.init()
        self.settings = Settings()
        # self.screen = pg.display.set_mode((self.settings.screen_width,
        #                                    self.settings.screen_height))

        #self.screen = pg.display.set_mode((1200, 450))
        self.screen = pg.display.set_mode((self.settings.screen_width,
                                           self.settings.screen_height))

        # self.bg_color = self.settings.bg_color
        # self.stats = Stats(game=self)
        # self.sb = Scoreboard(game=self)
        # self.mario = Mario(game=self)

        self.objects = []
        strip_objects('images/coords.txt', self.objects)
        self.camera = Camera(self.objects)
        self.goomba_images = from_sprite_sheet((0, 0), (16, 16), 3, 1,
                                               pg.image.load('images/goomba.png').convert_alpha())
        self.koopa_images = from_sprite_sheet((0, 0), (16, 24), 2, 1,
                                               pg.image.load('images/koopa.png').convert_alpha())
        for i in range(3):
            self.goomba_images[i] = pg.transform.scale2x(self.goomba_images[i])
        for i in range(2):
            self.koopa_images[i] = pg.transform.scale2x(self.koopa_images[i])
        self.enemies = pg.sprite.Group()
        self.enemies.add(Goomba(self.screen, self.goomba_images, self.objects, 400, 368))
        self.enemies.add(Goomba(self.screen, self.goomba_images, self.objects, 600, 368))
        self.enemies.add(Goomba(self.screen, self.goomba_images, self.objects, 700, 368))
        self.enemies.add(Koopa(self.screen, self.koopa_images, self.objects, 500, 352))
        self.mario = Mario(self.screen, self.objects, self.camera)
        self.mario_small_timer = Timer(from_sprite_sheet((0, 0), (17, 16), 6, 1,
                                                         pg.image.load(
                                                             'images/small mario normal.png').convert_alpha()), 300)
        self.mario_big_timer = Timer(from_sprite_sheet((0, 0), (16, 32), 6, 1,
                                                       pg.image.load(
                                                           'images/adult mario normal.png').convert_alpha()), 300)
        self.marioWorld = pg.image.load("images/emptyWorld.png")
        self.marioWorld = pg.transform.scale2x(self.marioWorld)
        self.font = pg.font.Font(None, 32)
        self.sound = Sound()
        # pg.mixer.music.load('sound/super_mario_bros.wav')
        # pg.mixer.music.play(-1)
        self.clock = pg.time.Clock()


    def update(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.marioWorld, (self.camera.back_x, 0))
        self.mario.update(self.mario_small_timer)
        self.mario.blitme()
        self.enemies.update()
        self.enemies.draw(self.screen)
        for enemy in self.enemies:
            if enemy.killme:
                self.enemies.remove(enemy)
        enemy = pg.sprite.spritecollideany(self.mario, self.enemies)
        if enemy is not None and int(self.mario.velocity.y) > 0:
            enemy.squish()
        self.clock.tick(60)
        pg.display.flip()

    def draw(self):

        pg.display.flip()

    def play(self):
        self.finished = False
        self.sound.play_bg()    #changed to uses the Sound class and plays in the game
        while not self.finished:
            self.check_events()
            self.update()
            self.draw()
            #
        self.game_over()


    def game_over(self):
        self.sound.play_game_over()
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

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    sys.exit()

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

