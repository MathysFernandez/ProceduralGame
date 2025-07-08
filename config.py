import pygame


# Dimension écran
def get_dimensions(): 
    largeur = pygame.display.Info().current_w
    hauteur = pygame.display.Info().current_h - 60
    return largeur, hauteur

def Titre():
    return "The lost"