# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    
    def __init__(self,x,y):
        Floater.randomize_angle(self)
        Prey.__init__(self, x, y, 10, 10, self.get_angle(), 5)
        self._image = PhotoImage(file='ufo.gif')

        
    def update(self, model):
        prob = random()*100
        if(0<=prob<30):
            self.set_speed(random()-0.5 + self.get_speed())
            if(self.get_speed() > 7): self.set_speed(7)
            if(self.get_speed()<3): self.set_speed(3)
            self.set_angle(random()-0.5+self.get_angle())
        Prey.move(self)
        
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self._image)
