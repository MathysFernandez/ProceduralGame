import pygame

#manque de commentaires

# Gestion des entrées pour déplacer la caméra
def deplacement_camera(camera_x, camera_y, player_x, player_y, vitesse_camera, donnees):
    
    touches = pygame.key.get_pressed()
    if (touches[pygame.K_d] or touches[pygame.K_RIGHT]) and player_x < donnees[1] * donnees[0] - donnees[3]:
        camera_x -= vitesse_camera
        player_x += vitesse_camera
    if (touches[pygame.K_q] or touches[pygame.K_LEFT]) and player_x > 0:
        camera_x += vitesse_camera
        player_x -= vitesse_camera
        
    
    if touches[pygame.K_s] or touches[pygame.K_DOWN]:
        camera_y -= vitesse_camera
        player_y += vitesse_camera
        
    return camera_x, camera_y, player_x, player_y