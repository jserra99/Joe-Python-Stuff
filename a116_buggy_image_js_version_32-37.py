import turtle as trtl

#Create a spider body
spdr = trtl.Turtle()
spdr.speed(10)
spdr.pensize(40)
spdr.circle(20)

#Create a spider head
spdr.goto(0,-25)
spdr.circle(5)

#Configuring spider legs
legs = 8
leg_len = 70
degree = 240 / legs
spdr.pensize(5)
counter = 0

#Draw Legs
while (counter < legs):
    spdr.goto(0,20)
    spdr.setheading((degree*counter)-15)
    spdr.pd()
    if (counter >= 4):
        spdr.setheading((degree*counter)-15)
        spdr.circle(100, 120)
    if (counter < 4):
        spdr.circle(-100, 120)
    spdr.pu()
    counter = counter + 1

#Draw Eyes
spdr.color('red')
x=8
for i in range (2):
    spdr.pu()
    spdr.goto(x,-30)
    spdr.pd()
    spdr.pensize(2)
    spdr.circle(5)
    x = x-20

spdr.hideturtle()
wn = trtl.Screen()
wn.mainloop()