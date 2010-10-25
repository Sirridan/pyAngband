class Thing(object):
    def __init__(self, id):
        self._map_x = 0
        self._map_y = 0
        self._id = id
    
    def get_xy(self):
        return (self._map_x, self._map_y)
    def set_x(self, x):
        self._map_x = x
    def set_y(self, y):
        self._map_y = y
    def set_xy(self, x, y):
        self._map_x = x
        self._map_y = y
