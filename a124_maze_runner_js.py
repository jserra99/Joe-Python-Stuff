import turtle as tt
import random as rng

wn = tt.Screen()
wn.bgcolor("black")
walls = tt.Turtle()
runner = tt.Turtle()
wallLength = 25
doorLength = 15
barrierLength = 30
walls.color("white")
walls.speed(11)

def makeBarrier(amount):
    walls.forward(amount)
    walls.left(90)
    walls.forward(barrierLength)
    walls.back(barrierLength)
    walls.right(90)

def makeDoor(amount):
    walls.forward(amount)
    walls.pu()
    walls.forward(doorLength)
    walls.pd()

def runnerDown():
    runner.setheading(270)
    runner.forward(5)

def runnerUp():
    runner.setheading(90)
    runner.forward(5)

def runnerRight():
    runner.setheading(0)
    runner.forward(5)

def runnerLeft():
    runner.setheading(180)
    runner.forward(5)

#Making the Maze
for i in range(25):
    walls.left(90)
    if (i < 1):
        walls.forward(wallLength) #Default Wall
    elif (i < 5): #Wall with a door
        j = rng.randint(0, wallLength - doorLength)
        makeDoor(j)
        walls.forward(wallLength-j-doorLength)
    else: #Wall with a barrier and a door
        if (rng.randint(0,1) == 1):
            k = rng.randint(0,wallLength-doorLength)
            makeBarrier(k)
            z = rng.randint(0,wallLength-doorLength-k)
            makeDoor(z)
            walls.forward(wallLength-k-z-doorLength)
        else: #Wall with a door and a barrier
            k = rng.randint(0,wallLength-doorLength)
            makeBarrier(k)
            z = rng.randint(0,wallLength-doorLength-k)
            makeDoor(z)
            walls.forward(wallLength-k-z-doorLength)
    wallLength += 15
walls.hideturtle()

#Maze runner code
runner.pu()
runner.goto(0, 250)
runner.pd()
runner.color("red")
wn.onkeypress(runnerDown, "s")
wn.onkeypress(runnerUp, "w")
wn.onkeypress(runnerRight, "d")
wn.onkeypress(runnerLeft, "a")

wn.listen()
wn.mainloop()