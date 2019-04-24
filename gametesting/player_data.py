# player data module


class Player():
    def __init__(self, life_points=100, atk_power=0, atk_range=0, atk_speed=1.0, ult_range=0, ult_style=0
                 , ult_cool_down=0, movement_speed_x=0, movement_speed_y=0 , color = (0,0,0)
                 ,box=[40,40],location_x=0,location_y=0):
        self.life_Points = life_points
        self.atk_Power = atk_power
        self.atk_range = atk_range
        self.ult_range = ult_range
        self.atk_speed = atk_speed
        self.ult_style = ult_style
        self.movement_speed_x = movement_speed_x
        self.movement_speed_y = movement_speed_y
        self.location_x=location_x
        self.location_y=location_y
        self.ult_cool_down = ult_cool_down
        self.color=color
        self.box=box
    def isAlive(self):
        return self.life_points > 0

    def takeHit(self, atk_power=0):
        self.life_points -= atk_power

player_one = Player()
player_two = Player()

