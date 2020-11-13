#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spdr = trtl.Turtle()
spdr.pensize(40)
spdr.circle(20)
legs = 6
leg_len = 70
degree = 380 / legs
spdr.pensize(5)
counter = 0
while (counter < legs):
  spdr.goto(0,0)
  spdr.setheading(degree*counter)
  spdr.forward(leg_len)
  counter = counter + 1
spdr.hideturtle()
wn = trtl.Screen()
wn.mainloop()
