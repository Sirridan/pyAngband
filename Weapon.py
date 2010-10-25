#Weapon.py

import Item
import Utils
import Effect

def default_brand(damage, target):
    return (damage, "")

def fire_brand(damage, target):
    return (damage * 3, "burn")

def cold_brand(damage, target):
    return (damage * 3, "freeze")
    
def acid_brand(damage, target):
    return (damage * 3, "corrode")
    
def elec_brand(damage, target):
    return (damage * 3, "zap")

def slay_dragon(damage, target):
    return (damage * 3, "smite")

def kill_dragon(damage, target):
    return (damage * 5, "furiously smite")

def time_brand(damage, target):
    if(Util.one_in(5)):
        target.add_timed_effect(Effect.SLOW, 10, Util.roll_dice("5d5+5"))
    return (damage * Util.roll_dice("1d5"))
    
def get_best_brand(target):
    return default_brand

class Weapon(Item.EquipableItem):
    def __init__(self, id):
        super(Weapon, self).__init__(id)
        self._damage_dice = "1d2"
        self._to_hit = 0
        self._to_dmg = 0
        self._to_armor = 0
        self._brands = []
    
    def calc_damage(self, target):
        damage = Utils.roll_dice(self._damage_dice)
        brand = default_brand
        if(len(self._brands) > 0):
            brand = get_best_brand(target)    #target is a LivingThing...
        return brand(damage, target)
    