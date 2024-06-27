# Chargement de la librairie 'pygame'
import pygame
# librairie qui sert à choisir des nombres aléatoires
import random

# Couleur de fond d'écran
white = (255, 255, 255)
# Couleurs pour notre bouton RELANCER
button_color = (200, 200, 200)
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

# dictionnaire qui associe une 'clé' (nom de la carte) à une 'valeur' (nom de l'image)
cartes = {
    "pirate": pygame.image.load('pirate.png'),
    "diamant": pygame.image.load('diamant.png'),
    "piece_or": pygame.image.load('piece_or.png'),
    "perroquet_singe": pygame.image.load('perroquet_singe.png'),
    "tete_de_mort": pygame.image.load('tete_de_mort.png'),
    "2_tetes_de_mort": pygame.image.load('2_tetes_de_mort.png'),
    "coffre": pygame.image.load('coffre.png'),
    "bateau_2": pygame.image.load('bateau_2.png'),
    "bateau_3": pygame.image.load('bateau_3.png'),
    "bateau_4": pygame.image.load('bateau_4.png'),
    "gardienne": pygame.image.load('gardienne.png'),
}

jeu_de_cartes = []

# On ajoute des cartes au jeu de cartes, type par type
jeu_de_cartes.extend(["pirate"] * 2)
jeu_de_cartes.extend(["diamant"] * 5)
jeu_de_cartes.extend(["piece_or"] * 5)
jeu_de_cartes.extend(["perroquet_singe"] * 5)
jeu_de_cartes.extend(["tete_de_mort"] * 3)
jeu_de_cartes.extend(["2_tetes_de_mort"] * 3)
jeu_de_cartes.extend(["coffre"] * 4)
jeu_de_cartes.extend(["bateau_2"] * 3)
jeu_de_cartes.extend(["bateau_3"] * 2)
jeu_de_cartes.extend(["bateau_4"] * 1)
jeu_de_cartes.extend(["gardienne"] * 2)

carte_active = -1

# Multiplicateur de score
multiplicateur = 1

# mis à vrai si on tire une carte bateau
en_combat = False
# sera mis à vrai quand on a besoin de désactiver le bouton SUIVANT
blocage_suivant = False
# dés sabres à obtenir pour vaincre le bateau
sabres_necessaires = 0
# bonus du bateau
valeur_bateau = 0

# Fonction pour lancer le dé
def lancer_de():
    return random.randint(1, 6)

# Fonction pour piocher une carte
def piocher_carte():
    # on tire un numéro entre 0 (première carte) et len(jeu_de_cartes) -1
    # (la longueur (length) de notre tableau, soir le nombre total de cartes,
    # moins 1 pour tomber sur le numéro 34 au maximum)
    numero = random.randint(0, len(jeu_de_cartes) -1)
    # on renvoie la carte qui correspond
    return jeu_de_cartes[numero]

# fonction qui compte le nombre de dés sur la face 1 (diamant)
def des_face_1():
    compte = 0
    if de_1 == 1:
      compte = compte + 1
    if de_2 == 1:
      compte = compte + 1
    if de_3 == 1:
      compte = compte + 1
    if de_4 == 1:
      compte = compte + 1
    if de_5 == 1:
      compte = compte + 1
    if de_6 == 1:
      compte = compte + 1
    if de_7 == 1:
      compte = compte + 1
    if de_8 == 1:
      compte = compte + 1
    if de_9 == 1:
       compte = compte +1
    return compte

def des_face_2():
    compte = 0
    if de_1 == 2:
      compte = compte + 1
    if de_2 == 2:
      compte = compte + 1
    if de_3 == 2:
      compte = compte + 1
    if de_4 == 2:
      compte = compte + 1
    if de_5 == 2:
      compte = compte + 1
    if de_6 == 2:
      compte = compte + 1
    if de_7 == 2:
      compte = compte + 1
    if de_8 == 2:
      compte = compte + 1
    if de_9 == 2:
       compte = compte +1
    return compte

def des_face_3():
    compte = 0
    if de_1 == 3:
      compte = compte + 1
    if de_2 == 3:
      compte = compte + 1
    if de_3 == 3:
      compte = compte + 1
    if de_4 == 3:
      compte = compte + 1
    if de_5 == 3:
      compte = compte + 1
    if de_6 == 3:
      compte = compte + 1
    if de_7 == 3:
      compte = compte + 1
    if de_8 == 3:
      compte = compte + 1
    return compte

def des_face_4():
    compte = 0
    if de_1 == 4:
      compte = compte + 1
    if de_2 == 4:
      compte = compte + 1
    if de_3 == 4:
      compte = compte + 1
    if de_4 == 4:
      compte = compte + 1
    if de_5 == 4:
      compte = compte + 1
    if de_6 == 4:
      compte = compte + 1
    if de_7 == 4:
      compte = compte + 1
    if de_8 == 4:
      compte = compte + 1
    return compte

def des_face_5():
    compte = 0
    if de_1 == 5:
      compte = compte + 1
    if de_2 == 5:
      compte = compte + 1
    if de_3 == 5:
      compte = compte + 1
    if de_4 == 5:
      compte = compte + 1
    if de_5 == 5:
      compte = compte + 1
    if de_6 == 5:
      compte = compte + 1
    if de_7 == 5:
      compte = compte + 1
    if de_8 == 5:
      compte = compte + 1
    return compte

def des_face_6():
    compte = 0
    if de_1 == 6:
      compte = compte + 1
    if de_2 == 6:
      compte = compte + 1
    if de_3 == 6:
      compte = compte + 1
    if de_4 == 6:
      compte = compte + 1
    if de_5 == 6:
      compte = compte + 1
    if de_6 == 6:
      compte = compte + 1
    if de_7 == 6:
      compte = compte + 1
    if de_8 == 6:
      compte = compte + 1
    if de_9 == 6:
      compte = compte + 1
    if de_10 == 6:
      compte = compte + 1
    return compte

def serie_de_3():
    compte = 0
    if des_face_1() == 3:
      compte = compte + 1
    if des_face_2() == 3:
      compte = compte + 1
    # cas spécial perroquet / singe
    if perroquet_singe == True:
       # on compte les 3 et les 4 ensemble
       if des_face_3() + des_face_4() == 3:
          compte = compte + 1
    else:
       # cas normal, on compte séparément
      if des_face_3() == 3:
        compte = compte + 1
      if des_face_4() == 3:
        compte = compte + 1
    if des_face_5() == 3:
      compte = compte + 1
    if des_face_6() == 3:
      compte = compte + 1
    return compte

def serie_de_4():
    compte = 0
    if des_face_1() == 4:
      compte = compte + 1
    if des_face_2() == 4:
      compte = compte + 1
    # cas spécial perroquet / singe
    if perroquet_singe == True:
       # on compte les 3 et les 4 ensemble
       if des_face_3() + des_face_4() == 4:
          compte = compte + 1
    else:
       # cas normal, on compte séparément
      if des_face_3() == 4:
        compte = compte + 1
      if des_face_4() == 4:
        compte = compte + 1
    if des_face_5() == 4:
      compte = compte + 1
    if des_face_6() == 4:
      compte = compte + 1
    return compte

def serie_de_5():
    compte = 0
    if des_face_1() == 5:
      compte = compte + 1
    if des_face_2() == 5:
      compte = compte + 1
    # cas spécial perroquet / singe
    if perroquet_singe == True:
       # on compte les 3 et les 4 ensemble
       if des_face_3() + des_face_4() == 5:
          compte = compte + 1
    else:
       # cas normal, on compte séparément
      if des_face_3() == 5:
        compte = compte + 1
      if des_face_4() == 5:
        compte = compte + 1
    if des_face_5() == 5:
      compte = compte + 1
    if des_face_6() == 5:
      compte = compte + 1
    return compte

def serie_de_6():
    compte = 0
    if des_face_1() == 6:
      compte = compte + 1
    if des_face_2() == 6:
      compte = compte + 1
    # cas spécial perroquet / singe
    if perroquet_singe == True:
       # on compte les 3 et les 4 ensemble
       if des_face_3() + des_face_4() == 6:
          compte = compte + 1
    else:
       # cas normal, on compte séparément
      if des_face_3() == 6:
        compte = compte + 1
      if des_face_4() == 6:
        compte = compte + 1
    if des_face_5() == 6:
      compte = compte + 1
    if des_face_6() == 6:
      compte = compte + 1
    return compte

def serie_de_7():
    compte = 0
    if des_face_1() == 7:
      compte = compte + 1
    if des_face_2() == 7:
      compte = compte + 1
    # cas spécial perroquet / singe
    if perroquet_singe == True:
       # on compte les 3 et les 4 ensemble
       if des_face_3() + des_face_4() == 7:
          compte = compte + 1
    else:
       # cas normal, on compte séparément
      if des_face_3() == 7:
        compte = compte + 1
      if des_face_4() == 7:
        compte = compte + 1
    if des_face_5() == 7:
      compte = compte + 1
    if des_face_6() == 7:
      compte = compte + 1
    return compte

def serie_de_8():
    compte = 0
    if des_face_1() == 8:
      compte = compte + 1
    if des_face_2() == 8:
      compte = compte + 1
    # cas spécial perroquet / singe
    if perroquet_singe == True:
       # on compte les 3 et les 4 ensemble
       if des_face_3() + des_face_4() == 8:
          compte = compte + 1
    else:
       # cas normal, on compte séparément
      if des_face_3() == 8:
        compte = compte + 1
      if des_face_4() == 8:
        compte = compte + 1
    if des_face_5() == 8:
      compte = compte + 1
    if des_face_6() == 8:
      compte = compte + 1
    return compte

# Initialisation de la face du dé (on le lance une fois)
de_1 = lancer_de()
de_2 = lancer_de()
de_3 = lancer_de()
de_4 = lancer_de()
de_5 = lancer_de()
de_6 = lancer_de()
de_7 = lancer_de()
de_8 = lancer_de()
de_9 = 0
de_10 = 0

# on pioche une carte
carte_active = piocher_carte()

# # DEBUG
# de_1 = 6
# de_2 = 6
# de_3 = 6
# de_4 = 6
# de_5 = 1
# de_6 = 1
# de_7 = 1
# de_8 = 1
# de_9 = 0
# de_10 = 0
# carte_active = "pirate"

# a t'on pioché un diamant ?
if carte_active == "diamant":
  # on active le 9e dé sur la face 1 (diamant)
  de_9 = 1
# a t'on pioché une pièce ?
if carte_active == "piece_or":
  # on active le 9e dé sur la face 2 (pièce d'or)
  de_9 = 2
# a t'on pioché une tête de mort ?
if carte_active == "tete_de_mort":
  # on active le 9e dé sur la face 6 (tête de mort)
  de_9 = 6
# a t'on pioché la carte avec deux têtes de mort ?
if carte_active == "2_tetes_de_mort":
  # on active le 9e dé sur la face 6 (tête de mort)
  de_9 = 6
  # et on active le 10e dé sur la face 6 (tête de mort)
  de_10 = 6
# a t'on pioché un pirate ?
if carte_active == "pirate":
   # on double le score
   multiplicateur = 2
else:
   # on ne double pas
   multiplicateur = 1
# a t'on pioché un perroquet / singe ?
if carte_active == "perroquet_singe":
  # on stocke cette information
  perroquet_singe = True
else:
  # on mets la variable sur False pour qu'elle ne reste pas active indéfiniment
  perroquet_singe = False
# a t'on pioché la gardienne ?
if carte_active == "gardienne":
  # on stocke cette information
  gardienne = True
else:
  # on mets la variable sur False pour qu'elle ne reste pas active indéfiniment
  gardienne = False
# a t'on pioché un coffre ?
if carte_active == "coffre":
  # on stocke cette information
  coffre = True
else:
  # on mets la variable sur False pour qu'elle ne reste pas active indéfiniment
  coffre = False

# Sur l'île de la tête de mort?
if des_face_6() >= 4:
  ile_de_la_tete_de_mort = True
else:
  ile_de_la_tete_de_mort = False

# a t'on pioché une carte bateau 2 ?
if carte_active == "bateau_2":
  en_combat = True
  blocage_suivant = True
  sabres_necessaires = 2
  valeur_bateau = 200
  # on désactive l'île de la tête de mort
  ile_de_la_tete_de_mort = False
# a t'on pioché une carte bateau 3 ?
if carte_active == "bateau_3":
  en_combat = True
  blocage_suivant = True
  sabres_necessaires = 3
  valeur_bateau = 500
  # on désactive l'île de la tête de mort
  ile_de_la_tete_de_mort = False
# a t'on pioché une carte bateau 4 ?
if carte_active == "bateau_4":
  en_combat = True
  blocage_suivant = True
  sabres_necessaires = 4
  valeur_bateau = 1000
  # on désactive l'île de la tête de mort
  ile_de_la_tete_de_mort = False

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

# On stocke le contenu des variables dans un tableau
stockage = [
    (de_1, couleur_de_1),
    (de_2, couleur_de_2),
    (de_3, couleur_de_3),
    (de_4, couleur_de_4),
    (de_5, couleur_de_5),
    (de_6, couleur_de_6),
    (de_7, couleur_de_7),
    (de_8, couleur_de_8)
]
# On trie dans l'ordre croissant
stockage.sort()
# On ré-assigne les valeurs triées aux variables
(de_1, couleur_de_1), (de_2, couleur_de_2), (de_3, couleur_de_3), (de_4, couleur_de_4), (de_5, couleur_de_5), (de_6, couleur_de_6), (de_7, couleur_de_7), (de_8, couleur_de_8) = stockage

# est-on en combat?
if en_combat == True:
    # le navire est-il vaincu ?
    if des_face_5() >= sabres_necessaires:
      # le navire est vaincu.
      # on stoppe le combat
      en_combat = False
      # on débloque le bouton SUIVANT
      blocage_suivant = False
      # on bloque autant de dés 'sabre' que nécessaire
      sabres_attribues = 0
      # doit-on bloquer le de 8 ?
      if de_8 == 5: # sabre
          if sabres_attribues < sabres_necessaires:
            couleur_de_8 = black
            sabres_attribues = sabres_attribues + 1
      # doit-on bloquer le de 7 ?
      if de_7 == 5: # sabre
          if sabres_attribues < sabres_necessaires:
            couleur_de_7 = black
            sabres_attribues = sabres_attribues + 1
      # doit-on bloquer le de 6 ?
      if de_6 == 5: # sabre
          if sabres_attribues < sabres_necessaires:
            couleur_de_6 = black
            sabres_attribues = sabres_attribues + 1
      # doit-on bloquer le de 5 ?
      if de_5 == 5: # sabre
          if sabres_attribues < sabres_necessaires:
            couleur_de_5 = black
            sabres_attribues = sabres_attribues + 1
      # doit-on bloquer le de 4 ?
      if de_4 == 5: # sabre
          if sabres_attribues < sabres_necessaires:
            couleur_de_4 = black
            sabres_attribues = sabres_attribues + 1
      # doit-on bloquer le de 3 ?
      if de_3 == 5: # sabre
          if sabres_attribues < sabres_necessaires:
            couleur_de_3 = black
            sabres_attribues = sabres_attribues + 1
      # doit-on bloquer le de 2 ?
      if de_2 == 5: # sabre
          if sabres_attribues < sabres_necessaires:
            couleur_de_2 = black
            sabres_attribues = sabres_attribues + 1
      # doit-on bloquer le de 1 ?
      if de_1 == 5: # sabre
          if sabres_attribues < sabres_necessaires:
            couleur_de_1 = black
            sabres_attribues = sabres_attribues + 1

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

bouton_suivant =  pygame.Rect(610, 50, 150, 50)

# Définir les rectangles où chaque joueur entre son prénom
rect_joueur1 = pygame.Rect(150, 200, 300, 40)
rect_joueur2 = pygame.Rect(150, 260, 300, 40)
# Dimensions et position du bouton 'OK' de l'écran d'accueil
bouton_ok = pygame.Rect(250, 500, 100, 40)

# Si on ne fait rien de spécial le programme va se terminer immédiatement.
# On crée donc une boucle infinie qui s'arrêtera quand on ferme la fenêtre avec la croix
running = True

# Liste de joueurs (tableau vide)
joueurs = []
prenom1 = ""
prenom2 = ""
joueur_actif = 0

scores = []

# sera mis à vrai quand on sera dans le dernier tour
dernier_tour = False
# sera mis à vrai quand le dernier tour sera terminé
fin_du_jeu = False
# sera mis à vrai quand on a besoin de désactiver les dés
blocage_des = False
# sera mis à vrai quand on a besoin de désactiver le bouton RELANCER
blocage_relancer = False

while running:
    # Le jeu est-il terminé ?
    if fin_du_jeu == True:
       # On affiche la même chose que l'écran d'accueil, avec les scores et les mots "fin du jeu"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)

        font = pygame.font.Font(None, 36)
        text_surf = font.render("Partie Terminée", True, text_color)
        text_rect = pygame.Rect(250, 50, 100, 40)
        screen.blit(text_surf, text_rect)

        # prénom et score du premier joueur
        pygame.draw.rect(screen, green, rect_joueur1)
        text_surf = font.render(f"{prenom1} - TOTAL: {scores[0]}", True, text_color)
        text_rect = text_surf.get_rect(center=rect_joueur1.center)
        screen.blit(text_surf, text_rect)

        # prénom et score du deuxième joueur
        pygame.draw.rect(screen, green, rect_joueur2)
        text_surf = font.render(f"{prenom2} - TOTAL: {scores[1]}", True, text_color)
        text_rect = text_surf.get_rect(center=rect_joueur2.center)
        screen.blit(text_surf, text_rect)
    # A t'on au moins un joueur? On calcule la 'longueur' de notre tableau de joueurs
    elif len(joueurs) >= 1:
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
                    if ile_de_la_tete_de_mort == False:
                      # à cet endroit dans le code, on sait qu'on a cliqué sur le bouton RELANCER. Reste à assigner une nouvelle face à notre dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_relancer == False:
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
                        # On stocke le contenu des variables dans un tableau
                        stockage = [
                            (de_1, couleur_de_1),
                            (de_2, couleur_de_2),
                            (de_3, couleur_de_3),
                            (de_4, couleur_de_4),
                            (de_5, couleur_de_5),
                            (de_6, couleur_de_6),
                            (de_7, couleur_de_7),
                            (de_8, couleur_de_8)
                        ]
                        # On trie dans l'ordre croissant
                        stockage.sort()
                        # On ré-assigne les valeurs triées aux variables
                        (de_1, couleur_de_1), (de_2, couleur_de_2), (de_3, couleur_de_3), (de_4, couleur_de_4), (de_5, couleur_de_5), (de_6, couleur_de_6), (de_7, couleur_de_7), (de_8, couleur_de_8) = stockage

                        # Le joueur est-il joué par l'ordinateur ?
                        if joueurs[joueur_actif] == "ORDI_1000":
                          # Au tour de ORDI_1000
                          # On bloque les clics sur les dés (l'ordi va les lancer lui-même)
                          blocage_des = True
                          # On bloque le bouton SUIVANT
                          blocage_suivant = True
                          # A t'on perdu ou a t'on zéro dé à relancer ? Si oui on débloque le bouton SUIVANT
                          if des_face_6() >= 3:
                            blocage_suivant = False
                          elif (couleur_de_1 != green and couleur_de_2 != green and couleur_de_3 != green and couleur_de_4 != green and couleur_de_5 != green and couleur_de_6 != green and couleur_de_7 != green and couleur_de_8 != green):
                              blocage_suivant = False
                          elif en_combat == True:
                              # on passe la couleur des sabres en rouge
                              # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                              if de_1 == 5:
                                  if couleur_de_1 == green:
                                  # on bloque le dé car on en a le droit
                                    couleur_de_1 = red
                              elif couleur_de_1 == red:
                                  # ce n'est pas la bonne face, on débloque car on en a le droit
                                  couleur_de_1 = green
                              if de_2 == 5:
                                  if couleur_de_2 == green:
                                  # on bloque le dé car on en a le droit
                                    couleur_de_2 = red
                              elif couleur_de_2 == red:
                                  # ce n'est pas la bonne face, on débloque car on en a le droit
                                  couleur_de_2 = green
                              if de_3 == 5:
                                  if couleur_de_3 == green:
                                  # on bloque le dé car on en a le droit
                                    couleur_de_3 = red
                              elif couleur_de_3 == red:
                                  # ce n'est pas la bonne face, on débloque car on en a le droit
                                  couleur_de_3 = green
                              if de_4 == 5:
                                  if couleur_de_4 == green:
                                  # on bloque le dé car on en a le droit
                                    couleur_de_4 = red
                              elif couleur_de_4 == red:
                                  # ce n'est pas la bonne face, on débloque car on en a le droit
                                  couleur_de_4 = green
                              if de_5 == 5:
                                  if couleur_de_5 == green:
                                  # on bloque le dé car on en a le droit
                                    couleur_de_5 = red
                              elif couleur_de_5 == red:
                                  # ce n'est pas la bonne face, on débloque car on en a le droit
                                  couleur_de_5 = green
                              if de_6 == 5:
                                  if couleur_de_6 == green:
                                  # on bloque le dé car on en a le droit
                                    couleur_de_6 = red
                              elif couleur_de_6 == red:
                                  # ce n'est pas la bonne face, on débloque car on en a le droit
                                  couleur_de_6 = green
                              if de_7 == 5:
                                  if couleur_de_7 == green:
                                  # on bloque le dé car on en a le droit
                                    couleur_de_7 = red
                              elif couleur_de_7 == red:
                                  # ce n'est pas la bonne face, on débloque car on en a le droit
                                  couleur_de_7 = green
                              if de_8 == 5:
                                  if couleur_de_8 == green:
                                  # on bloque le dé car on en a le droit
                                    couleur_de_8 = red
                              elif couleur_de_8 == red:
                                  # ce n'est pas la bonne face, on débloque car on en a le droit
                                  couleur_de_8 = green
                          else:
                              # la partie continue !
                              # Variables pour le calcul du score
                              mult_diamants = des_face_1()
                              mult_pieces = des_face_2()
                              mult_serie_3 = serie_de_3()
                              mult_serie_4 = serie_de_4()
                              mult_serie_5 = serie_de_5()
                              mult_serie_6 = serie_de_6()
                              mult_serie_7 = serie_de_7()
                              mult_serie_8 = serie_de_8()
                              if des_face_6() == 0:
                                  mult_tresor = 1
                              else:
                                  mult_tresor = 0
                              total = (100 * mult_diamants) + (100 * mult_pieces) + (100 * mult_serie_3) + (200 * mult_serie_4) + (500 * mult_serie_5) + (1000 * mult_serie_6) + (2000 * mult_serie_7) + (4000 * mult_serie_8) + (500 * mult_tresor) + valeur_bateau
                              if mult_diamants == 9:
                                # Neuf diamants ! La partie est gagnée
                                total = 99999
                              if mult_pieces == 9:
                                # Neuf pièces ! La partie est gagnée
                                total = 99999
                              total = total * multiplicateur
                              # a t'on obtenu 1000 points?
                              if total >= 1000:
                                # on bloque le bouton RELANCER pour conserver notre score
                                blocage_relancer = True
                                # on débloque le bouton SUIVANT pour valider notre score
                                blocage_suivant = False
                              else:
                                # on n'a pas encore 1000 points et on n'a pas encore perdu.
                                # si on a déjà 3 diamants ou plus, on les conserve
                                if des_face_1() >= 3:
                                    # on passe la couleur des diamants en rouge
                                    # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                    if de_1 == 1:
                                      if couleur_de_1 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_1 = red
                                    elif couleur_de_1 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_1 = green
                                    if de_2 == 1:
                                      if couleur_de_2 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_2 = red
                                    elif couleur_de_2 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_2 = green
                                    if de_3 == 1:
                                      if couleur_de_3 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_3 = red
                                    elif couleur_de_3 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_3 = green
                                    if de_4 == 1:
                                      if couleur_de_4 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_4 = red
                                    elif couleur_de_4 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_4 = green
                                    if de_5 == 1:
                                      if couleur_de_5 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_5 = red
                                    elif couleur_de_5 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_5 = green
                                    if de_6 == 1:
                                      if couleur_de_6 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_6 = red
                                    elif couleur_de_6 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_6 = green
                                    if de_7 == 1:
                                      if couleur_de_7 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_7 = red
                                    elif couleur_de_7 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_7 = green
                                    if de_8 == 1:
                                      if couleur_de_8 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_8 = red
                                    elif couleur_de_8 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_8 = green

                                # sinon, si on a déjà 3 pièces d'or ou plus, on les conserve
                                elif des_face_2() >= 3:
                                    # on passe la couleur des pièces d'or en rouge
                                    # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                    if de_1 == 2:
                                      if couleur_de_1 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_1 = red
                                    elif couleur_de_1 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_1 = green
                                    if de_2 == 2:
                                      if couleur_de_2 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_2 = red
                                    elif couleur_de_2 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_2 = green
                                    if de_3 == 2:
                                      if couleur_de_3 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_3 = red
                                    elif couleur_de_3 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_3 = green
                                    if de_4 == 2:
                                      if couleur_de_4 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_4 = red
                                    elif couleur_de_4 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_4 = green
                                    if de_5 == 2:
                                      if couleur_de_5 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_5 = red
                                    elif couleur_de_5 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_5 = green
                                    if de_6 == 2:
                                      if couleur_de_6 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_6 = red
                                    elif couleur_de_6 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_6 = green
                                    if de_7 == 2:
                                      if couleur_de_7 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_7 = red
                                    elif couleur_de_7 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_7 = green
                                    if de_8 == 2:
                                      if couleur_de_8 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_8 = red
                                    elif couleur_de_8 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_8 = green
  
                                # sinon, si on a déjà 3 singes ou plus, on les conserve
                                elif des_face_3() >= 3:
                                    # on passe la couleur des singes en rouge
                                    # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                    if de_1 == 3:
                                      if couleur_de_1 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_1 = red
                                    elif couleur_de_1 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_1 = green
                                    if de_2 == 3:
                                      if couleur_de_2 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_2 = red
                                    elif couleur_de_2 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_2 = green
                                    if de_3 == 3:
                                      if couleur_de_3 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_3 = red
                                    elif couleur_de_3 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_3 = green
                                    if de_4 == 3:
                                      if couleur_de_4 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_4 = red
                                    elif couleur_de_4 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_4 = green
                                    if de_5 == 3:
                                      if couleur_de_5 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_5 = red
                                    elif couleur_de_5 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_5 = green
                                    if de_6 == 3:
                                      if couleur_de_6 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_6 = red
                                    elif couleur_de_6 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_6 = green
                                    if de_7 == 3:
                                      if couleur_de_7 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_7 = red
                                    elif couleur_de_7 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_7 = green
                                    if de_8 == 3:
                                      if couleur_de_8 == green:
                                        # on bloque le dé car on en a le droit
                                        couleur_de_8 = red
                                    elif couleur_de_8 == red:
                                      # ce n'est pas la bonne face, on débloque car on en a le droit
                                      couleur_de_8 = green
        
                                    # sinon, si on a déjà 3 perroquets ou plus, on les conserve
                                    elif des_face_4() >= 3:
                                        # on passe la couleur des perroquets en rouge
                                        # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                        if de_1 == 4:
                                          if couleur_de_1 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_1 = red
                                        elif couleur_de_1 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_1 = green
                                        if de_2 == 4:
                                          if couleur_de_2 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_2 = red
                                        elif couleur_de_2 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_2 = green
                                        if de_3 == 4:
                                          if couleur_de_3 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_3 = red
                                        elif couleur_de_3 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_3 = green
                                        if de_4 == 4:
                                          if couleur_de_4 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_4 = red
                                        elif couleur_de_4 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_4 = green
                                        if de_5 == 4:
                                          if couleur_de_5 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_5 = red
                                        elif couleur_de_5 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_5 = green
                                        if de_6 == 4:
                                          if couleur_de_6 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_6 = red
                                        elif couleur_de_6 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_6 = green
                                        if de_7 == 4:
                                          if couleur_de_7 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_7 = red
                                        elif couleur_de_7 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_7 = green
                                        if de_8 == 4:
                                          if couleur_de_8 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_8 = red
                                        elif couleur_de_8 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_8 = green
      
                                    # sinon, si on a déjà 3 sabres ou plus, on les conserve
                                    elif des_face_5() >= 3:
                                        # on passe la couleur des sabres en rouge
                                        # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                        if de_1 == 5:
                                          if couleur_de_1 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_1 = red
                                        elif couleur_de_1 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_1 = green
                                        if de_2 == 5:
                                          if couleur_de_2 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_2 = red
                                        elif couleur_de_2 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_2 = green
                                        if de_3 == 5:
                                          if couleur_de_3 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_3 = red
                                        elif couleur_de_3 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_3 = green
                                        if de_4 == 5:
                                          if couleur_de_4 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_4 = red
                                        elif couleur_de_4 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_4 = green
                                        if de_5 == 5:
                                          if couleur_de_5 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_5 = red
                                        elif couleur_de_5 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_5 = green
                                        if de_6 == 5:
                                          if couleur_de_6 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_6 = red
                                        elif couleur_de_6 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_6 = green
                                        if de_7 == 5:
                                          if couleur_de_7 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_7 = red
                                        elif couleur_de_7 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_7 = green
                                        if de_8 == 5:
                                          if couleur_de_8 == green:
                                            # on bloque le dé car on en a le droit
                                            couleur_de_8 = red
                                        elif couleur_de_8 == red:
                                          # ce n'est pas la bonne face, on débloque car on en a le droit
                                          couleur_de_8 = green

                        # est-on en combat?
                        if en_combat == True:
                            # le navire est-il vaincu ?
                            if des_face_5() >= sabres_necessaires:
                              # le navire est vaincu.
                              # on stoppe le combat
                              en_combat = False
                              # on débloque le bouton SUIVANT
                              blocage_suivant = False
                              # on bloque autant de dés 'sabre' que nécessaire
                              sabres_attribues = 0
                              # doit-on bloquer le de 8 ?
                              if de_8 == 5: # sabre
                                  if sabres_attribues < sabres_necessaires:
                                    couleur_de_8 = black
                                    sabres_attribues = sabres_attribues + 1
                              # doit-on bloquer le de 7 ?
                              if de_7 == 5: # sabre
                                  if sabres_attribues < sabres_necessaires:
                                    couleur_de_7 = black
                                    sabres_attribues = sabres_attribues + 1
                              # doit-on bloquer le de 6 ?
                              if de_6 == 5: # sabre
                                  if sabres_attribues < sabres_necessaires:
                                    couleur_de_6 = black
                                    sabres_attribues = sabres_attribues + 1
                              # doit-on bloquer le de 5 ?
                              if de_5 == 5: # sabre
                                  if sabres_attribues < sabres_necessaires:
                                    couleur_de_5 = black
                                    sabres_attribues = sabres_attribues + 1
                              # doit-on bloquer le de 4 ?
                              if de_4 == 5: # sabre
                                  if sabres_attribues < sabres_necessaires:
                                    couleur_de_4 = black
                                    sabres_attribues = sabres_attribues + 1
                              # doit-on bloquer le de 3 ?
                              if de_3 == 5: # sabre
                                  if sabres_attribues < sabres_necessaires:
                                    couleur_de_3 = black
                                    sabres_attribues = sabres_attribues + 1
                              # doit-on bloquer le de 2 ?
                              if de_2 == 5: # sabre
                                  if sabres_attribues < sabres_necessaires:
                                    couleur_de_2 = black
                                    sabres_attribues = sabres_attribues + 1
                              # doit-on bloquer le de 1 ?
                              if de_1 == 5: # sabre
                                  if sabres_attribues < sabres_necessaires:
                                    couleur_de_1 = black
                                    sabres_attribues = sabres_attribues + 1

                    else:
                      # Nous sommes sur l'île de la tête de mort.
                      # On compte combien de dés tête de mort on a
                      tetes_de_mort = des_face_6()
                      # On relance les dés verts
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
                      # On stocke le contenu des variables dans un tableau
                      stockage = [
                          (de_1, couleur_de_1),
                          (de_2, couleur_de_2),
                          (de_3, couleur_de_3),
                          (de_4, couleur_de_4),
                          (de_5, couleur_de_5),
                          (de_6, couleur_de_6),
                          (de_7, couleur_de_7),
                          (de_8, couleur_de_8)
                      ]
                      # On trie dans l'ordre croissant
                      stockage.sort()
                      # On ré-assigne les valeurs triées aux variables
                      (de_1, couleur_de_1), (de_2, couleur_de_2), (de_3, couleur_de_3), (de_4, couleur_de_4), (de_5, couleur_de_5), (de_6, couleur_de_6), (de_7, couleur_de_7), (de_8, couleur_de_8) = stockage

                      # A t'on au moins une tête de mort de plus ?
                      if des_face_6() > tetes_de_mort:
                         # On a une tête de mort de plus, rien de spécial, on peut continuer à relancer
                         pass
                      else:
                         # On n'a pas obtenu de nouvelle tête de mort, il faut empêcher de relancer
                         # Pour cela, on mets tous les bords de couleur à 'black'
                         couleur_de_1 = black
                         couleur_de_2 = black
                         couleur_de_3 = black
                         couleur_de_4 = black
                         couleur_de_5 = black
                         couleur_de_6 = black
                         couleur_de_7 = black
                         couleur_de_8 = black

                elif rect_de_1.collidepoint(event.pos):
                    # on a cliqué sur le dé numéro 1
                    if ile_de_la_tete_de_mort == False:
                      # On n'est pas sur l'île, on permet de bloquer le dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_des == False:
                        if couleur_de_1 == green:
                            couleur_de_1 = red
                        elif couleur_de_1 == red:
                            couleur_de_1 = green
                elif rect_de_2.collidepoint(event.pos):
                    # on a cliqué sur le dé numéro 2
                    if ile_de_la_tete_de_mort == False:
                      # On n'est pas sur l'île, on permet de bloquer le dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_des == False:
                        if couleur_de_2 == green:
                            couleur_de_2 = red
                        elif couleur_de_2 == red:
                            couleur_de_2 = green
                elif rect_de_3.collidepoint(event.pos):
                    # on a cliqué sur le dé numéro 3
                    if ile_de_la_tete_de_mort == False:
                      # On n'est pas sur l'île, on permet de bloquer le dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_des == False:
                        if couleur_de_3 == green:
                            couleur_de_3 = red
                        elif couleur_de_3 == red:
                            couleur_de_3 = green
                elif rect_de_4.collidepoint(event.pos):
                    # on a cliqué sur le dé numéro 4
                    if ile_de_la_tete_de_mort == False:
                      # On n'est pas sur l'île, on permet de bloquer le dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_des == False:
                        if couleur_de_4 == green:
                            couleur_de_4 = red
                        elif couleur_de_4 == red:
                            couleur_de_4 = green
                elif rect_de_5.collidepoint(event.pos):
                    # on a cliqué sur le dé numéro 5
                    if ile_de_la_tete_de_mort == False:
                      # On n'est pas sur l'île, on permet de bloquer le dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_des == False:
                        if couleur_de_5 == green:
                            couleur_de_5 = red
                        elif couleur_de_5 == red:
                            couleur_de_5 = green
                elif rect_de_6.collidepoint(event.pos):
                    # on a cliqué sur le dé numéro 6
                    if ile_de_la_tete_de_mort == False:
                      # On n'est pas sur l'île, on permet de bloquer le dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_des == False:
                        if couleur_de_6 == green:
                            couleur_de_6 = red
                        elif couleur_de_6 == red:
                            couleur_de_6 = green
                elif rect_de_7.collidepoint(event.pos):
                    # on a cliqué sur le dé numéro 7
                    if ile_de_la_tete_de_mort == False:
                      # On n'est pas sur l'île, on permet de bloquer le dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_des == False:
                        if couleur_de_7 == green:
                            couleur_de_7 = red
                        elif couleur_de_7 == red:
                            couleur_de_7 = green
                elif rect_de_8.collidepoint(event.pos):
                    # on a cliqué sur le dé numéro 8
                    if ile_de_la_tete_de_mort == False:
                      # On n'est pas sur l'île, on permet de bloquer le dé
                      # mais uniquement si on n'est pas bloqué
                      if blocage_des == False:
                        if couleur_de_8 == green:
                            couleur_de_8 = red
                        elif couleur_de_8 == red:
                            couleur_de_8 = green
                elif bouton_suivant.collidepoint(event.pos):
                    if blocage_suivant == False:
                      blocage_des = False
                      blocage_relancer = False
                      if ile_de_la_tete_de_mort == False:
                        # on a cliqué sur le bouton SUIVANT
                        # on stocke les points
                        scores[joueur_actif] = scores[joueur_actif] + total
                        # Si le joueur a 6000 points, on déclenche le dernier tour
                        if scores[joueur_actif] >= 6000:
                          dernier_tour = True
                      else:
                        # on enlève à chaque autre joueur 100 points par tête de mort
                        # On parcours tous les scores
                        for i in range(len(scores)):
                            # si ce n'est pas le score du joueur actif, on enlève les points
                            if i != joueur_actif:
                                scores[i] = scores[i] - (100 * des_face_6() * multiplicateur)
                                # on remet à zéro si on est tombé dans le négatif
                                if scores[i] < 0:
                                  scores[i] = 0
                      # on passe au joueur suivant
                      joueur_actif = joueur_actif + 1
                      if joueur_actif >= len(joueurs):
                        # on a fait tout le tour, on revient au début
                        joueur_actif = 0
                        if dernier_tour == True:
                            # on vient de terminer le dernier tour.
                            # on remets à False des fois que ce soit une fausse alerte
                            dernier_tour = False
                            # a t'on toujours un joueur avec 6000 points?
                            for score in scores:
                              # on regarde chaque score un par un
                              if score >= 6000:
                                # on a trouvé un haut score, on arrête le jeu
                                fin_du_jeu = True
                      # mis à vrai si on tire une carte bateau
                      en_combat = False
                      # sera mis à vrai quand on a besoin de désactiver le bouton SUIVANT
                      blocage_suivant = False
                      # dés sabres à obtenir pour vaincre le bateau
                      sabres_necessaires = 0
                      # bonus du bateau
                      valeur_bateau = 0
                      # on relance tous les dés et on les trie
                      de_1 = lancer_de()
                      de_2 = lancer_de()
                      de_3 = lancer_de()
                      de_4 = lancer_de()
                      de_5 = lancer_de()
                      de_6 = lancer_de()
                      de_7 = lancer_de()
                      de_8 = lancer_de()
                      de_9 = 0
                      de_10 = 0

                      # on pioche une carte
                      carte_active = piocher_carte()

                      # # DEBUG
                      # de_1 = 6
                      # de_2 = 6
                      # de_3 = 1
                      # de_4 = 1
                      # de_5 = 1
                      # de_6 = 1
                      # de_7 = 1
                      # de_8 = 1
                      # de_9 = 0
                      # de_10 = 0
                      # carte_active = "2_tetes_de_mort"

                      # a t'on pioché un diamant ?
                      if carte_active == "diamant":
                        # on active le 9e dé sur la face 1 (diamant)
                        de_9 = 1
                      # a t'on pioché une pièce ?
                      if carte_active == "piece_or":
                        # on active le 9e dé sur la face 2 (pièce d'or)
                        de_9 = 2
                      # a t'on pioché une tête de mort ?
                      if carte_active == "tete_de_mort":
                        # on active le 9e dé sur la face 6 (tête de mort)
                        de_9 = 6
                      # a t'on pioché la carte avec deux têtes de mort ?
                      if carte_active == "2_tetes_de_mort":
                        # on active le 9e dé sur la face 6 (tête de mort)
                        de_9 = 6
                        # et on active le 10e dé sur la face 6 (tête de mort)
                        de_10 = 6
                      # a t'on pioché un pirate ?
                      if carte_active == "pirate":
                        # on double le score
                        multiplicateur = 2
                      else:
                        # on ne double pas
                        multiplicateur = 1
                      # a t'on pioché un perroquet / singe ?
                      if carte_active == "perroquet_singe":
                        # on stocke cette information
                        perroquet_singe = True
                      else:
                        # on mets la variable sur False pour qu'elle ne reste pas active indéfiniment
                        perroquet_singe = False
                      # a t'on pioché la gardienne ?
                      if carte_active == "gardienne":
                        # on stocke cette information
                        gardienne = True
                      else:
                        # on mets la variable sur False pour qu'elle ne reste pas active indéfiniment
                        gardienne = False
                      # a t'on pioché un coffre ?
                      if carte_active == "coffre":
                        # on stocke cette information
                        coffre = True
                      else:
                        # on mets la variable sur False pour qu'elle ne reste pas active indéfiniment
                        coffre = False

                      # Sur l'île de la tête de mort?
                      if des_face_6() >= 4:
                        ile_de_la_tete_de_mort = True
                      else:
                        ile_de_la_tete_de_mort = False

                      # a t'on pioché une carte bateau 2 ?
                      if carte_active == "bateau_2":
                        en_combat = True
                        blocage_suivant = True
                        sabres_necessaires = 2
                        valeur_bateau = 200
                        # on désactive l'île de la tête de mort
                        ile_de_la_tete_de_mort = False
                      # a t'on pioché une carte bateau 3 ?
                      if carte_active == "bateau_3":
                        en_combat = True
                        blocage_suivant = True
                        sabres_necessaires = 3
                        valeur_bateau = 500
                        # on désactive l'île de la tête de mort
                        ile_de_la_tete_de_mort = False
                      # a t'on pioché une carte bateau 4 ?
                      if carte_active == "bateau_4":
                        en_combat = True
                        blocage_suivant = True
                        sabres_necessaires = 4
                        valeur_bateau = 1000
                        # on désactive l'île de la tête de mort
                        ile_de_la_tete_de_mort = False

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

                      stockage = [
                          (de_1, couleur_de_1),
                          (de_2, couleur_de_2),
                          (de_3, couleur_de_3),
                          (de_4, couleur_de_4),
                          (de_5, couleur_de_5),
                          (de_6, couleur_de_6),
                          (de_7, couleur_de_7),
                          (de_8, couleur_de_8)
                      ]
                      stockage.sort()
                      (de_1, couleur_de_1), (de_2, couleur_de_2), (de_3, couleur_de_3), (de_4, couleur_de_4), (de_5, couleur_de_5), (de_6, couleur_de_6), (de_7, couleur_de_7), (de_8, couleur_de_8) = stockage

                      # est-on en combat?
                      if en_combat == True:
                          # le navire est-il vaincu ?
                          if des_face_5() >= sabres_necessaires:
                            # le navire est vaincu.
                            # on stoppe le combat
                            en_combat = False
                            # on débloque le bouton SUIVANT
                            blocage_suivant = False
                            # on bloque autant de dés 'sabre' que nécessaire
                            sabres_attribues = 0
                            # doit-on bloquer le de 8 ?
                            if de_8 == 5: # sabre
                                if sabres_attribues < sabres_necessaires:
                                  couleur_de_8 = black
                                  sabres_attribues = sabres_attribues + 1
                            # doit-on bloquer le de 7 ?
                            if de_7 == 5: # sabre
                                if sabres_attribues < sabres_necessaires:
                                  couleur_de_7 = black
                                  sabres_attribues = sabres_attribues + 1
                            # doit-on bloquer le de 6 ?
                            if de_6 == 5: # sabre
                                if sabres_attribues < sabres_necessaires:
                                  couleur_de_6 = black
                                  sabres_attribues = sabres_attribues + 1
                            # doit-on bloquer le de 5 ?
                            if de_5 == 5: # sabre
                                if sabres_attribues < sabres_necessaires:
                                  couleur_de_5 = black
                                  sabres_attribues = sabres_attribues + 1
                            # doit-on bloquer le de 4 ?
                            if de_4 == 5: # sabre
                                if sabres_attribues < sabres_necessaires:
                                  couleur_de_4 = black
                                  sabres_attribues = sabres_attribues + 1
                            # doit-on bloquer le de 3 ?
                            if de_3 == 5: # sabre
                                if sabres_attribues < sabres_necessaires:
                                  couleur_de_3 = black
                                  sabres_attribues = sabres_attribues + 1
                            # doit-on bloquer le de 2 ?
                            if de_2 == 5: # sabre
                                if sabres_attribues < sabres_necessaires:
                                  couleur_de_2 = black
                                  sabres_attribues = sabres_attribues + 1
                            # doit-on bloquer le de 1 ?
                            if de_1 == 5: # sabre
                                if sabres_attribues < sabres_necessaires:
                                  couleur_de_1 = black
                                  sabres_attribues = sabres_attribues + 1

                      # Le joueur est-il joué par l'ordinateur ?
                      if joueurs[joueur_actif] == "ORDI_1000":
                         # Au tour de ORDI_1000
                         # On bloque les clics sur les dés (l'ordi va les lancer lui-même)
                         blocage_des = True
                         # On bloque le bouton SUIVANT
                         blocage_suivant = True
                         # A t'on perdu ou a t'on zéro dé à relancer ? Si oui on débloque le bouton SUIVANT
                         if des_face_6() >= 3:
                           blocage_suivant = False
                         elif (couleur_de_1 != green and couleur_de_2 != green and couleur_de_3 != green and couleur_de_4 != green and couleur_de_5 != green and couleur_de_6 != green and couleur_de_7 != green and couleur_de_8 != green):
                            blocage_suivant = False
                         elif en_combat == True:
                            # on passe la couleur des sabres en rouge
                            # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                            if de_1 == 5:
                                if couleur_de_1 == green:
                                # on bloque le dé car on en a le droit
                                  couleur_de_1 = red
                            elif couleur_de_1 == red:
                                # ce n'est pas la bonne face, on débloque car on en a le droit
                                couleur_de_1 = green
                            if de_2 == 5:
                                if couleur_de_2 == green:
                                # on bloque le dé car on en a le droit
                                  couleur_de_2 = red
                            elif couleur_de_2 == red:
                                # ce n'est pas la bonne face, on débloque car on en a le droit
                                couleur_de_2 = green
                            if de_3 == 5:
                                if couleur_de_3 == green:
                                # on bloque le dé car on en a le droit
                                  couleur_de_3 = red
                            elif couleur_de_3 == red:
                                # ce n'est pas la bonne face, on débloque car on en a le droit
                                couleur_de_3 = green
                            if de_4 == 5:
                                if couleur_de_4 == green:
                                # on bloque le dé car on en a le droit
                                  couleur_de_4 = red
                            elif couleur_de_4 == red:
                                # ce n'est pas la bonne face, on débloque car on en a le droit
                                couleur_de_4 = green
                            if de_5 == 5:
                                if couleur_de_5 == green:
                                # on bloque le dé car on en a le droit
                                  couleur_de_5 = red
                            elif couleur_de_5 == red:
                                # ce n'est pas la bonne face, on débloque car on en a le droit
                                couleur_de_5 = green
                            if de_6 == 5:
                                if couleur_de_6 == green:
                                # on bloque le dé car on en a le droit
                                  couleur_de_6 = red
                            elif couleur_de_6 == red:
                                # ce n'est pas la bonne face, on débloque car on en a le droit
                                couleur_de_6 = green
                            if de_7 == 5:
                                if couleur_de_7 == green:
                                # on bloque le dé car on en a le droit
                                  couleur_de_7 = red
                            elif couleur_de_7 == red:
                                # ce n'est pas la bonne face, on débloque car on en a le droit
                                couleur_de_7 = green
                            if de_8 == 5:
                                if couleur_de_8 == green:
                                # on bloque le dé car on en a le droit
                                  couleur_de_8 = red
                            elif couleur_de_8 == red:
                                # ce n'est pas la bonne face, on débloque car on en a le droit
                                couleur_de_8 = green
                         else:
                            # la partie continue !
                            # Variables pour le calcul du score
                            mult_diamants = des_face_1()
                            mult_pieces = des_face_2()
                            mult_serie_3 = serie_de_3()
                            mult_serie_4 = serie_de_4()
                            mult_serie_5 = serie_de_5()
                            mult_serie_6 = serie_de_6()
                            mult_serie_7 = serie_de_7()
                            mult_serie_8 = serie_de_8()
                            if des_face_6() == 0:
                                mult_tresor = 1
                            else:
                                mult_tresor = 0
                            total = (100 * mult_diamants) + (100 * mult_pieces) + (100 * mult_serie_3) + (200 * mult_serie_4) + (500 * mult_serie_5) + (1000 * mult_serie_6) + (2000 * mult_serie_7) + (4000 * mult_serie_8) + (500 * mult_tresor) + valeur_bateau
                            if mult_diamants == 9:
                              # Neuf diamants ! La partie est gagnée
                              total = 99999
                            if mult_pieces == 9:
                              # Neuf pièces ! La partie est gagnée
                              total = 99999
                            total = total * multiplicateur
                            # a t'on obtenu 1000 points?
                            if total >= 1000:
                              # on bloque le bouton RELANCER pour conserver notre score
                              blocage_relancer = True
                              # on débloque le bouton SUIVANT pour valider notre score
                              blocage_suivant = False
                            else:
                               # on n'a pas encore 1000 points et on n'a pas encore perdu.
                               # si on a déjà 3 diamants ou plus, on les conserve
                               if des_face_1() >= 3:
                                  # on passe la couleur des diamants en rouge
                                  # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                  if de_1 == 1:
                                     if couleur_de_1 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_1 = red
                                  elif couleur_de_1 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_1 = green
                                  if de_2 == 1:
                                     if couleur_de_2 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_2 = red
                                  elif couleur_de_2 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_2 = green
                                  if de_3 == 1:
                                     if couleur_de_3 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_3 = red
                                  elif couleur_de_3 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_3 = green
                                  if de_4 == 1:
                                     if couleur_de_4 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_4 = red
                                  elif couleur_de_4 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_4 = green
                                  if de_5 == 1:
                                     if couleur_de_5 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_5 = red
                                  elif couleur_de_5 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_5 = green
                                  if de_6 == 1:
                                     if couleur_de_6 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_6 = red
                                  elif couleur_de_6 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_6 = green
                                  if de_7 == 1:
                                     if couleur_de_7 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_7 = red
                                  elif couleur_de_7 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_7 = green
                                  if de_8 == 1:
                                     if couleur_de_8 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_8 = red
                                  elif couleur_de_8 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_8 = green

                               # sinon, si on a déjà 3 pièces d'or ou plus, on les conserve
                               elif des_face_2() >= 3:
                                  # on passe la couleur des pièces d'or en rouge
                                  # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                  if de_1 == 2:
                                     if couleur_de_1 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_1 = red
                                  elif couleur_de_1 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_1 = green
                                  if de_2 == 2:
                                     if couleur_de_2 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_2 = red
                                  elif couleur_de_2 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_2 = green
                                  if de_3 == 2:
                                     if couleur_de_3 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_3 = red
                                  elif couleur_de_3 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_3 = green
                                  if de_4 == 2:
                                     if couleur_de_4 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_4 = red
                                  elif couleur_de_4 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_4 = green
                                  if de_5 == 2:
                                     if couleur_de_5 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_5 = red
                                  elif couleur_de_5 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_5 = green
                                  if de_6 == 2:
                                     if couleur_de_6 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_6 = red
                                  elif couleur_de_6 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_6 = green
                                  if de_7 == 2:
                                     if couleur_de_7 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_7 = red
                                  elif couleur_de_7 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_7 = green
                                  if de_8 == 2:
                                     if couleur_de_8 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_8 = red
                                  elif couleur_de_8 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_8 = green
 
                               # sinon, si on a déjà 3 singes ou plus, on les conserve
                               elif des_face_3() >= 3:
                                  # on passe la couleur des singes en rouge
                                  # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                  if de_1 == 3:
                                     if couleur_de_1 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_1 = red
                                  elif couleur_de_1 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_1 = green
                                  if de_2 == 3:
                                     if couleur_de_2 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_2 = red
                                  elif couleur_de_2 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_2 = green
                                  if de_3 == 3:
                                     if couleur_de_3 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_3 = red
                                  elif couleur_de_3 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_3 = green
                                  if de_4 == 3:
                                     if couleur_de_4 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_4 = red
                                  elif couleur_de_4 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_4 = green
                                  if de_5 == 3:
                                     if couleur_de_5 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_5 = red
                                  elif couleur_de_5 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_5 = green
                                  if de_6 == 3:
                                     if couleur_de_6 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_6 = red
                                  elif couleur_de_6 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_6 = green
                                  if de_7 == 3:
                                     if couleur_de_7 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_7 = red
                                  elif couleur_de_7 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_7 = green
                                  if de_8 == 3:
                                     if couleur_de_8 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_8 = red
                                  elif couleur_de_8 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_8 = green
 
                               # sinon, si on a déjà 3 perroquets ou plus, on les conserve
                               elif des_face_4() >= 3:
                                  # on passe la couleur des perroquets en rouge
                                  # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                  if de_1 == 4:
                                     if couleur_de_1 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_1 = red
                                  elif couleur_de_1 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_1 = green
                                  if de_2 == 4:
                                     if couleur_de_2 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_2 = red
                                  elif couleur_de_2 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_2 = green
                                  if de_3 == 4:
                                     if couleur_de_3 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_3 = red
                                  elif couleur_de_3 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_3 = green
                                  if de_4 == 4:
                                     if couleur_de_4 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_4 = red
                                  elif couleur_de_4 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_4 = green
                                  if de_5 == 4:
                                     if couleur_de_5 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_5 = red
                                  elif couleur_de_5 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_5 = green
                                  if de_6 == 4:
                                     if couleur_de_6 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_6 = red
                                  elif couleur_de_6 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_6 = green
                                  if de_7 == 4:
                                     if couleur_de_7 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_7 = red
                                  elif couleur_de_7 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_7 = green
                                  if de_8 == 4:
                                     if couleur_de_8 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_8 = red
                                  elif couleur_de_8 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_8 = green
 
                               # sinon, si on a déjà 3 sabres ou plus, on les conserve
                               elif des_face_5() >= 3:
                                  # on passe la couleur des sabres en rouge
                                  # et la couleur des autres dés en vert (sauf ceux qui sont déjà noirs)
                                  if de_1 == 5:
                                     if couleur_de_1 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_1 = red
                                  elif couleur_de_1 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_1 = green
                                  if de_2 == 5:
                                     if couleur_de_2 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_2 = red
                                  elif couleur_de_2 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_2 = green
                                  if de_3 == 5:
                                     if couleur_de_3 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_3 = red
                                  elif couleur_de_3 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_3 = green
                                  if de_4 == 5:
                                     if couleur_de_4 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_4 = red
                                  elif couleur_de_4 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_4 = green
                                  if de_5 == 5:
                                     if couleur_de_5 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_5 = red
                                  elif couleur_de_5 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_5 = green
                                  if de_6 == 5:
                                     if couleur_de_6 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_6 = red
                                  elif couleur_de_6 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_6 = green
                                  if de_7 == 5:
                                     if couleur_de_7 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_7 = red
                                  elif couleur_de_7 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
                                     couleur_de_7 = green
                                  if de_8 == 5:
                                     if couleur_de_8 == green:
                                      # on bloque le dé car on en a le droit
                                      couleur_de_8 = red
                                  elif couleur_de_8 == red:
                                     # ce n'est pas la bonne face, on débloque car on en a le droit
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
        if gardienne == True:
           # Le dé numéro 8 est-il une tête de mort ?
           if couleur_de_8 == black:
              # Oui - on passe le fond en vert pour qu'il puisse être relancé
              couleur_de_8 = green
              # On a utilisé le pouvoir de la gardienne
              gardienne = False
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

        # Afficher le prénom du joueur dont c'est le tour:
        font = pygame.font.Font(None, 24)
        text_surf = font.render(f"Tour de: {joueurs[joueur_actif]} - Score: {scores[joueur_actif]}", True, text_color)
        text_rect = pygame.Rect(500, 20, 100, 50)
        screen.blit(text_surf, text_rect)

        # Afficher le bouton SUIVANT:
        pygame.draw.rect(screen, button_color, bouton_suivant)
        font = pygame.font.Font(None, 36)
        text_surf = font.render("SUIVANT", True, text_color)
        text_rect = text_surf.get_rect(center=bouton_suivant.center)
        screen.blit(text_surf, text_rect)

        # Si on est sur l'île de la tête de mort, on l'affiche à l'écran
        if ile_de_la_tete_de_mort == True:
          screen.blit(pygame.transform.scale(pygame.image.load('ile.png'), (150, 250)), (40, 200))

        # on affiche la carte à l'écran
        screen.blit(pygame.transform.scale(cartes[carte_active], (150, 250)), (200, 200))

        if coffre == True:
          # On sauvegarde tous les dés
            sauv_de_1 = de_1
            sauv_de_2 = de_2
            sauv_de_3 = de_3
            sauv_de_4 = de_4
            sauv_de_5 = de_5
            sauv_de_6 = de_6
            sauv_de_7 = de_7
            sauv_de_8 = de_8

        if des_face_6() >= 3:
            if ile_de_la_tete_de_mort == False:
              # Le joueur a perdu, est-ce qu'il a la carte coffre?
              if coffre == True:
                 # On garde les dés rouges et on mets à 0 les autres
                 if couleur_de_1 != red:
                    de_1 = 0
                 if couleur_de_2 != red:
                    de_2 = 0
                 if couleur_de_3 != red:
                    de_3 = 0
                 if couleur_de_4 != red:
                    de_4 = 0
                 if couleur_de_5 != red:
                    de_5 = 0
                 if couleur_de_6 != red:
                    de_6 = 0
                 if couleur_de_7 != red:
                    de_7 = 0
                 if couleur_de_8 != red:
                    de_8 = 0

        # Variables pour le calcul du score
        mult_diamants = des_face_1()
        mult_pieces = des_face_2()
        mult_serie_3 = serie_de_3()
        mult_serie_4 = serie_de_4()
        mult_serie_5 = serie_de_5()
        mult_serie_6 = serie_de_6()
        mult_serie_7 = serie_de_7()
        mult_serie_8 = serie_de_8()
        if des_face_6() == 0:
            mult_tresor = 1
        else:
            mult_tresor = 0
        total = (100 * mult_diamants) + (100 * mult_pieces) + (100 * mult_serie_3) + (200 * mult_serie_4) + (500 * mult_serie_5) + (1000 * mult_serie_6) + (2000 * mult_serie_7) + (4000 * mult_serie_8) + (500 * mult_tresor) + valeur_bateau
        if mult_diamants == 9:
           # Neuf diamants ! La partie est gagnée
           total = 99999
        if mult_pieces == 9:
           # Neuf pièces ! La partie est gagnée
           total = 99999
        total = total * multiplicateur
        
        if coffre == True:
          # On récupère les valeurs des dés
          de_1 = sauv_de_1
          de_2 = sauv_de_2
          de_3 = sauv_de_3
          de_4 = sauv_de_4
          de_5 = sauv_de_5
          de_6 = sauv_de_6
          de_7 = sauv_de_7
          de_8 = sauv_de_8

        # Afficher la zone de texte pour les scores
        font = pygame.font.Font(None, 30)
        # Le texte que l'on va afficher, et où les variables seront mises à jour
        scores_text = [
            f"Diamants: x{mult_diamants} = {100 * mult_diamants * multiplicateur}",
            f"Pièces d'or: x{mult_pieces} = {100 * mult_pieces * multiplicateur}",
            f"3 dés: x{mult_serie_3} = {100 * mult_serie_3 * multiplicateur}",
            f"4 dés: x{mult_serie_4} = {200 * mult_serie_4 * multiplicateur}",
            f"5 dés: x{mult_serie_5} = {500 * mult_serie_5 * multiplicateur}",
            f"6 dés: x{mult_serie_6} = {1000 * mult_serie_6 * multiplicateur}",
            f"7 dés: x{mult_serie_7} = {2000 * mult_serie_7 * multiplicateur}",
            f"8 dés: x{mult_serie_8} = {4000 * mult_serie_8 * multiplicateur}",
            f"Trésor: x{mult_tresor} = {500 * mult_tresor * multiplicateur}",
            f"TOTAL: {total} points"
        ]

        if valeur_bateau != 0:
          scores_text = [
            f"Diamants: x{mult_diamants} = {100 * mult_diamants * multiplicateur}",
            f"Pièces d'or: x{mult_pieces} = {100 * mult_pieces * multiplicateur}",
            f"3 dés: x{mult_serie_3} = {100 * mult_serie_3 * multiplicateur}",
            f"4 dés: x{mult_serie_4} = {200 * mult_serie_4 * multiplicateur}",
            f"5 dés: x{mult_serie_5} = {500 * mult_serie_5 * multiplicateur}",
            f"6 dés: x{mult_serie_6} = {1000 * mult_serie_6 * multiplicateur}",
            f"7 dés: x{mult_serie_7} = {2000 * mult_serie_7 * multiplicateur}",
            f"8 dés: x{mult_serie_8} = {4000 * mult_serie_8 * multiplicateur}",
            f"Trésor: x{mult_tresor} = {500 * mult_tresor * multiplicateur}",
            f"Combat: {valeur_bateau}",
            f"TOTAL: {total} points"
        ]

        if en_combat == True:
           # on affiche une info sur le score à battre
          scores_text = [
              "LE COMBAT FAIT RAGE !",
              f"Sabres nécessaires: {sabres_necessaires}",
              f"Vos sabres: {des_face_5()}"
          ]

        if des_face_6() >= 3:
            if ile_de_la_tete_de_mort == False:
              blocage_suivant = False
              # a t'on la carte coffre ?
              if coffre == False:
                # pas de chance
                # avons nous de plus perdu contre un bateau ?
                if valeur_bateau == 0:
                  # c'est juste une défaite classique
                  total = 0
                  scores_text = [
                      f"OH NON, C'EST PERDU !",
                      f"TOTAL: {total} points"
                  ]
                else:
                  # on a en plus perdu contre un bateau !!
                  total = -1 * valeur_bateau
                  scores_text = [
                      f"LE NAVIRE VOUS A COULÉ !!",
                      f"TOTAL: {total} points"
                  ]
              else:
                # on garde les points des dés rouges
                # on retire le bonus de 500 points
                total = total - 500
                # on bloque les clics sur les dés et le bouton RELANCER
                blocage_des = True
                blocage_relancer = True
                scores_text = [
                    f"OH NON, C'EST PERDU !",
                    f"Diamants: x{mult_diamants} = {100 * mult_diamants * multiplicateur}",
                    f"Pièces d'or: x{mult_pieces} = {100 * mult_pieces * multiplicateur}",
                    f"3 dés: x{mult_serie_3} = {100 * mult_serie_3 * multiplicateur}",
                    f"4 dés: x{mult_serie_4} = {200 * mult_serie_4 * multiplicateur}",
                    f"5 dés: x{mult_serie_5} = {500 * mult_serie_5 * multiplicateur}",
                    # Comme on a au moins 3 têtes de mort, il est impossible
                    # d'avoir plus de 5 dés identiques et d'avoir le bonus des
                    # 8 dés sans tête de mort, donc on n'affiche rien de plus ici
                    f"TOTAL DU COFFRE: {total} points"
                ]
            else:
              scores_text = [
                  f"SuR L'iLe De La TêTe De MoRT...",
                  f"MALUS ADVERSAIRE: {des_face_6() * 100 * multiplicateur} points"
              ]

        # boucle qui prend chaque ligne de texte et qui l'affiche
        for i, line in enumerate(scores_text):
            text_surf = font.render(line, True, text_color)
            screen.blit(text_surf, (400, 270 + i * 30))
    else:
        # On n'a pas de joueur, on affiche l'écran d'accueil
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Le joueur a cliqué sur la première zone de texte ?
                if rect_joueur1.collidepoint(event.pos):
                    # Oui: on stocke cette information
                    dans_rect_joueur_1 = True
                else:
                    # Non il a cliqué ailleurs: on stocke cette information
                    dans_rect_joueur_1 = False

                # Le joueur a cliqué sur la deuxième zone de texte ?
                if rect_joueur2.collidepoint(event.pos):
                    # Oui: on stocke cette information
                    dans_rect_joueur_2 = True
                else:
                    # Non il a cliqué ailleurs: on stocke cette information
                    dans_rect_joueur_2 = False

                # Le joueur a t'il cliqué sur le bouton 'OK' ?
                if bouton_ok.collidepoint(event.pos):
                    # Oui: on stocke les prénoms dans la variable 'joueurs' (sauf s'il manque des prénoms')
                    if prenom1 != "" and prenom2 != "":
                        joueurs = [prenom1, prenom2]
                        scores = [0, 0]
                    # Comme notre variable 'joueurs' n'est plus vide, le jeu va passer à l'écran principal
            elif event.type == pygame.KEYDOWN:
                # Le joueur essaie t'il d'écrire au clavier dans la première zone de texte ?
                if dans_rect_joueur_1:
                    if event.key == pygame.K_BACKSPACE:
                        # Si on appuie sur 'backspace', on efface une lettre
                        prenom1 = prenom1[:-1]
                    else:
                        # Sinon on ajoute la lettre tapée
                        prenom1 += event.unicode
                # Le joueur essaie t'il d'écrire au clavier dans la deuxième zone de texte ?
                elif dans_rect_joueur_2:
                    if event.key == pygame.K_BACKSPACE:
                        # Si on appuie sur 'backspace', on efface une lettre
                        prenom2 = prenom2[:-1]
                    else:
                        # Sinon on ajoute la lettre tapée
                        prenom2 += event.unicode

        # On affiche un fond d'écran blanc
        screen.fill(white)

        # on choisit une police de taille 36 pour écrire en grosses lettres
        font = pygame.font.Font(None, 36)
        # on crée une variable text_surf qui contiendra le texte "Entrez vos prénoms !"
        text_surf = font.render("Entrez vos prénoms !", True, text_color)
        # on définit une zone où afficher ce texte
        text_rect = pygame.Rect(250, 50, 100, 40)
        # enfin, on affiche le texte dans ce rectangle
        screen.blit(text_surf, text_rect)

        # on affiche une zone verte pour le premier prénom
        pygame.draw.rect(screen, green, rect_joueur1)
        # on crée une variable text_surf qui contiendra les lettres entrées au clavier
        text_surf = font.render(prenom1, True, text_color)
        text_rect = text_surf.get_rect(center=rect_joueur1.center)
        # enfin, on affiche le texte dans la zone correspondante
        screen.blit(text_surf, text_rect)

        # on affiche une zone verte pour le deuxième prénom
        pygame.draw.rect(screen, green, rect_joueur2)
        # on crée une variable text_surf qui contiendra les lettres entrées au clavier
        text_surf = font.render(prenom2, True, text_color)
        text_rect = text_surf.get_rect(center=rect_joueur2.center)
        # enfin, on affiche le texte dans la zone correspondante
        screen.blit(text_surf, text_rect)

        # Afficher le bouton OK:
        # on affiche un rectangle rouge de la taille de notre bouton
        pygame.draw.rect(screen, red, bouton_ok)
        # on choisit une police de taille 36 pour écrire en grosses lettres
        font = pygame.font.Font(None, 36)
        # on crée une variable text_surf qui contiendra le texte OK
        text_surf = font.render("OK", True, text_color)
        # on définit un que notre texte doit être centré sur notre bouton
        text_rect = text_surf.get_rect(center=bouton_ok.center)
        # enfin, on affiche le résultat
        screen.blit(text_surf, text_rect)

    # On rafraichit l'écran (on affiche le nouvel écran à la place de l'ancien)
    pygame.display.flip()

# Si on arrive ici c'est qu'on a quitté le jeu (on est donc sorti de la boucle infinie)
# On ferme le programme proprement
pygame.quit()
