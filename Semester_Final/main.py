'''
This will be a very hard project.
'''

#Importing necessary modules
import pygame as pg, time, player

clock = 0
paused = False
available_songs = ('Megalovania')
chosen_song = input(f"Which song would you like? : {available_songs} : ").lower()
size = width, height = 600, 600
pg.init()
screen = pg.display.set_mode(size)
screen.fill('black') #Changes the background to black, this can be changed later to an image.
pg.display.set_caption('DDR 2021')


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.KEYDOWN:
            key = event.key
            '''if key == pg.K_ESCAPE:
                player.pause(paused)'''
            if key == pg.K_SPACE:
                player.start(chosen_song)
