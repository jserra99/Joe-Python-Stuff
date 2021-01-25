'''
Does work on macOS but due to some differences with windows such as the way it handles directories causes some features
to break, ie: the screenshot function which saves to the wrong place on macOS, 
right clicking with the trackpad also does not seem to work. Requires pygame and pyautogui.
Make sure to run this on your largest monitor.
'''

#Importing necessary modules
import pygame as pg
import pyautogui as ag
import time, os

#Asking for some user input
pen_colors = ['white', 'red', 'green', 'blue', 'yellow', 'orange', 'purple', 'black']
background = input("What color would you like the canvas background color to be? : ")
pen_option = pen_colors.index(input(f"Which color would you like? {pen_colors} : "))

#Setting up the game
x, y = ag.size()
pg.init()
size = width, height = x, y
screen = pg.display.set_mode(size)
screen.fill(background)
pg.display.set_caption("Artcreator")
pensize = 5

def take_screenshot():
    '''Takes a screenshot of your art and saves it to a created folder.'''
    file_extension = 0
    folder_path = os.path.dirname(os.path.realpath(__file__)) #Gets the path of the directory where this python file is located
    myScreenShot = ag.screenshot()
    try: #Makes the artwork directory in the python file's directory if it does not exist
        os.mkdir(folder_path + "\\artwork")
    except:
        pass
    while True:
        #Checks if a given art piece extension number is already taken, if not then it takes the screenshot underneath that name
        target = str(folder_path + f"\\artwork\\art_piece{file_extension}.png")
        if os.path.isfile(target) == True:
            file_extension += 1
        else:
            myScreenShot.save(target)
            print("Taking screenshot...")
            break

#Giving some instructions to the artist
print("Hold Left Click to draw and Right Click or Delete to erase.\nPress A & D to cycle pen colors.\nPress W & S to increase or decrease the pensize.\nTo save a screenshot of your work press space.")

while True: #While loop that constantly checks for events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        #Mouse events
        elif pg.mouse.get_pressed() == (1, 0, 0):
            mouse_pos = pg.mouse.get_pos()
            pg.draw.circle(screen, pen_colors[pen_option], mouse_pos, pensize)
        elif pg.mouse.get_pressed() == (0, 0, 1):
            mouse_pos = pg.mouse.get_pos()
            pg.draw.circle(screen, background, mouse_pos, (pensize * 2))
        #Keyboard events
        if event.type == pg.KEYDOWN:
            key = event.key
            if key == pg.K_a:
                if pen_option == 0:
                    pen_option = (len(pen_colors) - 1)
                else:
                    pen_option -= 1
                print("Your new color is:", pen_colors[pen_option])
            elif key == pg.K_d:
                if pen_option == (len(pen_colors) - 1):
                    pen_option = 0
                else:
                    pen_option += 1
                print("Your new color is:", pen_colors[pen_option])
            elif key == pg.K_w:
                pensize += 1
                print("Pensize increased by 1.")
            elif key == pg.K_s:
                if pensize != 1:
                    pensize -= 1
                    print("Pensize decreased by 1.")
                else:
                    print("Pensize already at maximum smallest width.")
            elif key == pg.K_SPACE:
                take_screenshot()
            elif key == pg.K_DELETE:
                screen.fill(background)
                print("Screen cleared.")

    pg.display.update()
