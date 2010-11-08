from Creature import Creature

boots = "boots"
lring = "lring"
rring = "rring"
weapon = "weapon"
ranged = "ranged"
hat = "hat"
body = "body"
gloves = "gloves"
neck = "neck"
shield = "shield"

class Player(object): #Player(Creature):
    def __init__(self):
        self._x = 1
        self._y = 1
        self._inventory = []
        self._equipment = {boots:None, lring:None, rring:None, weapon:None, ranged:None, hat:None, body:None, gloves:None, neck:None, shield:None}

    def get_xy(self):
        return (self._x, self._y)
    def set_xy(self, x, y):
        if(x < 0 or y < 0): return
        self._x = x
        self._y = y