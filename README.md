# 1000 Sabords !!

Nous allons programmer le jeu '1000 Sabords' en python. Vous trouverez une liste de missions ci-dessous, votre but est de remplir 1 mission par jour. Si vous vous sentez d'attaque vous pouvez en faire plus, mais déjà si vous en faites une par jour ca sera déjà très bien !

## Avant de commencer à programmer
Il vous faut de quoi programmer et exécuter le jeu. Pour ce faire, commencez par les étapes suivantes:

### Installer python
Pour tester si vous avez déjà python sur votre machine:

1. ouvrez un terminal de commande: Dans le menu `Démarrer`, tapez `cmd` (pour 'commande'). Cliquez sur `ouvrir` sur le premier résultat
2. dans le terminal (la fenêtre noire), tapez `python --version`.
  * Si ca affiche un message du genre `Python 3.9.0`, c'est bon, python est déjà installé
  * Sinon:
    * Sur Internet, allez sur https://www.python.org/downloads/
    * Cliquez sur `Download Python 3.12.3`
    * Une fois que c'est fait, sur votre PC allez dans le répertoire `Téléchargements` et double-cliquez sur le ficher téléchargé
      * Suivez les instructions à l'écran

### Installer pip
Pip est un programme de téléchargement dédié aux libraires python. Nous allons en avoir besoin pour installer la librairie `pygame` qui contient du code utile pour la création de jeux vidéo.

Pour tester si vous avez déjà pip sur votre machine:

1. si ce n'est déjà fait, ouvrez un terminal de commande (comme expliqué au-dessus)
2. dans le terminal, tapez `pip --version`.
  * Si ca affiche un message du genre `pip 20.2.3`, c'est bon, pip est déjà installé
  * Sinon: installez pip en tapant la commande `python pip install`

### Installer pygame
Pygame est une librairie python qui facilite le développement de jeux.

Pour installer pygame, faites ceci:

1. si ce n'est déjà fait, ouvrez un terminal de commande (comme expliqué plus haut)
2. dans le terminal, tapez `pip install pygame`

### Installer VSCode
On a tout ce qu'il faut pour faire fonctionner le jeu, mais maintenant il faut l'écrire. VSCode est un logiciel dédié à l'écriture de programmes (je l'utilise moi-même régulièrement pour le travail).

Pour installer VSCode, faites ceci:

1. Sur Internet, allez sur https://code.visualstudio.com/download
2. Cliquez sur le bouton `Windows`
3. Sur votre PC allez dans le répertoire `Téléchargements` et double-cliquez sur le fichier téléchargé
  * Suivez les instructions à l'écran

### Maintenant on peut commencer :)
* Lancez VSCode depuis le menu `Démarrer`
* Dans la partie gauche de l'écran (`Explorer`), faites un click droit puis choisissez `nouveau fichier...`
* Appelez-le `jeu.py`. Il va s'ouvrir dans la partie de droite de l'écran. Un fichier vide mais qui ne va pas rester vide.
* Pour vérifier que tout fonctionne, écrivez (ou copiez-collez) ce code dans `jeu.py`:

```
# Chargement de la librairie 'pygame'
import pygame

# Couleur de fond d'écran
white = (255, 255, 255)

# Initialization de pygame
pygame.init()

# On crée une fenêtre de 800 pixels de long et de 600 pixels de haut qui contiendra notre jeu
win_size = (800, 600)
screen = pygame.display.set_mode(win_size)
# Un nom sympa qui s'affichera en haut de la fenêtre
pygame.display.set_caption("1000 Sabords !!!")

# Si on ne fait rien de spécial le programme va se terminer immédiatement.
# On crée donc une boucle infinie qui s'arrêtera quand on ferme la fenêtre avec la croix
running = True
while running:
    for event in pygame.event.get():
        # Faire une action (cliquer, appuyer sur une touche) s'appelle un 'event' (événement)
        # On regarde à chaque tour de boucle si on a cliqué sur la croix (événement 'QUIT')
        if event.type == pygame.QUIT:
            running = False

    # On dessine sur l'écran (pour le moment juste un fond blanc)
    screen.fill(white)

    # On rafraichit l'écran (on affiche le nouvel écran à la place de l'ancien)
    pygame.display.flip()

# Si on arrive ici c'est qu'on a quitté le jeu (on est donc sorti de la boucle infinie)
# On ferme le programme proprement
pygame.quit()
```
* Pour tester que ca fonctionne, démarrez le programme. Dans VSCode, en haut de la fenêtre de jeu.py, il y a un petit triangle (comme un bouton 'play'). Appuyez dessus.
* Si tout va bien, une fenêtre blanche va s'afficher. Cliquez sur la croix pour la fermer.

Félicitations, vous êtes maintenant prêt à programmer le jeu de 1000 Sabords !

## 1ère mission: jeter un dé
Pour commencer nous allons afficher un dé, et un bouton 'RELANCER' qui permet de relancer le dé. Pour ce dé nous avons besoin de six images qui représentent ses faces:
* Un diamant
* Une pièce d'or
* Un singe
* Un perroquet
* Un sabre
* Une tête de mort

Sur Internet, cherchez une image adéquate pour chacune de ces six faces. Téléchargez-les et mettez-les dans le même répertoire que là où se trouve votre fichier `jeu.py`. Les images devraient apparaitre dans VSCode dans la colonne de gauche. Renommez ces images en fonction de ce qu'elles représentent.

### Le premier dé

Il est temps de commencer à programmer. Notre dé aura une dimension de 50x50 pixels et sera affiché vers la gauche de l'écran. La face affichée sera choisie aléatoirement.

Dans la logique de la programmation, on commence par choisir une valeur au hasard entre 1 et 6, on choisit l'image correspondante au numéro, et on l'affiche. Inspirez-vous des morceaux de code suivants, à vous de voir où les positionner pour que tout fonctionne. Il y aura quelques ajustements à faire en fonction du nom de vos images...

```
# librairie qui sert à choisir des nombres aléatoires
import random
```

```
# dictionnaire qui associe une 'clé' (nombre de 1 à 6) à une 'valeur' (nom de l'image)
images = {
    1: pygame.image.load('diamant.png'),
    2: pygame.image.load('piece_or.png'),
    3: pygame.image.load('singe.png'),
    4: pygame.image.load('perroquet.png'),
    5: pygame.image.load('sabre.png'),
    6: pygame.image.load('tete_de_mort.png')
}
```

```
# Fonction pour lancer le dé
def lancer_de():
    return random.randint(1, 6)
```

```
# Initialisation de la face du dé (on le lance une fois)
de_1 = lancer_de()
```

```
# Afficher le dé (attention cette partie doit être dans la boucle infinie)
# Explications:
#   image[de_1] : récupère l'image dans le dictionnaire correspondant au numéro aléatoire
#   pygame.transform.scale(..., (50, 50)) : redimensionne l'image à la taille de 50x50 pixels
#   screen.blit(..., (30, 60)) : positionne l'image à 30 pixels du bord gauche et à 60 pixels du haut de l'écran
screen.blit(pygame.transform.scale(images[de_1], (50, 50)), (30, 60))
```

Testez votre code en appuyant sur le bouton 'play'. À chaque fois que vous démarrez votre jeu vous verrez que le dé affiche une des 6 images possibles.

### Le bouton RELANCER
Il reste à ajouter un bouton RELANCER. Le code suivant sera utile, à vous de le placer au bon endroit...

```
# Couleurs pour notre bouton RELANCER
button_color = (100, 100, 100)
text_color = (0, 0, 0)
```

```
# Définir les dimensions et la position du bouton, nécessaire pour savoir quand on clique dessus
# Explications:
#  200: position du bouton par rapport au bord gauche
#  50: position du bouton par rapport au haut de la fenêtre
#  150: longueur du bouton
#  50: hauteur du bouton
bouton_relancer = pygame.Rect(200, 50, 150, 50)
```

```
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
```

```
# On teste si un bouton est cliqué (événement 'MOUSEBUTTONDOWN')
# (le mot-clé 'elif' est la même chose que 'else if', ca doit vous aider à comprendre où placer ce code)
elif event.type == pygame.MOUSEBUTTONDOWN:
    # à cet endroit dans le code, on sait que la souris a été cliquée. On teste pour savoir si on a cliqué sur le bouton RELANCER
    if bouton_relancer.collidepoint(event.pos):
        # à cet endroit dans le code, on sait qu'on a cliqué sur le bouton RELANCER. Reste à assigner une nouvelle face à notre dé
        de_1 = lancer_de()  # Relancer le dé
```

N'hésitez pas à tester au fur et à mesure. Si tout va bien, vous devriez maintenant avoir un jeu où on peut relancer le dé à chaque fois qu'on appuie sur le bouton. Bon, y'a encore du boulot pour avoir un jeu complet, mais c'est déjà une très bonne base ! Félicitations et à demain pour le deuxième module.


## 2ème mission: afficher 8 dés, bloquer des dés
Un dé c'est bien, mais il nous en faut huit !
Nous allons donc faire les choses suivantes:
* afficher 8 dés au lieu d'un seul
* leur ajouter un bord qui pourra changer de couleur
  * bord vert: le dé peut être relancé
  * bord rouge: le dé est bloqué (on ne veut pas le relancer)
  * bord noir: le dé est bloqué pour toujours (pour les têtes de mort)
* on pourra bloquer / débloquer des dés en cliquant dessus
* on pourra relancer les dés à bord vert

### Les 7 autres dés

Commencez par ajouter 7 dés supplémentaires. Pour ce faire, donnez un nom à chacun des dés. Le dé actuel est associé à la variable `de_1`.
* en regardant comment `de_1` a été initialisé, ajoutez l'initialisation des variables `de_2`, `de_3` etc jusqu'à `de_8`
* affichez les dés supplémentaires à droite du premier dé. Espacez les dés de 52 pixels à chaque fois (en prévision de l'ajout du bord de couleur)
* le bouton RELANCER apparaitra sur les dés, déplacez le bouton sur la droite pour que ca ne chevauche plus (le placer à 450 pixels du bord gauche devrait être amplement suffisant).
* enfin, ajoutez le code nécessaire pour que, lorsque l'on clique sur le bouton RELANCER, tous les dés soient relancés et pas uniquement `de_1`.

### Le bord de couleur

Nous allons maintenant ajouter un bord de couleur (vert, rouge, noir) aux dés. Pour ce faire, nous allons dessiner un carré de 52x52 pixels derrière le dé de 50x50 pixels. Si les deux carrés sont bien centrés, il devrait rester un bord de 1 pixel tout autour de notre dé.

Utilisez le code suivant pour définir les couleurs:

```
# couleurs des bords des dés
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
```

Chaque dé va avoir une variable qui contient sa couleur. Voici le code pour initialiser la couleur `de_1`, mettez ce code au bon endroit et initialisez les autres dés sur cette même couleur

```
# Initialiser la couleur du bord
couleur_de_1 = green
```

Affichez les carrés de couleur avant d'afficher les dés (si vous affichez les carrés après, il apparaitront par-dessus les dés au lieu d'en dessous). Voici le code pour le premier dé, à compléter:

```
# Dessiner le carré vert derrière le dé_1
# Explications:
#   29: à 29 pixels du bord (car le dé 1 est à 30 pixels)
#   59: à 59 pixels du haut (car le dé 1 est à 60 pixels)
#   52: longueur du carré (50 + 2 pour dépasser de 1 pixel de chaque côté)
#   52: hauteur du carré (50 + 2 pour dépasser de 1 pixel en haut et en bas)
pygame.draw.rect(screen, couleur_de_1, pygame.Rect(29, 59, 52, 52))
```

### Bloquer / debloquer un dé
Dans la partie initialisation, ajoutez le code qui définit où se trouvent les dés. Ce sont les même coordonnées que vous avez utilisé dans les lignes `pygame.draw.rect(screen, couleur_de_1, pygame.Rect(29, 59, 52, 52))`

Voici le code pour le dé 1, à compléter pour les autres:

```
# Définir les rectangles pour chaque dé pour détecter les clics
rect_de_1 = pygame.Rect(29, 59, 52, 52)
```

Maintenant que nous avons les variables `rect_de_1` etc, nous pouvons les utiliser pour tester si on a cliqué sur un dé. Le code suivant teste si on a cliqué sur le dé 1, ce code inverse la couleur de vert à rouge et inversemenent. À placer au bon endroit et à compléter pour les autres dés.

```
elif rect_de_1.collidepoint(event.pos):
    # on a cliqué sur le dé numéro 1
    if couleur_de_1 == green:
        couleur_de_1 = red
    elif couleur_de_1 == red:
        couleur_de_1 = green
```

Note: avez vous vu qu'on ne teste pas pour la couleur noir ? C'est parce que cette couleur va être dédiée aux têtes de mort. Un dé à bord noir ne changera donc pas de couleur en cliquant dessus.

### Relancer les dés verts uniquement
Modifiez la ligne de code suivante: `de_1 = lancer_de()  # Relancer le dé` de manière à le relancer uniquement si son fond est vert.

Une fois que c'est fait, faites pareil pour les autres dés.

### Mettre les têtes de mort sur fond noir
Il reste une dernière chose à faire: dès qu'un dé affiche une tête de mort, on change la couleur sur noir de manière à ce qu'on ne puisse plus le relancer.

Dans le dictionnaire, nous avons associé la tête de mort au numéro 6. Il suffit alors, après un lancer de dé, de regarder si ce dé est sur le 6. Si oui, on change sa couleur pour le noir. Ajoutez ce code juste après avoir lancé le dé 1:

```
if de_1 == 6:
    couleur_de_1 = black
```
Faites la même chose pour les autres dés.

Testez votre code si ce n'est déjà fait (on ne fait jamais trop de tests !). Si vous ne bloquez aucun dé et que vous relancez plusieurs fois, vous finirez par avoir 8 têtes de mort.

Si c'est le cas, félicitations, vous avez rempli votre deuxième mission avec succès !

## 3ème mission: fin de tour, afficher / masquer le score potentiel
## 4ème mission: stopper son tour, score global, fin à 6000 points
## 5ème mission: jouer à plusieurs
## 6ème mission: l'île de la tête de mort
## 7ème mission: on affiche les cartes
## 8ème mission: on code les règles spéciales
## 9ème mission: jouer contre... l'ordinateur

## Félicitations !!!
Vous avez codé le jeu de 1000 Sabords en python en juste quelques jours, c'est du bon boulot ! Vous pouvez l'améliorer en ajoutant de nouvelles cartes de votre invention, en rendant le jeu plus joli... ou tout simplement en y jouant avec vos amis !
