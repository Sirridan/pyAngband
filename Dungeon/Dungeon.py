import Thing

class TerrainFlags(object):
    def __init__(self, passable = False, visible = False, lit = False):
        self._passable = passable
        self._visible = visible
        self._lit = lit
    
    def is_lit(self): return self._lit
    def is_visible(self): return self._visible
    def is_passable(self): return self._passable
    def change_lit(self, lit):
        self._lit = lit
    def change_visible(self, visible):
        self._visible = visible
    def change_passable(self, passable):
        self._passable = passable

class DungeonCell(object):
    """Container class for dungeon tiles, has the terrain, creature, items, etc."""
    def __init__(self, terrain, items = [], creature = None, gold = [], flags = None):
        self._terrain_id = terrain
        self._items = items
        self._creature = creature
        self._gold = gold
        if(flags == None):
            self._flags = TerrainFlags(False, False, False)
        else:
            self._flags = flags
    def copy(self):
        return DungeonCell(self._terrain_id, self._items, self._creature, self._gold, self._terrain_flags)
    def get_terrain_id(self): return self._terrain_id
    def get_items(self): return self._items
    def get_creature(self): return self._creature
    def get_gold(self): return self._gold
    def add_gold(self, gold):
        self._gold.append(gold)
    def set_creature(self, creature):
        #if(self._creature != None) except
        self._creature = creature
    def add_item(self, item):
        self._items.append(item)
    def change_terrain_id(self, terrain):
        self._terrain_id = terrain
    def change_flags(self, passable = None, visible = None, lit = None):
        if(passable != None): self._flags.change_passable(passable)
        if(visible != None): self._flags.change_visible(visible)
        if(lit != None): self._flags.change_lit(lit)
        
    class Dungeon(object):
        pass