from vector import Vector

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800

        self.mario_speed_factor = 3
        self.mario_limit = 3

        self.enemy_speed_factor = 1
        #self.fleet_drop_speed = 10
        self.enemy_direction = Vector(1, 0)

        self.fire_ball_speed_factor = 3
        self.fire_ball_width = 3
        self.fire_ball_height = 15
        self.fire_ball_color = 255, 0, 0