#Sval.py
from ID.Tval import *

def print_item_name(tval, sval):
    if(tval not in SVAL):
        print "TVAL does not exist!"
        return
    item = SVAL[tval]
    if(sval not in item):
        print "Item not found!"
        return
    print SVAL_NAMES[item[sval]]

    


#item name is SVAL_NAMES[tval][sval]
#need to split this file into TVAL and SVAL

SVAL_NAMES = {
    TV_POTION:  (
            "Cure Light Wounds"
                ),
                
    TV_SCROLL:  (
            "Phase Door"
                ),
                
    TV_WAND:    (
            "Magic Missile"
                ),
                
    TV_ROD:     (
            "Lightning Bolt"
                ),
                
    TV_EDGED:   (
            "Long Sword",
            "Dagger",
            "Short Sword",
            "Blade of Chaos",
            "Sabre",
            "Falchion",
            "Scimitar",
            "Zweihander",
            "Executioner's Sword"
                )

}

#sval dictionary, if a Tval isn't in there, then it's items are decided by a function or
#somewhere else. Such as chests, scrolls, wands, etc.

SV_EDGED    =   (NONE, LONGSWORD, DAGGER, SHORTSWORD, BLADEOFCHAOS, SABRE, FALCHION, SCIMITAR, ZWEIHANDER, EXECUTIONERSSWORD) = range(-1, TV_EDGED_MAX)
SV_WAND     =   (NONE, WAND_MAGICMISSLE) = range(-1, TV_WAND_MAX)
SV_ROD      =   (NONE, ROD_LIGHTNINGBOLT) = range(-1, TV_ROD_MAX)
SV_POTION   =   (NONE, POT_CURELIGHTWOUNDS) = range(-1, TV_POTION_MAX)
SV_SCROLL   =   (NONE, SCR_PHASEDOOR) = range(-1, TV_SCROLL_MAX)

SVAL = {
        TV_EDGED: SV_EDGED,
        TV_POTION: SV_POTION,
        TV_ROD: SV_ROD,
        TV_SCROLL: SV_SCROLL,
        TV_WAND: SV_WAND
        }
