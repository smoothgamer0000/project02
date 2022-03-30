import pygame as pg
from vector import Vector
#from timer import Timer
from pygame.sprite import Sprite, Group
#from sound import Sound

class Mario(Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        #self.sound = game.sound
        self.ball = None
        self.stats = game.stats
        #self.mario_image = pg.image.load('images/mario.bmp')

        #self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #self.center_bottom()
        self.v = Vector()
        self.firing = False
        self.frames = 0
        #self.exploding_timer = Timer(image_list=Ship.exploding_images, delay=200, is_loop=False)
        #self.normal_timer = Timer(image_list=Ship.images, delay=1000, is_loop=True)
        #self.timer = self.normal_timer
        self.dying = False

        def set_ball(self, ball): self.ball = ball

        def set_spawn(self): pass

        # def reset_timer(self):
        #     self.exploding_timer.reset()
        #     self.normal_timer.reset()
        #     self.timer = self.normal_timer

        def toggle_firing(self): self.firing = not self.firing

        # def hit(self):
        #     self.timer = self.exploding_timer
        #     self.dying = True
        #     self.sound.play_ship_explosion()
        def is_dying(self): return self.dying
        def die(self):
            self.stats.mario_hit()
            if self.stats.lives_left == 0:
                self.game.finished = True
            self.dying = False
            self.game.restart()

        def moving(self, vector): self.v = vector
        def inc_add(self, other): self.v += other

