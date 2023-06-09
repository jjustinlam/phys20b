# The Hunter class is derived from Pulsator and Mobile_Simulton (in that order).
#   It updates/displays like its Pulsator base, but also is mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):  
    hunt_range = 200
    def __init__(self, x,y):
        Pulsator.__init__(self, x,y)
        Mobile_Simulton.__init__(self,x,y,*self.get_dimension(), 0,5)
        self.randomize_angle()
    def update(self, model):
        prey = model.find(lambda x: (isinstance(x, Prey) and self.distance(x.get_location()) <=Hunter.hunt_range))
        if len(prey) == 0:
            self.move()
            return Pulsator.update(self,model)
        follow = min(prey, key = lambda y: self.distance(y.get_location()))
        x1,y1 = self.get_location()
        x2,y2 = follow.get_location()
        dy = y2-y1
        dx = x2 - x1
        self.set_angle(atan2(dy,dx))
        self.move()
        return Pulsator.update(self, model)
        
