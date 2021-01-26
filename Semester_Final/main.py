'''
This will be a very hard project.
'''

#Importing necessary modules
import pygame as pg, time, player, pygame.freetype

clock = 0
paused = False
available_songs = ('Megalovania')
chosen_song = input(f"Which song would you like?, {available_songs} : ").lower()
size = width, height = 600, 600
pg.init()
screen = pg.display.set_mode(size)
screen.fill('black') #Changes the background to black, this can be changed later to an image.
display = pg.display
display.set_caption('DDR 2021')
display_font = pg.freetype.SysFont("Comic Sans MS", 30)
display_font.render_to(screen, (0,0), "Press Space to Start!", fgcolor='white')


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
                display_font.render_to(screen, (0,0), "Press Space to Start!", fgcolor='black', bgcolor='black')
                player.start(chosen_song, screen, display)

    pg.display.update()
