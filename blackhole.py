# The Black_Hole class is derived from Simulton; it updates by finding+removing
#   any class derived from Prey whose center is contained inside its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Black_Hole.radius*2,Black_Hole.radius*2)
    def update(self,model):
        eaten = model.find(lambda s: (isinstance(s,Prey) and self.contains(s.get_location())))
        for i in eaten:
            model.remove(i)
        return eaten
    def display(self,the_canvas):
        x,y = self.get_location()
        w,h = self.get_dimension()
        the_canvas.create_oval(x-w/2,y-h/2, x+w/2, y+h/2, fill='#000')
    def contains(self, xy):
        w,_ = self.get_dimension()
        return self.distance(xy) < w/2
            