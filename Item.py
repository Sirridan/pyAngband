import Thing, Status

class Item(Thing.Thing):
    def __init__(self, id):
        super(Item, self).__init__(id)
        self._thrown_damage = "1d2"
        self._weight = 0
        self._value = 0
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