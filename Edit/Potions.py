from ID.Tval import *
from ID.Sval import *
from Effects.Effects import *
from Edit.Helper import *
#structure of this file is this:
#TVAL:
#   SVAL:
#       ITEM DATA

#items need
"""
    resists are:    FIRE, COLD, ACID, ELEC, POISON, CONFUSION, LIGHT, DARK, NEXUS, NETHER, DISENCHANTMENT
                    SOUND, PLASMA, FORCE, GRAVITY, TIME, INERTIA, SHARDS
    
    flags are:      FREE_ACTION, NO_BLINDNESS, SEE_INVIS, ESP, TUNNELING, NO_CONFUSION, REGENERATE, NO_FEAR, NO_ATTACK
                    IMPAIR_HP, IMPAIR_SP
                    
    powers are:     SHOT_POWER, BLOWS, SHOTS, STR, DEX, CON, INT, WIS, CHA, TUNNELING, INFRA, SPEED
    
    Do not need everything in the list, if the key is missing, it's okay. Just needs the first six key-value pairs.
    
    The 'created' key is only for artifacts.
    
    This dictionary of dictionaries, is the item_kind information, used to build individual item objects.

item_group = {
    TV_:   {

        SVAL:   {
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
                },

"""

potions = {
    TV_POTION:   {
        POT_CURELIGHTWOUNDS:   {
                weight: "4",
                value: "30",
                rarity: "0",
                depth: "0-15", 
                thrown_damage: "2d3",
                effect: (EFF_CURELIGHT, 0, 0)
                }
        }
}