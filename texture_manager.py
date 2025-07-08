import pygame
import random

#manque de commentaires


def placer_texture(taille_cellule,largeur_grille,hauteur_grille,T, grille):
       
    # Charger les textures
    # tentative 
    try:
        #4fichiers "herbe" différents en fonction des changements du terrain
        herbe = pygame.image.load("assets/herbe.png").convert_alpha()
        herbe = pygame.transform.scale(herbe, (taille_cellule, taille_cellule))
        herbe2 = pygame.image.load("assets/herbe2.png").convert_alpha()
        herbe2 = pygame.transform.scale(herbe2, (taille_cellule, taille_cellule))
        herbe3 = pygame.image.load("assets/herbe3.png").convert_alpha()
        herbe3 = pygame.transform.scale(herbe3, (taille_cellule, taille_cellule))
        herbe4 = pygame.image.load("assets/herbe4.png").convert_alpha()
        herbe4 = pygame.transform.scale(herbe4, (taille_cellule, taille_cellule))
        
        terre1 = pygame.image.load("assets/terre1.png").convert_alpha()
        terre1 = pygame.transform.scale(terre1, (taille_cellule, taille_cellule))
        terre2 = pygame.image.load("assets/terre2.png").convert_alpha()
        terre2 = pygame.transform.scale(terre2, (taille_cellule, taille_cellule))
        terre3 = pygame.image.load("assets/terre3.png").convert_alpha()
        terre3 = pygame.transform.scale(terre3, (taille_cellule, taille_cellule))
        terre4 = pygame.image.load("assets/terre4.png").convert_alpha()
        terre4 = pygame.transform.scale(terre4, (taille_cellule, taille_cellule))
        
        terre_liane1 = pygame.image.load("assets/terre_liane1.png").convert_alpha()
        terre_liane1 = pygame.transform.scale(terre_liane1, (taille_cellule, taille_cellule))
        terre_liane2 = pygame.image.load("assets/terre_liane2.png").convert_alpha()
        terre_liane2 = pygame.transform.scale(terre_liane2, (taille_cellule, taille_cellule))
        terre_liane3 = pygame.image.load("assets/terre_liane3.png").convert_alpha()
        terre_liane3 = pygame.transform.scale(terre_liane3, (taille_cellule, taille_cellule))
        
        ciel = pygame.image.load("assets/ciel.png").convert_alpha()
        ciel = pygame.transform.scale(ciel, (taille_cellule, taille_cellule))
        
        plante1 = pygame.image.load("assets/plante1.png").convert_alpha()
        plante1 = pygame.transform.scale(plante1, (taille_cellule, taille_cellule))
        plante2 = pygame.image.load("assets/plante2.png").convert_alpha()
        plante2 = pygame.transform.scale(plante2, (taille_cellule, taille_cellule))
        plante3 = pygame.image.load("assets/plante3.png").convert_alpha()
        plante3 = pygame.transform.scale(plante3, (taille_cellule, taille_cellule))
        plante4 = pygame.image.load("assets/plante4.png").convert_alpha()
        plante4 = pygame.transform.scale(plante4, (taille_cellule, taille_cellule))
        
        plante5 = pygame.image.load("assets/herbe&pierre1.png").convert_alpha()
        plante5 = pygame.transform.scale(plante5, (taille_cellule, taille_cellule))
        
        tombe = pygame.image.load("assets/tombe.png").convert_alpha()
        tombe = pygame.transform.scale(tombe, (taille_cellule, taille_cellule))
        
        
        animal = pygame.image.load("assets/animal.png").convert_alpha()
        animal = pygame.transform.scale(animal, (taille_cellule, taille_cellule))
        
        dechet1 = pygame.image.load("assets/dechet1.png").convert_alpha()
        dechet1 = pygame.transform.scale(dechet1, (taille_cellule, taille_cellule))
        dechet2 = pygame.image.load("assets/dechet2.png").convert_alpha()
        dechet2 = pygame.transform.scale(dechet2, (taille_cellule, taille_cellule))
        
        pierre = pygame.image.load("assets/pierre.png").convert_alpha()
        pierre = pygame.transform.scale(pierre, (taille_cellule, taille_cellule))
    
    
    #Si erreur alors informer de la provenance de l'erreur
    except pygame.error as e:
        print("Erreur lors du chargement des textures (texture_manager)")
        pygame.quit()
        exit()
    
    
    # Créer un groupe pour les blocs de terre (permettant la detection de collisions entre le sol et le joueur)
    blocs_terre_rects = pygame.sprite.Group()
    blocs_dechet_rects = pygame.sprite.Group()
    

    # Placer des textures dans la grille
    l = []
    compt = 0
    for j in range(largeur_grille):
        num_alea = random.randint(0,3)
        if compt == 1:
            compt = 2
        elif compt ==2:
            compt = 0
        
        for i in range(hauteur_grille):
            grille[i][j] = ciel
            num_alea = random.randint(0,3)
            if i+1 == T[j] and num_alea == 3 and compt == 0:
                    if random.randint(0,1) == 0:
                        grille[i][j] = dechet1
                    else:
                        grille[i][j] = dechet2
                    compt = 1
                    x = j * taille_cellule
                    y = i * taille_cellule
                    rect_dechet = pygame.Rect(x, y, taille_cellule, taille_cellule)
                    sprite_dechet = pygame.sprite.Sprite()
                    sprite_dechet.rect = rect_dechet
                    blocs_dechet_rects.add(sprite_dechet)
                    
            if i == T[j]:
                grille[i][j] = herbe
            
            if i == T[j] and j>0 and j < largeur_grille-1 and T[j-1] != T[j] and T[j] == T[j+1]:
                grille[i][j] = herbe2
            
            if i == T[j] and j>0 and j < largeur_grille-1 and T[j-1] == T[j] and T[j] != T[j+1]:
                grille[i][j] = herbe3
            
            if i == T[j] and j>0 and j < largeur_grille-1 and T[j-1] == T[j] and T[j] == T[j+1]:
                if i > 1 and (grille[i][j-1] == herbe or grille[i][j-1] == herbe2 or grille[i][j-1] == herbe3 or grille[i][j-1] == herbe4):
                    alea = random.randint(1,5)
                    if alea == 1:
                        grille[i][j] = plante1
                    elif alea == 2:
                        grille[i][j] = plante2
                    elif alea == 3:
                        grille[i][j] = plante3
                    elif alea == 4:
                        grille[i][j] = plante5
                    #rare
                    elif alea == 5:
                        rand = random.randint(1,4)
                        if rand == 1:
                            grille[i][j] = animal
                        if rand == 2:
                            grille[i][j] = plante4
                        if rand == 3:
                            grille[i][j] = tombe
                        if rand == 4:
                            grille[i][j] = herbe4
                    else:
                        grille[i][j] = herbe4
                else:
                    grille[i][j] = herbe4
            
            
            if i-1 >= T[j]:
                rando = random.randint(1,17)
                if rando <= 4:
                    grille[i][j] = terre1
                elif 5 <= rando <= 8:
                    grille[i][j] = terre2
                elif 9 <= rando <= 12:
                    grille[i][j] = terre3
                elif 13 <= rando <= 16:
                    grille[i][j] = terre4
                elif rando == 17:
                    randi = random.randint(1,3)
                    if randi == 1:
                        grille[i][j] = terre_liane1
                    elif randi == 2:
                        grille[i][j] = terre_liane2
                    elif randi == 3:
                        grille[i][j] = terre_liane3
                
                # Créer un rectangle représentant la position de la terre et l'ajoute au groupe
                x = j * taille_cellule
                y = i * taille_cellule
                rect_terre = pygame.Rect(x, y, taille_cellule, taille_cellule)
                sprite_terre = pygame.sprite.Sprite()
                sprite_terre.rect = rect_terre
                blocs_terre_rects.add(sprite_terre)
            
            if i-2 > T[j] and random.randint(0,15) == 1:
                grille[i][j] = pierre
            elif i > 0 and j > 0 and grille[i][j-1] == pierre and grille[i][j-1] == pierre and random.randint(0,2) == 1:
                grille[i][j] = pierre
            elif i > 0 and j > 0 and grille[i-1][j] == pierre and random.randint(0,3) == 1:
                grille[i][j] = pierre
            elif i > 0 and j > 0 and grille[i][j-1] == pierre and random.randint(0,3) == 1:
                grille[i][j] = pierre
              
    return grille, blocs_terre_rects, blocs_dechet_rects
