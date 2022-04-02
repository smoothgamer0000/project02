import pygame as pg

class Sound:
    def __init__(self): 
        pg.mixer.init()
        self.super_jump = pg.mixer.Sound('sound/super_jump.wav')
        self.stomp = pg.mixer.Sound('sound/stomp.wav')
        self.game_over = pg.mixer.Sound('sound/gameover.wav')
        self.one_up = pg.mixer.Sound('sound/1_up.wav')
        self.bowser_falls = pg.mixer.Sound('sound/bowser_falls.wav')
        self.bowser_fire = pg.mixer.Sound('sound/bowser_fire.wav')
        self.break_block = pg.mixer.Sound('sound/break_block.wav')
        self.flag_pole = pg.mixer.Sound('sound/flagpole.wav')
        self.kick = pg.mixer.Sound('sound/kick.wav')
        self.mario_die = pg.mixer.Sound('sound/mario_die.wav')
        self.pause = pg.mixer.Sound('sound/pause.wav')
        self.pipe_down = pg.mixer.Sound('sound/pipe_powerdown.wav')
        self.power_down = pg.mixer.Sound('sound/pipe_powerdown.wav')
        self.power_up = pg.mixer.Sound('sound/powerup.wav')
        self.power_up_appear = pg.mixer.Sound('sound/powerup_appear.wav')
        self.small_jump = pg.mixer.Sound('sound/small_jump.wav')
        self.stage_clear = pg.mixer.Sound('sound/stage_clear.wav')
        self.vine = pg.mixer.Sound('sound/vine.wav')
        self.warning = pg.mixer.Sound('sound/warning.wav')
        self.world_clear = pg.mixer.Sound('sound/world_clear.wav')

    #uses a function to play music
    def play_music(self, music, volume=0.3):
        pg.mixer.music.unload()
        pg.mixer.music.load(music)
        pg.mixer.music.set_volume(volume)
        pg.mixer.music.play(-1, 0.0)

    def busy(self): 
        return pg.mixer.get_busy()

    def stop_bg(self): 
        pg.mixer.music.stop()

    # Sound when there are no more lives
    def play_game_over(self):
        self.stop_bg()     # no more background music
        self.play_sound(self.game_over)
        while self.busy():    # stays here until end_theme finishes playing
            pass

    # Sound when you reach the flag pole
    def play_finished_level(self):
        self.stop_bg()
        self.play_sound(self.flag_pole)
        while self.busy():
            pass
        self.play_sound(self.stage_clear)
        while self.busy():
            pass

    # Sound when mario dies
    def play_mario_died(self):
        self.stop_bg()
        self.play_sound(self.mario_die)
        while self.busy():
            pass

    #uses a function to play sounds
    def play_sound(self, sound):
        pg.mixer.Sound.play(sound)

    #background music
    def play_bg(self):
        self.play_music('sound/super_mario_bros.wav')

    #lists of sounds to play
    def play_super_jump(self): self.play_sound(self.super_jump)
    def play_stomp(self): self.play_sound(self.stomp)
    def play_one_up(self): self.play_sound(self.one_up)
    def play_bowser_falls(self): self.play_sound(self.bowser_falls)
    def play_bowser_fire(self): self.play_sound(self.bowser_fire)
    def play_break_block(self): self.play_sound(self.break_block)
    def play_kick(self): self.play_sound(self.kick)
    def play_pause(self):
        self.stop_bg()
        self.play_sound(self.pause)
    def play_pipe_down(self): self.play_sound(self.pipe_down)
    def play_power_down(self): self.play_sound(self.power_down)
    def play_power_up(self): self.play_sound(self.power_up)
    def play_power_up_appear(self): self.play_sound(self.power_up_appear)
    def play_small_jump(self): self.play_sound(self.small_jump)
    def play_vine(self): self.play_sound(self.vine)
    def play_warning(self): self.play_sound(self.warning)