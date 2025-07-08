import random
import pygame
import hauteur_bloc
import texture_manager
import os


#manque de commentaires


ALPHA = (255, 255, 255)
SPEED = 0.1

def changeskin(pressed,player):
    if pressed[pygame.K_1]==True:
        player.images = []
        img = pygame.image.load(os.path.join('assets/slime_bleu'+ '.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        player.images.append(img)
        player.image = player.images[0]
        player.image = pygame.transform.scale(player.image, (82, 82))
    if pressed[pygame.K_2]==True:
        player.images = []
        img = pygame.image.load(os.path.join('assets/slime_rouge'+ '.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        player.images.append(img)
        player.image = player.images[0]
        player.image = pygame.transform.scale(player.image, (82, 82))
    if pressed[pygame.K_3]==True:
        player.images = []
        img = pygame.image.load(os.path.join('assets/slime_dead'+ '.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        player.images.append(img)
        player.image = player.images[0]
        player.image = pygame.transform.scale(player.image, (82, 82)) 

def handle_movement(pressed, player):
    global cameraOffset, playerScreenPos
    if player.rect.x > 100:
        player.rect.x += (pressed[pygame.K_d] - pressed[pygame.K_q]) * SPEED
    player.rect.y += pressed[pygame.K_s] * SPEED
    player.rect.y += -pressed[pygame.K_z] * SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('assets/slime_bleu'+ '.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, (82, 82)) 
        self.rect = self.image.get_rect()
