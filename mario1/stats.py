import os

class Stats:
    def __init__(self,game):
        self.game = game
        self.settings = game.settings
        #self.reset_stats()
        #self.last_lives_left = self.lives_left
        self.score = 0
        self.level = 0
        #self.highscore = self.load_high_score()

        def __del__(self): self.save_high_score()

        def load_high_score(self):
            try:
                with open("highscore.txt", "r") as f:
                    return int(f.read())
            except:
                return 0

        def save_high_score(self):
            try:
                with open("highscore.txt", "w+") as f:
                    f.write(str(round(self.highscore, -1)))
            except:
                print("highscore.txt not found...")

        def get_score(self):
            return self.score

        def get_highscore(self):
            return self.highscore

        def get_level(self):
            return self.level

        def get_lives_left(self):
            return self.lives_left

        def reset_stats(self):
            self.lives_left = self.settings.mario_limit

        def enemy_hit(self, enemy):
            self.score += enemy.points
            self.highscore = max(self.score, self.highscore)