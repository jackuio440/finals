import glob, os
import pygame
import random

def playmusic():
    pygame.init()
    mp3files = glob.glob(os.path.join("music", "*.mp3"))
    index = random.randint(0, len(mp3files) - 1)
    pygame.mixer.music.load(mp3files[index])
    pygame.mixer.music.play(loops=0)
    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
