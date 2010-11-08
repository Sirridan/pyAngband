#This is it, real and true Angband
from Commands import *
from Creature.Player import Player

(   AKEY_ESCAPE,
    AKEY_UP,
    AKEY_DOWN,
    AKEY_LEFT,
    AKEY_RIGHT) = range(500, 505)
    
MOVEMENT_KEYS = [AKEY_UP, AKEY_DOWN, AKEY_LEFT, AKEY_RIGHT, '1', '2', '3', '4', '5', '6', '7', '8', '9'] #redfine later in options

MOVE_UP             = [AKEY_UP, '8']
MOVE_DOWN           = [AKEY_DOWN, '2']
MOVE_LEFT           = [AKEY_LEFT, '4']
MOVE_RIGHT          = [AKEY_RIGHT, '6']
MOVE_UP_AND_LEFT    = ['7']
MOVE_UP_AND_RIGHT   = ['9']
MOVE_DOWN_AND_LEFT  = ['1']
MOVE_DOWN_AND_RIGHT = ['3']

def create_game_session():
    return Angband()

class Angband(object):
    """The Angband class, this is the 'game', it controls everything and does everything."""
    def __init__(self):
        self._key_queue = []    #keys are (key, shift, ctrl, alt, x, y) x, y are only for mouse presses
        self._player = Player()
        self._done = False

    def add_key(self, key):
        self._key_queue.append(key)
    
    def get_key(self):
        if len(self._key_queue) == 0:
            return None
        key = self._key_queue[0]
        self._key_queue = self._key_queue[1:]
        return key
        
    def unget_key(self, key):
        self._key_queue = [key].append(self._key_queue)
        
    def process_world(self):
        """This is where everything happens"""
        key = self.get_key()
        if(key == None): return
        if(key[0] in MOVEMENT_KEYS):
            pxy = self._player.get_xy()
            if(key[0] in MOVE_UP):
                self._player.set_xy(pxy[0], pxy[1] - 1)
            elif(key[0] in MOVE_DOWN):
                self._player.set_xy(pxy[0], pxy[1] + 1)
            elif(key[0] in MOVE_LEFT):
                self._player.set_xy(pxy[0] - 1, pxy[1])
            elif(key[0] in MOVE_RIGHT):
                self._player.set_xy(pxy[0] + 1, pxy[1])
            elif(key[0] in MOVE_UP_AND_LEFT):
                self._player.set_xy(pxy[0] - 1, pxy[1] - 1)
            elif(key[0] in MOVE_UP_AND_RIGHT):
                self._player.set_xy(pxy[0] + 1, pxy[1] - 1)
            elif(key[0] in MOVE_DOWN_AND_LEFT):
                self._player.set_xy(pxy[0] - 1, pxy[1] + 1)
            elif(key[0] in MOVE_DOWN_AND_RIGHT):
                self._player.set_xy(pxy[0] + 1, pxy[1] + 1)
        if(key[0] == AKEY_ESCAPE):
            self.shutdown()
    
    def get_current_display(self):
        """Get the stuff that needs displaying"""
        pxy = self._player.get_xy()
        return ('@', pxy[0], pxy[1])

    def shutdown(self):
        """Do everything that needs to be done to shutdown the game"""
        self._done = True
        
    def running(self):
        return(self._done == False)