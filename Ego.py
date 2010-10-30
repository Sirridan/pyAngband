class Ego(object):
    def __init__(self, ego):
        self._id = ego['id']
	self._name = ego['name']
        self._to_hit = ego['to_hit']
        self._to_dam = ego['to_dam']
        self._resists = ego['resists']
        self._to_ac = ego['to_ac']
        self._powers = ego['powers']
        self._effect = ego['effect']
        self._charges = ego['charges']
        self._recharge = ego['recharge']
        self._tval_allowed = ego['tvals']
        
	
