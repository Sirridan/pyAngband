import ID.Tval, ID.Sval
from Effects.Effects import effects
from Edit.Helper import *

class Item(object):
    """
        weight: "",
        value: "",
        rarity: "",
        depth: "min-max", 
        damage: "xdy",
        ac: "0",
        thrown_damage: "xdy",
        created: False,
        to_hit: "0",
        to_dam: "0",
        to_ac: "0",
        item_resists: [],
        resists: [],
        vulnerabilities: [],
        immunities: [],
        flags: [],
        powers: {POWER: VALUE},
        effect: (EFFECT, RECHARGE, CHARGES)
    """
    def __init__(self, tval, sval, item_kind_info):
        self._tval = tval
        self._sval = sval
        if(weight in item_kind_info):           self._weight = item_kind_info[weight]
        if(value in item_kind_info):            self._value = item_kind_info[value]
        if(rarity in item_kind_info):           self._rarity = item_kind_info[rarity]
        if(depth in item_kind_info):            self._depth = item_kind_info[depth]
        if(damage in item_kind_info):           self._damage = item_kind_info[damage]
        if(ac in item_kind_info):               self._ac = item_kind_info[ac]
        if(thrown_damage in item_kind_info):    self._thrown_damage = item_kind_info[thrown_damage]
        if(to_hit in item_kind_info):           self._to_hit = item_kind_info[to_hit]
        if(to_dam in item_kind_info):           self._to_dam = item_kind_info[to_dam]
        if(to_ac in item_kind_info):            self._to_ac = item_kind_info[to_ac]
        if(item_resists in item_kind_info):     self._item_resists = item_kind_info[item_resists]
        if(resists in item_kind_info):          self._resists = item_kind_info[resists]
        if(vulnerabilities in item_kind_info):  self._vulnerabilities = item_kind_info[vulnerabilities]
        if(immunities in item_kind_info):       self._immunities = item_kind_info[immunities]
        if(flags in item_kind_info):            self._flags = item_kind_info[flags]
        if(powers in item_kind_info):           self._powers = item_kind_info[powers]
        if(effect in item_kind_info):
            temp_eff = item_kind_info[effect][0]
            temp_recharge = item_kind_info[effect][1]
            temp_charges = item_kind_info[effect][2]
            self._effect = temp_eff
            if(temp_recharge > 0):
                self._recharge = temp_recharge
                self._recharge_time = 0
            if(temp_charges > 0): self._charges = temp_charges

    def get_powers(self):
        return self._powers
    def equipable(self):
        global EQUIPABLE
        return self._tval in ID.Tval.EQUIPABLE
    def readable(self):
        return self._tval in ID.Tval.READABLE
    def zappable(self):
        return self._tval in ID.Tval.ZAPPABLE
    def drinkable(self):
        return self._tval in ID.Tval.DRINKABLE
    def use(self, target, world):
        if(hasattr(self, "_charges")): 
            if(self._charges > 0):
                self._charges -= 1
        if(hasattr(self, "_recharge")):
            if(self._recharge_time == 0):
                self._recharge_time = self._recharge
        effect_function = effects[self._effect]
        effect_function(target, world)
    