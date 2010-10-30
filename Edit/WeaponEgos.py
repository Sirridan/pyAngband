#note when an ego (or any other) item is created, a function is called to that item
#it is in a dictionary with the EGO_ID as the key

weapon_egos = {
#	EGO_ID:	{
#		"name": "",
#		"to_hit": "0",
#		"to_dam": "0",
#		"to_ac": "0",
#		"tvals": [],
#		"resists": [],
#		"stats": {},
#		"flags": [],
#		"effect": {}
#		},
	EGO_HOLY_AVENGER:
		{
		"name": "%o (Holy Avenger)",
		"to_hit": "2d5+5",
		"to_dam": "3d5+5",
		"to_ac": "1d10",
		"tvals": ["hafted", "sword", "polearm"],
		"resists": [],
		"stats": {},
		"flags": ["blessed", "kill_undead", "kill_demon", "slay_evil"],
		"effect": {}
		},
	EGO_OF_FLAME:	{
		"name": "%o of Flame",
		"to_hit": "3d4",
		"to_dam": "3d4",
		"to_ac": "0",
		"tvals": ["hafted", "sword", "polearm", "shot", "arrow", "bolt", "digger"],
		"resists": ["fire"],
		"stats": {},
		"flags": ["brand_fire"],
		"effect": {}
		},
	EGO_OF_SPEED:	{
		"name": "%o of Speed",
		"to_hit": "0",
		"to_dam": "0",
		"to_ac": "3d3",
		"tvals": ["boots", "dragon_armor"],
		"resists": [],
		"stats": {},
		"flags": [],
		"effect": {}
		}
}
