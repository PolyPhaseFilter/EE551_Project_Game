class Enemy():
    def __init__(self, lifePoints=100):
        self.lifePoints = lifePoints

    def isAlive(self):
        return self.lifePoints > 0

    def takeHit(self, hitPower=0):
        self.lifePoints -= hitPower

class Defender():
    def __init__(self, lifePoints=100 , hitpower = 10):
        self.hitpower = hitpower
        self.lifePoints = lifePoints

    def attack(self, target):
        target.takeHit(self.hitpower)
