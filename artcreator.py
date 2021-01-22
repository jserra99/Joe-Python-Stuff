#Importing necessary modules
import pygame as pg
import pyautogui as ag
import time, os

#Asking for some user input
pen_colors = ['white', 'red', 'green', 'blue', 'yellow', 'orange', 'purple', 'black']
background = input("What color would you like the canvas background color to be? : ")
pen_option = pen_colors.index(input("Which color would you like? {} : ".format(pen_colors)))

#Setting up the game
x, y = ag.size()
pg.init()
size = width, height = x, y
screen = pg.display.set_mode(size)
screen.fill(background)
pg.display.set_caption("Artcreator")
pensize = 5

def take_screenshot():
    file_extension = 0
    folder_path = os.path.dirname(os.path.realpath(__file__))
    myScreenShot = ag.screenshot()
    try:
        os.mkdir(folder_path + "\\artwork")
    except:
        pass
    while True:
        target = str(folder_path + "\\artwork\\art_piece{}.png".format(file_extension))
        if os.path.isfile(target) == True:
            file_extension += 1
        else:
            myScreenShot.save(target)
            break

#Giving some instructions to the artist
print("Hold Left Click to draw and Right Click to erase.\nPress 1 & 2 to cycle pen colors.\nPress W & S to increase or decrease the pensize.\nTo save a screenshot of your work press space.")

#While loop that constantly checks for events
while True:
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
            if event.key == pg.K_1:
                if pen_option == 0:
                    pen_option = (len(pen_colors) - 1)
                else:
                    pen_option -= 1
                print("Your new color is:", pen_colors[pen_option])
            elif event.key == pg.K_2:
                if pen_option == (len(pen_colors) - 1):
                    pen_option = 0
                else:
                    pen_option += 1
                print("Your new color is:", pen_colors[pen_option])
            elif event.key == pg.K_w:
                pensize += 1
                print("Pensize increased by 1.")
            elif event.key == pg.K_s:
                if pensize != 1:
                    pensize -= 1
                    print("Pensize decreased by 1.")
                else:
                    print("Pensize already at maximum smallest width.")
            elif event.key == pg.K_SPACE:
                take_screenshot()

    pg.display.update()
