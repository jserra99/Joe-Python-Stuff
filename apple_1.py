'''
Definitely my worst code yet. Super inefficient, the problem is making an active event handler and having that have to conform to changing inputs. 
The turtle code has no good way of doing this. I have spent about 4 hours trying to get this to work. 
Here were some more issues I was running into: you cannot pass parameters into the onkeypress event function handler so there was no 
way I could easily create one definition for all the apples. I then ran into problems with my new input intake method looping and crashing with a while loop, 
only one apple being controlled at a time, and numerous other things. I finally settled on the built in ontimer function of the turtle module. 
Which kept looping the same code over and over without crashing but did not update the code at all. As my lists were being modified outside of the ontimer loop, 
the lists it was supposed to be reading were not being properly updated by itself. Basically python interpretted it once and stored it in memory. 
Therefore all the apples work the first go around but not the second. I also had some issues where instead of giving the int of the sprite 
Y-cor it was giving me the memory address. (Very fun to deal with). 
TLDR: This technically checks off all the boxes required by pltw: It holds 5 apples, they each *contain* a letter, and (atleast the first time) when the player 
types a letter it works.
'''

#   a123_apple_1.py
import turtle as trtl
import time
import random as rng

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=607, height=406)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
font = ("Arial", 55, "bold")
labor = []
key_values = []
button_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
backup_list = button_list.copy()

apple1 = trtl.Turtle()
apple2 = trtl.Turtle()
apple3 = trtl.Turtle()
apple4 = trtl.Turtle()
apple5 = trtl.Turtle()

labor.append(apple1)
labor.append(apple2)
labor.append(apple3)
labor.append(apple4)
labor.append(apple5)
fruit_backup = labor.copy()
for fruit in labor:
  fruit.pu()


#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def exist(active_apple, key2p):
  active_apple.goto(rng.randint(-200,200), 0)
  active_apple.write(key2p, font=font)

def be_alive(active_apple, key2p):
  active_apple.clear()
  active_apple.sety(-165)
  time.sleep(1)
  active_apple.goto(rng.randint(-200,200), 0)
  my_guy = labor.index(active_apple)
  active_apple.write(key2p, font=font)

def apple11():
  global button_list
  global key_values
  del key_values[0]
  key_values.insert(0, button_list.pop())
  be_alive(apple1, key_values[0])

def apple22():
  global button_list
  global key_values
  del key_values[1]
  key_values.insert(1, button_list.pop())
  be_alive(apple2, key_values[1])

def apple33():
  global button_list
  global key_values
  del key_values[2]
  key_values.insert(2, button_list.pop())
  be_alive(apple3, key_values[2])

def apple44():
  global button_list
  global key_values
  del key_values[3]
  key_values.insert(3, button_list.pop())
  be_alive(apple4, key_values[3])

def apple55():
  global button_list
  global key_values
  del key_values[4]
  key_values.insert(4, button_list.pop())
  be_alive(apple5, key_values[4])

def checker():
  global key_values
  try:
    wn.onkeypress(apple11, key_values[0])
    wn.onkeypress(apple22, key_values[1])
    wn.onkeypress(apple33, key_values[2])
    wn.onkeypress(apple44, key_values[3])
    wn.onkeypress(apple55, key_values[4])
  except expression as identifier:
    pass


#-----function calls-----
index = 0
for fruit in labor:
  key_values.append(button_list.pop())
  fruit.pu()
  draw_apple(fruit)
  exist(fruit, key_values[index])
  index += 1

wn.ontimer(checker, 10)
wn.listen()
wn.mainloop()
