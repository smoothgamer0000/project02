import pygame as pg

class Sound:
    def __init__(self): 
        pg.mixer.init()
        self.super_jump = pg.mixer.Sound('sound/super_jump.wav')
        self.stomp = pg.mixer.Sound('sound/stomp.wav')

    #uses a function to play music
    def play_music(self, music, volume=0.3):
        pg.mixer.music.unload()
        pg.mixer.music.load(music)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(-1, 0.0)

    #uses a function to play sounds
    def play_sound(self, sound):
        pg.mixer.Sound.play(sound)

    #background music
    def play_bg(self):
        self.play_music('sound/super_mario_bros.wav')

    #lists of sounds to play
    def play_super_jump(self): self.play_sound(self.super_jump)
    def play_stomp(self): self.play_sound(self.stomp)