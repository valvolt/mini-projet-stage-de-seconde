# Chargement de la librairie 'pygame'
import pygame
# librairie qui sert à choisir des nombres aléatoires
import random

# Couleur de fond d'écran
white = (255, 255, 255)
# Couleurs pour notre bouton RELANCER
button_color = (100, 100, 100)
text_color = (0, 0, 0)
# couleurs des bords des dés
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)

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
de_2 = lancer_de()
de_3 = lancer_de()
de_4 = lancer_de()
de_5 = lancer_de()
de_6 = lancer_de()
de_7 = lancer_de()
de_8 = lancer_de()

# Initialiser la couleur du bord
# Cas particulier: le dé tombe directement sur une tête de mort
if de_1 == 6:
  couleur_de_1 = black
else:
  couleur_de_1 = green
if de_2 == 6:
  couleur_de_2 = black
else:
  couleur_de_2 = green
if de_3 == 6:
  couleur_de_3 = black
else:
  couleur_de_3 = green
if de_4 == 6:
  couleur_de_4 = black
else:
  couleur_de_4 = green
if de_5 == 6:
  couleur_de_5 = black
else:
  couleur_de_5 = green
if de_6 == 6:
  couleur_de_6 = black
else:
  couleur_de_6 = green
if de_7 == 6:
  couleur_de_7 = black
else:
  couleur_de_7 = green
if de_8 == 6:
  couleur_de_8 = black
else:
  couleur_de_8 = green

# Définir les rectangles pour chaque dé pour détecter les clics
rect_de_1 = pygame.Rect(29, 59, 52, 52)
rect_de_2 = pygame.Rect(81, 59, 52, 52)
rect_de_3 = pygame.Rect(133, 59, 52, 52)
rect_de_4 = pygame.Rect(185, 59, 52, 52)
rect_de_5 = pygame.Rect(237, 59, 52, 52)
rect_de_6 = pygame.Rect(289, 59, 52, 52)
rect_de_7 = pygame.Rect(341, 59, 52, 52)
rect_de_8 = pygame.Rect(393, 59, 52, 52)

# Définir les dimensions et la position du bouton, nécessaire pour savoir quand on clique dessus
# Explications:
#  200: position du bouton par rapport au bord gauche
#  50: position du bouton par rapport au haut de la fenêtre
#  100: longueur du bouton
#  50: hauteur du bouton
bouton_relancer = pygame.Rect(450, 50, 150, 50)

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
                if couleur_de_1 == green:
                  de_1 = lancer_de()  # Relancer le dé
                  if de_1 == 6:
                      couleur_de_1 = black
                if couleur_de_2 == green:
                  de_2 = lancer_de()  # Relancer le dé
                  if de_2 == 6:
                      couleur_de_2 = black
                if couleur_de_3 == green:
                  de_3 = lancer_de()  # Relancer le dé
                  if de_3 == 6:
                      couleur_de_3 = black
                if couleur_de_4 == green:
                  de_4 = lancer_de()  # Relancer le dé
                  if de_4 == 6:
                      couleur_de_4 = black
                if couleur_de_5 == green:
                  de_5 = lancer_de()  # Relancer le dé
                  if de_5 == 6:
                      couleur_de_5 = black
                if couleur_de_6 == green:
                  de_6 = lancer_de()  # Relancer le dé
                  if de_6 == 6:
                      couleur_de_6 = black
                if couleur_de_7 == green:
                  de_7 = lancer_de()  # Relancer le dé
                  if de_7 == 6:
                      couleur_de_7 = black
                if couleur_de_8 == green:
                  de_8 = lancer_de()  # Relancer le dé
                  if de_8 == 6:
                      couleur_de_8 = black
            elif rect_de_1.collidepoint(event.pos):
                # on a cliqué sur le dé numéro 1
                if couleur_de_1 == green:
                    couleur_de_1 = red
                elif couleur_de_1 == red:
                    couleur_de_1 = green
            elif rect_de_2.collidepoint(event.pos):
                # on a cliqué sur le dé numéro 2
                if couleur_de_2 == green:
                    couleur_de_2 = red
                elif couleur_de_2 == red:
                    couleur_de_2 = green
            elif rect_de_3.collidepoint(event.pos):
                # on a cliqué sur le dé numéro 3
                if couleur_de_3 == green:
                    couleur_de_3 = red
                elif couleur_de_3 == red:
                    couleur_de_3 = green
            elif rect_de_4.collidepoint(event.pos):
                # on a cliqué sur le dé numéro 4
                if couleur_de_4 == green:
                    couleur_de_4 = red
                elif couleur_de_4 == red:
                    couleur_de_4 = green
            elif rect_de_5.collidepoint(event.pos):
                # on a cliqué sur le dé numéro 5
                if couleur_de_5 == green:
                    couleur_de_5 = red
                elif couleur_de_5 == red:
                    couleur_de_5 = green
            elif rect_de_6.collidepoint(event.pos):
                # on a cliqué sur le dé numéro 6
                if couleur_de_6 == green:
                    couleur_de_6 = red
                elif couleur_de_6 == red:
                    couleur_de_6 = green
            elif rect_de_7.collidepoint(event.pos):
                # on a cliqué sur le dé numéro 7
                if couleur_de_7 == green:
                    couleur_de_7 = red
                elif couleur_de_7 == red:
                    couleur_de_7 = green
            elif rect_de_8.collidepoint(event.pos):
                # on a cliqué sur le dé numéro 8
                if couleur_de_8 == green:
                    couleur_de_8 = red
                elif couleur_de_8 == red:
                    couleur_de_8 = green

    # On dessine sur l'écran (pour le moment juste un fond blanc)
    screen.fill(white)

    # Dessiner le carré vert derrière le dé_1
    pygame.draw.rect(screen, couleur_de_1, pygame.Rect(29, 59, 52, 52))
    pygame.draw.rect(screen, couleur_de_2, pygame.Rect(81, 59, 52, 52))
    pygame.draw.rect(screen, couleur_de_3, pygame.Rect(133, 59, 52, 52))
    pygame.draw.rect(screen, couleur_de_4, pygame.Rect(185, 59, 52, 52))
    pygame.draw.rect(screen, couleur_de_5, pygame.Rect(237, 59, 52, 52))
    pygame.draw.rect(screen, couleur_de_6, pygame.Rect(289, 59, 52, 52))
    pygame.draw.rect(screen, couleur_de_7, pygame.Rect(341, 59, 52, 52))
    pygame.draw.rect(screen, couleur_de_8, pygame.Rect(383, 59, 52, 52))

    # Afficher le dé (attention cette partie doit être dans la boucle infinie)
    # Explications:
    #   image[de_1] : récupère l'image dans le dictionnaire correspondant au numéro aléatoire
    #   pygame.transform.scale(..., (50, 50)) : redimensionne l'image à la taille de 50x50 pixels
    #   screen.blit(..., (30, 60)) : positionne l'image à 30 pixels du bord gauche et à 60 pixels du haut de l'écran
    screen.blit(pygame.transform.scale(images[de_1], (50, 50)), (30, 60))
    screen.blit(pygame.transform.scale(images[de_2], (50, 50)), (82, 60))
    screen.blit(pygame.transform.scale(images[de_3], (50, 50)), (134, 60))
    screen.blit(pygame.transform.scale(images[de_4], (50, 50)), (186, 60))
    screen.blit(pygame.transform.scale(images[de_5], (50, 50)), (238, 60))
    screen.blit(pygame.transform.scale(images[de_6], (50, 50)), (290, 60))
    screen.blit(pygame.transform.scale(images[de_7], (50, 50)), (342, 60))
    screen.blit(pygame.transform.scale(images[de_8], (50, 50)), (394, 60))

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
