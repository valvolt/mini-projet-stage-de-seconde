# Chargement de la librairie 'pygame'
import pygame
# librairie qui sert à choisir des nombres aléatoires
import random

# Couleur de fond d'écran
white = (255, 255, 255)
# Couleurs pour notre bouton RELANCER
button_color = (100, 100, 100)
text_color = (0, 0, 0)

# Initialization de pygame
pygame.init()

# On crée une fenêtre de 800 pixels de long et de 600 pixels de haut qui contiendra notre jeu
win_size = (800, 600)
screen = pygame.display.set_mode(win_size)
pygame.display.set_caption("1000 Sabords !!!")

# dictionnaire qui associe une 'clé' (nombre de 1 à 6) à une 'valeur' (nom de l'image)
images = {
    1: pygame.image.load('diamant.png'),
    2: pygame.image.load('piece_or.png'),
    3: pygame.image.load('singe.png'),
    4: pygame.image.load('perroquet.png'),
    5: pygame.image.load('sabre.png'),
    6: pygame.image.load('tete_de_mort.png')
}

# Fonction pour lancer le dé
def lancer_de():
    return random.randint(1, 6)

# Initialisation de la face du dé (on le lance une fois)
de_1 = lancer_de()

# Définir les dimensions et la position du bouton, nécessaire pour savoir quand on clique dessus
# Explications:
#  200: position du bouton par rapport au bord gauche
#  50: position du bouton par rapport au haut de la fenêtre
#  100: longueur du bouton
#  50: hauteur du bouton
bouton_relancer = pygame.Rect(200, 50, 150, 50)

# Si on ne fait rien de spécial le programme va se terminer immédiatement.
# On crée donc une boucle infinie qui s'arrêtera quand on ferme la fenêtre avec la croix
running = True
while running:
    for event in pygame.event.get():
        # Faire une action (cliquer, appuyer sur une touche) s'appelle un 'event' (événement)
        # On regarde à chaque tour de boucle si on a cliqué sur la croix (événement 'QUIT')
        if event.type == pygame.QUIT:
            running = False
        # On teste si un bouton est cliqué (événement 'MOUSEBUTTONDOWN')
        # (le mot-clé 'elif' est la même chose que 'else if', ca doit vous aider à comprendre où placer ce code)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # à cet endroit dans le code, on sait que la souris a été cliquée. On teste pour savoir si on a cliqué sur le bouton RELANCER
            if bouton_relancer.collidepoint(event.pos):
                # à cet endroit dans le code, on sait qu'on a cliqué sur le bouton RELANCER. Reste à assigner une nouvelle face à notre dé
                de_1 = lancer_de()  # Relancer le dé

    # On dessine sur l'écran (pour le moment juste un fond blanc)
    screen.fill(white)

    # Afficher le dé (attention cette partie doit être dans la boucle infinie)
    # Explications:
    #   image[de_1] : récupère l'image dans le dictionnaire correspondant au numéro aléatoire
    #   pygame.transform.scale(..., (50, 50)) : redimensionne l'image à la taille de 50x50 pixels
    #   screen.blit(..., (30, 60)) : positionne l'image à 30 pixels du bord gauche et à 60 pixels du haut de l'écran
    screen.blit(pygame.transform.scale(images[de_1], (50, 50)), (30, 60))

    # Afficher le bouton RELANCER:
    # on affiche un rectangle gris de la taille de notre bouton
    pygame.draw.rect(screen, button_color, bouton_relancer)
    # on choisit une police de taille 36 pour écrire en grosses lettres
    font = pygame.font.Font(None, 36)
    # on crée une variable text_surf qui contiendra le texte RELANCER
    text_surf = font.render("RELANCER", True, text_color)
    # on définit un que notre texte doit être centré sur notre bouton
    text_rect = text_surf.get_rect(center=bouton_relancer.center)
    # enfin, on affiche le texte centré par-dessus le rectangle gris
    screen.blit(text_surf, text_rect)

    # On rafraichit l'écran (on affiche le nouvel écran à la place de l'ancien)
    pygame.display.flip()

# Si on arrive ici c'est qu'on a quitté le jeu (on est donc sorti de la boucle infinie)
# On ferme le programme proprement
pygame.quit()
