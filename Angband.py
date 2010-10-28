#This is it, real and true Angband
import Dungeon, Effects, Status
import Creature, Monster, Player
import Item, Armor, Weapon, Ego, Artifact #move this to a seperate thing?


def create_game_session():
    return Angband()

class Angband(object):
    """The Angband class, this is the 'game', it controls everything and does everything."""
    def __init__(self):
        self._key_queue = []
        self._player = Player.Player()

    def add_key(self, key):
        self._key_queue.append(key)
    
    def process_world(self):
        """This is where everything happens"""
        
