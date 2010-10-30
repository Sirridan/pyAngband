import Status
#later, we must create a "make" function which takes a base item and copies it, think of it like
#c-Angband's item_kind types

class Item(object):
    def __init__(self, id):
        self._id = id
        self._thrown_damage = "1d2"
        self._weight = 0
        self._value = 0
        self._rarity = 0
        self._depth = 0
        self._resists = None    #elements this item is resistant to
                                #unlike regular v, this can mean that items may resist
                                #or are completely immune
        
class EquipableItem(Item):
    def __init__(self, id):
        super(EquipableItem, self).__init__(id)
    
    def apply_stats(self, status):
        new_status = Status.Status(status)
        #apply changes from this item to new_status here
        return new_status

class ConsumableItem(Item):
    def __init__(self, id):
        super(ConsumableItem, self).__init__(id)
        self._use_function = None #get it later
    def use(self, world, target):
        self._use_function(self, world, target)

