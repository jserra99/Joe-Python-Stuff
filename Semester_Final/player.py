import time, os, winsound, pygame as pg

def start(selected_song):
    #code to start the game goes here
    pg.font.init()
    if selected_song == 'megalovania':
        mega_start()
    else:
        normal_font = pg.freetype.SysFont("Comic Sans MS", 30)
    play_song(selected_song)
    pass

def play_song(song):
    current_folder = os.path.dirname(os.path.realpath(__file__))
    song_path = str(current_folder + f"\\songs\\{song}.wav")
    if os.path.isfile(song_path) == True:
        winsound.PlaySound(song_path, winsound.SND_ASYNC)
        print("Beginning playback...")
    else:
        print("Please put your song in a folder named 'songs' in this file's folder.")

def mega_start():
    mega_font = pg.freetype.Font(os.path.dirname(os.path.realpath(__file__) + "\\resources\\undertale_font.ttf"), 30)


'''def pause(paused):
    if paused == False:
        paused = True
        #Code to pause the game goes here
    else:
        paused = False
        #Code to resume the game goes here'''