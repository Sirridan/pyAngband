#Effects.py
import Utils, Status

MAXEFFECTS = 18

EFF_NYI = -1
(EFF_SLOW,
EFF_BLEED,
EFF_POISON,
EFF_STUN,
EFF_BLINDNESS,
EFF_PARALYZE,
EFF_HALLUCINATE,
EFF_CONFUSE,
EFF_BLIND,
EFF_FEAR,
EFF_TERROR,
EFF_TEMP_VULNERABLE,
#beneficial
EFF_SPEED,
EFF_BERSERK,
EFF_HERO,
EFF_BLESSED,
EFF_TEMP_RESIST,
EFF_TEMP_IMMUNE) = range(MAXEFFECTS)

def do_nyi(effect, target):
    pass

def do_slow(effect, target):
    #target is a living thing
    target.affect(Status.SPEED, -10)
    effect.decrease_duration()
def do_poison(effect, target):
    #target is a living thing
    target.do_damage(1, "poison")
    effect.decrease_duration()
def do_bleed(effect, target):
    target.do_damage(1, "wound")
    effect.decrease_duration()
def do_stun(effect, target):
    magnitude = 0
    duration = effect.get_duration()
    if(duration > 200):
        target.affect(Status.KO, 1)
    elif(effect.get_duration >= 100):
        magnitude = -20
    elif(effect.get_duration > 0):
        magnitude = -10
    target.affect(Status.TO_HIT_MELEE, magnitude)
    target.affect(Status.TO_HIT_RANGED, magnitude)
    target.affect(Status.AC, magnitude)
    effect.decrease_duration()

MAXELEMENTS = 22
(ELE_ACID,
ELE_ELECTRICITY,
ELE_FIRE,
ELE_COLD,
ELE_POISON,
ELE_FEAR,
ELE_LIGHT,
ELE_DARKNESS,
ELE_BLINDNESS,
ELE_CONFUSION,
ELE_SOUND,
ELE_SHARD,
ELE_NEXUS,
ELE_NETHER,
ELE_CHAOS,
ELE_DISENCHANT,
ELE_FORCE,
ELE_INTERTIA,
ELE_TIME,
ELE_PLASMA,
ELE_GRAVITY,
ELE_PARALYZE) = range(MAXELEMENTS)
    
EffectFunction =    { EFF_NYI: do_nyi,
                      EFF_SLOW: do_slow,
                      EFF_POISON: do_poison
                    }

def get_function(effect):
    if(not effect in EffectFunction):
        return Effects.EffectFunction[Effects.EFF_NYI]
    return Effects.EffectFunction[effect]
#RESISTS CLASS
class Resists(object):

    REMOVE = 0
    ADD = 1
    def __init__(self):
        self._resists = []
        self._vulnerabilities = []
        self._immunities = []
    
    def resists(self, element):
        return (self._resists.contains(element) or self._immunities.contains(element))
    def is_immmune(self, element):
        return (self._immunities.contains(element))
    def is_vulnerable(self, element):
        return (self._vulnerabilities.contains(element))
    def normal_effect(self, element):
        return (not self.resists(element)) and (not self.is_immune(element)) and (not self.is_vulnerable(element))

    def change_resists(self, element, action):
        if(action == Resists.ADD):
            if(element in self._resists): self._resists.add(element)
        else:
            if(element in self._resists): self._resists.remove(element)
    
    def change_immunity(self, element, action):
        if(action == Resists.ADD):
            if(element in self._immunities): self._immunities.add(element)
        else:
            if(element in self._immunities): self._immunities.remove(element)
    
    def change_vulnerability(self, element, action):
        if(action == Resists.ADD):
            if(element in self._vulnerabilities): self._vulnerabilities.add(element)
        else:
            if(element in self._vulnerabilities): self._vulnerabilities.remove(element)
            
#EFFECTS CLASS
class Effect(object):
    def __init__(self, effect, duration, magnitude = 0):
        self._effect = effect
        self._duration = duration
        self._magnitude = magnitude
        self._function = Effects.get_function(self._effect)
        #self._function = Effect.EffectFunction[self._effect]
    
    def effect_do(self, target):
        self._function(self, target)
    def get_effect(self):
        return self._effect
    def get_duration(self):
        return self._duration
    def get_magnitude(self):
        return self._magnitude
    def lower_duration(self, amt = 1):
        self._duration -= amt
    def increase_duration(self, amt = 1):
        self._duration += amt