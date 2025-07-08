# musique.py
import pygame

# Initialisation de pygame mixer
pygame.mixer.init()

def jouer_musique(son):
    #Charge et joue un fichier sonore
    pygame.mixer.music.load(son)
    pygame.mixer.music.play()