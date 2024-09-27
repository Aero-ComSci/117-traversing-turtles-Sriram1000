import turtle as trtl

class TurtleClass:
    def __init__(self, shape, color):
        self.turtle = trtl.Turtle(shape)
        self.turtle.color(color)
    
    def main_move_function(self, startx, starty, angle):
        self.turtle.penup()
        self.turtle.goto(startx, starty)
        self.turtle.pendown()
        self.turtle.setheading(angle)
        self.turtle.forward(100)

    def get_x_pos(self):
        return self.turtle.xcor()

    def get_y_pos(self):
        return self.turtle.ycor()

turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["gold", "purple", "orange", "green", "blue", "red"]

startx = 0
starty = 0
start_angle = 45

my_turtles = []


for i in range(len(turtle_shapes)):
    my_turtle = TurtleClass(turtle_shapes[i], turtle_colors[i])

    my_turtle.main_move_function(startx, starty, start_angle)

    startx = my_turtle.get_x_pos()
    starty = my_turtle.get_y_pos()
    
    start_angle -= 45

    my_turtles.append(my_turtle)

wn = trtl.Screen()
wn.mainloop()
