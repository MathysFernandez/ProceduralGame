import pygame
import sys
import config
import musique
import time


class Bouton:
    def __init__(self, texte, x, y, largeur, hauteur, couleur, couleur_survol, action=None, font=None):
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.texte = texte
        self.couleur = couleur
        self.couleur_survol = couleur_survol
        self.action = action
        self.font = font or pygame.font.SysFont("Arial", 30)
        self.peut_cliquer = True  # Empêche clics multiples rapides

    def dessiner(self, surface):
        souris = pygame.mouse.get_pos()
        clic = pygame.mouse.get_pressed()

        couleur_actuelle = self.couleur_survol if self.rect.collidepoint(souris) else self.couleur
        pygame.draw.rect(surface, couleur_actuelle, self.rect, border_radius=20)

        # Action au clic avec contrôle de répétition
        if self.rect.collidepoint(souris):
            if clic[0] and self.peut_cliquer and self.action:
                # ajouter de la musique du fond
                musique.jouer_musique("sound/clic.mp3")
                time.sleep(0.1)
                self.peut_cliquer = False
                pygame.time.set_timer(pygame.USEREVENT + 1, 300)  # Réactive clic après 300ms
                self.action()

        texte_rendu = self.font.render(self.texte, True, (0, 0, 0))
        texte_rect = texte_rendu.get_rect(center=self.rect.center)
        surface.blit(texte_rendu, texte_rect)

# Chargement du son de fond
son_fond = pygame.mixer.Sound("sound/musique-fond.mp3")
pygame.mixer.Channel(0).play(son_fond, loops=-1)

class Menu:
    def __init__(self):
        pygame.init()
        # Dimension ecran avec ajustement pour la barre des tâches
        self.largeur_ecran, self.hauteur_ecran = config.get_dimensions()
        pygame.display.set_caption("ProcéduralGame")

        # Initialisation de la fenêtre de jeu
        self.screen = pygame.display.set_mode((self.largeur_ecran, self.hauteur_ecran))

        self.fond = pygame.image.load("assets/background.jpg").convert()
        self.fond = pygame.transform.scale(self.fond, (self.largeur_ecran, self.hauteur_ecran))

        self.font_titre = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 40)
        self.font_bouton = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 25)
        self.clock = pygame.time.Clock()

        # Position centrée des boutons
        self.bouton_jouer = Bouton("Jouer", self.largeur_ecran // 2 - 100, self.hauteur_ecran // 2 - 60, 200, 60, (50, 200, 50), (100, 255, 100), self.lancer_jeu, self.font_bouton)
        self.bouton_quitter = Bouton("Quitter", self.largeur_ecran // 2 - 100, self.hauteur_ecran // 2 + 60, 200, 60, (200, 100, 200), (255, 100, 255), self.quitter, self.font_bouton)

    def lancer_jeu(self):
        import main
        main.lancer_jeu()

    def quitter(self):
        pygame.quit()
        sys.exit()

    def afficher(self):
        en_cours = True
        while en_cours:
            self.screen.blit(self.fond, (0, 0))

            # Titre centré
            titre = self.font_titre.render("ProcéduralGame", True, (119, 181, 254))
            titre_rect = titre.get_rect(center=(self.largeur_ecran // 2, 100))
            self.screen.blit(titre, titre_rect)

            # Dessiner les boutons
            self.bouton_jouer.dessiner(self.screen)
            self.bouton_quitter.dessiner(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False
                if event.type == pygame.USEREVENT + 1:
                    self.bouton_jouer.peut_cliquer = True
                    self.bouton_quitter.peut_cliquer = True

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


# Lancer le menu 

if __name__ == "__main__":
    menu = Menu()
    menu.afficher()



