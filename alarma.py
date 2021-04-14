import pygame

# Play the mp3 file

def run():
    
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/Music/alarm-clock.mp3")
    pygame.mixer.music.play()
