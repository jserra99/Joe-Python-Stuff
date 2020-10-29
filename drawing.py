from turtle import *

speed(10)
pu()
bk(500)

def draw_square():
    pd()
    color(color_input)
    begin_fill()
    for i in range (4):
        forward(250)
        left(90)
    end_fill()
    pu()
    forward(375)

def draw_triangle():
    pd()
    color(color_input)
    begin_fill()
    for i in range (3):
        forward(250)
        left(120)
    end_fill()
    pu()
    forward(375)

def draw_circle():
    forward(125)
    pd()
    color(color_input)
    begin_fill()
    circle(125, 360)
    end_fill()
    pu()
    forward(250)

accepted_strings = {'square', 'triangle', 'circle'}

figure_input = input("What Shape should the first figure be?: ")
color_input = input("What color should the first figure be?: ")

if figure_input in accepted_strings:
    print("Drawing a %s %s." % (color_input, figure_input))
    if figure_input == 'square':
        draw_square()

    
    elif figure_input == 'triangle':
        draw_triangle()

    else:
        draw_circle() 

else:
    print("That is not a valid shape.")

figure_input = input("What Shape should the second figure be?: ")
color_input = input("What color should the second figure be?: ")
print("Drawing a %s %s." % (color_input, figure_input))

if figure_input in accepted_strings:
    print("Drawing a %s %s." % (color_input, figure_input))
    if figure_input == 'square':
        draw_square()

    
    elif figure_input == 'triangle':
        draw_triangle()

    else:
        draw_circle() 

else:
    print("That is not a valid shape.")

figure_input = input("What Shape should the third figure be?: ")
color_input = input("What color should the third figure be?: ")
print("Drawing a %s %s." % (color_input, figure_input))

if figure_input in accepted_strings:
    print("Drawing a %s %s." % (color_input, figure_input))
    if figure_input == 'square':
        draw_square()

    
    elif figure_input == 'triangle':
        draw_triangle()

    else:
        draw_circle() 

else:
    print("That is not a valid shape.")

#There is much more code space efficient ways to do this but if we're being real, this is a turtle script.

done()
