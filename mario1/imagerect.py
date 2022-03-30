import pygame as pg


class ImageRect:
    def __init__(self, screen, image, height, width):
        self.screen = screen
        name = image

        img = pg.image.load(name).convert_alpha()
        img = pg.transform.scale(img, (height, width))
        self.rect = img.get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height
        self.image = img

    def blit(self):
        self.screen.blit(self.image, self.rect)