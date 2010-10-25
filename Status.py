#Status.py
import LivingThing, Utils, Effects

MAXSTATUSES = 42

(STR,
INT,
WIS,
DEX,
CON,
CHA,
AC,
TO_HIT_MELEE,
TO_HIT_RANGED,
TO_DMG_MELEE,
TO_DMG_RANGED,
SPEED,
HP,
SP,
LEVEL,
EXP,
MAXEXP,
GOLD,
TURNS,
ACTIVE_TURNS,
MAX_DEPTH,
BLOWS,
SHOTS,
INRAVISION,
BURDEN,
SAVING_THROW,
STEALTH,
FIGHTING,
SHOOTING,
DISARMING,
MAGIC_DEVICE,
PERCEPTION,
SEARCHING,
TUNNELING,
SHOT_POWER,
#Negative statuses here
KO,
PARALYZED,
CONFUSED,
STUNNED,
POISONED,
HALLUCINATING,
BLIND) = range(MAXSTATUSES)


class Stats(object):
    #The standard six character statistics
    def __init__(self, strength, intelligence, wisdom, dexterity, constitution, charisma):
        self._stats =    {    "str" : strength,
                            "int" : intelligence,
                            "wis" : wisdom,
                            "dex" : dexterity,
                            "con" : constitution,
                            "cha" : charisma
                        }

    def set_stat(self, stat, value):
        self._stats[stat] = value
    def get_stat(self, stat):
        return self._stats[stat]
    
class Status(object):
    #This is the status of a creature or player
    #It is the snapshot of everything a creature is at any given moment
    
    def __init__(self, copy_status = None):
        if(copy_status == None):
            self._stats = Stats(0, 0, 0, 0, 0, 0)
            self._resists = Effects.Resists()
            self._status = {}
        else: #copy constructor
            pass
        