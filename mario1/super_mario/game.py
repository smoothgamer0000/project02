import pygame as pg
from goomba import Goomba
from timer import Timer
from mario import Mario
from camera import Camera
from object_functions import from_sprite_sheet, strip_objects
import sys


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1200, 450))
        self.objects = []
        strip_objects('images/coords.txt', self.objects)
        self.camera = Camera(self.objects)
        self.goomba_images = from_sprite_sheet((0, 0), (16, 16), 3, 1,
                                                   pg.image.load('images/goomba.png').convert_alpha())
        self.enemies = pg.sprite.Group()
        self.enemies.add(Goomba(self.screen, self.goomba_images, self.objects, 400, 368))
        self.mario = Mario(self.screen, self.objects, self.camera)
        self.mario_small_timer = Timer(from_sprite_sheet((0, 0), (17, 16), 6, 1,
                                                   pg.image.load('images/small mario normal.png').convert_alpha()), 300)
        self.mario_big_timer = Timer(from_sprite_sheet((0, 0), (16, 32), 6, 1,
                                                        pg.image.load(
                                                            'images/adult mario normal.png').convert_alpha()), 300)
        self.marioWorld = pg.image.load("images/emptyWorld.png")
        self.marioWorld = pg.transform.scale2x(self.marioWorld)
        self.font = pg.font.Font(None, 32)
        pg.mixer.music.load('sound/super_mario_bros.wav')
        pg.mixer.music.play(-1)
        self.clock = pg.time.Clock()


    def play(self):
        while True:
            self.check_events()
            self.update()

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

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    sys.exit()

game = Game()
game.play()