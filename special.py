#The White_Hole class is derived from Black_Hole and for any Prey whose center is in its radius,
#instead of deleting the object from the simulation it creates two new objects of that same type just outside of itself.
#Every time it creates those two duplicates, it shrinks its dimensions by 1. If a Prey has already been 
#duplicated that particular object cannot be duplicated again although its duplicates can still be duplicated.
from prey import Prey
from blackhole import Black_Hole
class White_Hole(Black_Hole):
    count = dict()
    def update(self,model):
        eaten = model.find(lambda s: (isinstance(s, Prey) and self.contains(s.get_location())))
        x,y = self.get_location()
        for i in eaten:
            if(i not in self.count or self.count[i] ==0):
                model.add(type(i)(x+self.radius+1,y+self.radius+1))
                model.add(type(i)(x-self.radius-1,y-self.radius-1))
                self.count[i] = 1
                self.change_dimension(-1, -1)
        if(self.get_dimension() == (0,0)):
            model.remove(self)
        return eaten
    def display(self, the_canvas):
        x,y = self.get_location()
        w,h = self.get_dimension()
        the_canvas.create_oval(x-w/2,y-h/2, x+w/2, y+h/2, fill='#eee')