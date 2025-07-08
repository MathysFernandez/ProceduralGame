import random
import pygame
import hauteur_bloc 
import texture_manager
import camera
import os
import joueur
import musique
import ecran_demarrage
import config
import time



print()
def lancer_jeu():  # AJOUT
    pygame.init()

    est_en_saut = False

    # Dimension ecran
    largeur_ecran, hauteur_ecran = config.get_dimensions()

    # Dimensions de la grille
    taille_cellule = 50

    largeur_grille = largeur_ecran // taille_cellule + 30  # +... pour bien remplir
    hauteur_grille = hauteur_ecran // taille_cellule + 15


    # Couleurs
    couleur_grille = (100, 100, 100)
    couleur_cellule = (200, 200, 200)

    #Ne pas supprimer merci
    clock = pygame.time.Clock()
    
    # Créer la fenêtre avec pour parametre (largeur et hauteur)
    fenetre = pygame.display.set_mode((largeur_ecran, hauteur_ecran))

    # Chargement du son de fond
    son_fond = pygame.mixer.Sound("sound/musique-fond.mp3")
    pygame.mixer.Channel(0).play(son_fond, loops=-1)

    # Créer la grille
    grille = [[None for _ in range(largeur_grille)] for _ in range(hauteur_grille)]

    # Appel de la fonction hauteur du fichier hauteur_bloc
    h_dep = hauteur_grille-8
    h_min = (hauteur_ecran // taille_cellule)//2
    h_max = hauteur_grille-5

    # appel de la fonction génération procédural de hauteur 
    T = hauteur_bloc.hauteur(largeur_grille, h_dep, h_max, h_min)

    # creation de la map avec Génération procédural 
    grille_textures, blocs_terre_groupe, blocs_dechet_groupe = texture_manager.placer_texture(taille_cellule, largeur_grille, hauteur_grille, T, grille)

    nb_total_dechets = len(blocs_dechet_groupe)

    # Position initiale de la caméra
    camera_x = 0
    camera_y = 0

    # Initialisation du joueur
    player = joueur.Player()  # spawn player
    player.rect.x = largeur_ecran/2  # go to x
    player.rect.y = hauteur_ecran/2  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)

    # déclaraton de l'emplacement imaginaire du joueur avec pour référentiel la grille
    # modif taille pour permettre de decendre dans une cellule
    position_player = pygame.Rect(player.rect.x, player.rect.y, taille_cellule-5, taille_cellule-5)
    # ajustabilité des positions pour la "hitbox" (jsp comment cela s'écrit mdr)
    position_player.x = player.rect.x + 17
    position_player.y = player.rect.y + 17


    donnees = [taille_cellule,largeur_grille,hauteur_grille,position_player.width]
    # Vitesse de déplacement de la caméra et joueur 
    vitesse_camera = 5
    
    #gravité
    gravity = 1
    velocity = 0

    font = pygame.font.SysFont("fonts/PressStart2P-Regular.ttf", 40)
    # Compteur de déchets ramassés
    count = 0
    
    # Boucle principale du jeu
    running = True
    while running:
        keys_pressed = pygame.key.get_pressed()
        joueur.handle_movement(keys_pressed, player)
        joueur.changeskin(keys_pressed, player)
        # gestion évènement si joueur ferme fenetre alors fermer programme
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (keys_pressed[pygame.K_z] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_SPACE]) and not est_en_saut:
                musique.jouer_musique("sound/saut.mp3")
                velocity = -13  # vitesse vers le haut
                est_en_saut = True

        # Stocker la position précédente du joueur
        ancienne_position_x = position_player.x
        ancienne_position_y = position_player.y
        ancienne_camera_x = camera_x
        ancienne_camera_y = camera_y
        
        #velocité
        if velocity >= 10 :
            velocity = 10
        else:
            velocity += gravity

        # Gestion des entrées pour déplacer la caméra et le joueur 
        camera_x, camera_y, position_player.x, position_player.y = camera.deplacement_camera(camera_x, camera_y, position_player.x, position_player.y, vitesse_camera, donnees)
        
        # Dessiner la grille en tenant compte de la position de la caméra
        fenetre.fill((0, 0, 0))
        for y in range(hauteur_grille):
            for x in range(largeur_grille):
                # Calcule la position de la cellule à l'écran en fonction de la caméra
                screen_x = x * taille_cellule + camera_x
                screen_y = y * taille_cellule + camera_y

                # Crée un objet pygame.Rect pour la position à l'écran
                rect = pygame.Rect(screen_x, screen_y, taille_cellule, taille_cellule)

                # Dessine le contour du rectangle de la cellule
                pygame.draw.rect(fenetre, couleur_cellule, rect)
                pygame.draw.rect(fenetre, couleur_grille, rect, 1)

                # Dessine la texture en fonction de la grille
                if grille[y][x] is not None:
                    fenetre.blit(grille[y][x], rect)
        
        #gravité
        #la gravité doit se passer avant la detection de sol
        position_player.y += velocity
        camera_y -= velocity
        
        # Detection de collision
        for bloc_terre in blocs_terre_groupe:
            if position_player.colliderect(bloc_terre.rect):
                #Detection collision bas 
                if velocity > 0 and ancienne_position_y + position_player.height <= bloc_terre.rect.top + 5:
                    camera_y += position_player.bottom - bloc_terre.rect.top
                    position_player.bottom = bloc_terre.rect.top
                    velocity = 0
                    est_en_saut = False  # <-- permet de resauter
                    #musique.jouer_musique("sound/atterrissage.mp3")


                #Detection collision gauche 
                elif position_player.left < bloc_terre.rect.right and ancienne_position_x >= bloc_terre.rect.right:
                    camera_x += position_player.left - bloc_terre.rect.right
                    position_player.left = bloc_terre.rect.right
                
                #Detection collision droite
                elif position_player.right > bloc_terre.rect.left and ancienne_position_x <= bloc_terre.rect.left:
                    camera_x += position_player.right - bloc_terre.rect.left
                    position_player.right = bloc_terre.rect.left
                """position_player.x = ancienne_position_x
                position_player.y = ancienne_position_y
                camera_x = ancienne_camera_x
                camera_y = ancienne_camera_y
                """
        for bloc_dechet in blocs_dechet_groupe.copy():
            if position_player.colliderect(bloc_dechet.rect):
                ciel = pygame.image.load("assets/ciel.png").convert_alpha()
                ciel = pygame.transform.scale(ciel, (taille_cellule, taille_cellule))
                i = int(bloc_dechet.rect[0] / taille_cellule)
                j = int(bloc_dechet.rect[1] / taille_cellule)
                grille[j][i] = ciel
                blocs_dechet_groupe.remove(bloc_dechet)
                count += 1
                break
                

        player_list.draw(fenetre)
        if count >= nb_total_dechets:
            texte_fin = font.render("Vous avez gagné !", True, (0, 0, 0))
            texte_rect = texte_fin.get_rect(center=(largeur_ecran // 2, hauteur_ecran // 2))
            fenetre.blit(texte_fin, texte_rect)
            pygame.display.flip()
            pygame.time.wait(3000)
            running = False
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


# === Code d’entrée principal ===
if __name__ == "__main__":
    menu = ecran_demarrage.Menu()
    menu.afficher()