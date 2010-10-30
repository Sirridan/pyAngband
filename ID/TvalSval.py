TV_NONE = 'none'
TV_JUNK = 'junk'
TV_POTION = 'potion'
TV_SCROLL = 'scroll'
TV_WAND = 'wand'
TV_ROD = 'rod'
TV_CHEST = 'chest'
TV_SWORD = 'sword'
TV_HAFTED = 'hafted'
TV_POLEARM = 'polearm'


#sval dictionary, if a Tval isn't in there, then it's items are decided by a function or
#somewhere else. Such as chests, scrolls, wands, etc.
SVAL = {
	TV_SWORD: ["Long Sword", "Dagger", "Short Sword", "Blade of Chaos"],
	TV_HAFTED: ["Mace", "Warhammer", "Mace of Disruption", "Two-Handed Great Flail"],
	TV_POLEARM: ["Waraxe", "Greataxe", "Lucerne Hammer"],
	}
