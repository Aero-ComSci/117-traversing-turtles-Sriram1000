import turtle as trtl

my_turtles = []

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

class turtle:
    def __init__(self, shape, color):
        self.turtle = trtl.Turtle(shape)
        self.turtle.penup()
        self.turtle.color(color)
        self.turtle.pensize(2)
        
    def main(self, startx, starty, startDir, forwardLength):
        self.turtle.goto(startx, starty)
        self.turtle.pendown()
        self.setheading(startDir)
        self.turtle.right(45)
        self.turtle.forward(forwardLength)



for s in turtle_shapes:
  t = trtl.Turtle(s)
  my_turtles.append(t)

 
startx = 0
starty = 0
variable = 0

for t in my_turtles:
  t.goto(startx, starty)
  t.right(90)     
  t.forward(50)

  if 
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()
