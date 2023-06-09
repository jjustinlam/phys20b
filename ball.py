# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10). 


from prey import Prey


class Ball(Prey): 
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self, x, y, Ball.radius*2, Ball.radius*2, 0, 5)
        Prey.randomize_angle(self)
    def update(self, model):
        Prey.move(self)
    def display(self,the_canvas):
        x,y = self.get_location()
        the_canvas.create_oval(x-Ball.radius, y-Ball.radius, x+Ball.radius, y+Ball.radius, fill='#00f')
        