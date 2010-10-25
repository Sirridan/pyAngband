import Thing, Effects, Utils
class LivingThing(Thing.Thing):
    def __init__(self, id):
        super(LivingThing, self).__init__(id)
        self._timed_effects = {}
        self._status = {}
        self._speed = 0
        self._energy = 0
    def add_timed_effect(self, effect, duration, stacks = False):
        if(effect in self._timed_effects):
            if(self._timed_effects[effect] == None):
                #add effect if it's empty
                self._timed_effects[effect] = Effect(effect, duration)
            elif(stacks):
                #increase duration if and only if the effect can stack with itself
                #things like paralyze don't stack
                self._timed_effects[effect].increase_duration(duration)
        else:
            #otherwise just add it if it's never been here before.
            self._timed_effects[effect] = Effect(effect, duration)
    def affect(self, effect):
        #actually change the living thing's status object.
        #it is changed or created in the do_calcs function
        pass
        
    def get_status(self):
        #return the status of this living thing
        return None