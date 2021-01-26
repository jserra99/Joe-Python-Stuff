import time, os, winsound, pygame as pg, pygame.freetype

def start(selected_song, surface, display):
    #code to start the game goes here
    pg.font.init()
    if selected_song == 'megalovania':
        mega_start(surface, display)
    else:
        normal_font = pg.freetype.SysFont("Comic Sans MS", 30)
    pass
    play_song(selected_song)

def play_song(song):
    current_folder = os.path.dirname(os.path.realpath(__file__))
    song_path = str(current_folder + f"\\songs\\{song}.wav")
    if os.path.isfile(song_path) == True:
        winsound.PlaySound(song_path, winsound.SND_ASYNC)
        print("Beginning playback...")
    else:
        Exception("Please put your song in a folder named 'songs' in this file's folder.")
        pg.EXIT()
        exit()

def mega_start(surface, display):
    mega_font = pg.freetype.Font(os.path.dirname(os.path.realpath(__file__)) + "\\resources\\undertale_font.ttf", 75)
    mega_font.render_to(surface, (0, 0), "Get Ready!", fgcolor='white',)
    display.update()
    time.sleep(3.5)
    mega_font.render_to(surface, (0, 0), "Get Ready!", fgcolor='black', bgcolor='black')
    mega_font.render_to(surface, (0, 0), "You're Gonna Have a", fgcolor='white',)
    mega_font.render_to(surface, (0, 60), "Bad Time!", fgcolor='white',)
    display.update()
    time.sleep(3.5)
    mega_font.render_to(surface, (0, 0), "You're Gonna Have a", fgcolor='black', bgcolor='black')
    mega_font.render_to(surface, (0, 60), "Bad Time!", fgcolor='black', bgcolor='black')
    display.update()
