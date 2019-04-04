# player data module

class Player():
    def __init__(self, life_points=10, atk_power=0, atk_range=0, atk_speed=1.0, ult_range=0, ult_style=0
                 , ult_cool_down=0, movement_speed=60):
        self.life_Points = life_points
        self.atk_Power = atk_power
        self.atk_range = atk_range
        self.ult_range = ult_range
        self.atk_speed = atk_speed
        self.ult_style = ult_style
        self.movement_speed = movement_speed
        self.ult_cool_down = ult_cool_down

    def isAlive(self):
        return self.life_points > 0

    def takeHit(self, atk_power=0):
        self.life_points -= atk_power