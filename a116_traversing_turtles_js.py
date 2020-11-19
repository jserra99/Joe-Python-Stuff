#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    my_turtles.append(t)

#  Sets the starting turtle location
startx = 0
starty = 0
direction = 120
#  Goes to the previously set starting location and orients the turtle
for t in my_turtles:
    t.setheading(direction - 60)
    t.penup()
    t.goto(startx, starty)
    t.pendown()
    new_color = turtle_colors.pop()
    t.pencolor(new_color)
    t.fillcolor(new_color)
    t.forward(50)
    direction = t.heading()

#  changes the new starting position coordinates
    startx = t.xcor()
    starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
