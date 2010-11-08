from Edit.Helper import *
"""
        id: ID_,
        depth: "min", 
        ac: "0",
        speed: "0",
        max_hp: "0",
        max_sp: "0",
        experience: "0",
        attacks: [],
        spells: [],
        resists: [],
        drops: [],
        vulnerabilities: [],
        immunities: [],
        flags: [],
        killed: False,
        
"""

class Creature(object):
    def __init__(self, creature_info):
        if(id in creature_info): self._x = creature_info[x]
        if(depth in creature_info): self._x = creature_info[x]
        if(ac in creature_info): self._x = creature_info[x]
        if(speed in creature_info): self._x = creature_info[x]
        if(max_hp in creature_info): self._x = creature_info[x]
        if(max_sp in creature_info): self._x = creature_info[x]
        if(experience in creature_info): self._x = creature_info[x]
        if(attacks in creature_info): self._x = creature_info[x]
        if(spells in creature_info): self._x = creature_info[x]
        if(resists in creature_info): self._x = creature_info[x]
        if(drops in creature_info): self._x = creature_info[x]
        if(vulnerabilities in creature_info): self._x = creature_info[x]
        if(immunities in creature_info): self._x = creature_info[x]
        if(flags in creature_info): self._x = creature_info[x]
        if(killed in creature_info): self._x = creature_info[x]
