# Pijersi : les règles du jeu


![](./pictures/pijersi-2022-0723-0940.jpg)

Type de jeu : traverser pour gagner + empilement + capture

![](./pictures/schema.png)

<div style="page-break-after: always;"></div>

## Introduction

Dans le jeu “pijersi”, deux joueurs, blanc et noir, déplacent leurs cubes, seuls ou en piles dynamiques, qui s’affrontent dans leurs rôles de "pierre", "feuille", "ciseaux" et "sage". Chaque joueur s’efforce d’atteindre le premier la dernière ligne adverse. 

Le jeu "[pijersi](https://github.com/LucasBorboleta/pijersi)” est une variante du jeu “[jersi](https://github.com/LucasBorboleta/jersi)”. En [lojban](https://mw.lojban.org), la racine “prije” et son affixe “pi” signifient “sage”, tandis que la racine “jersi” signifie “chasser” ou “poursuivre”. Prononcer `/pi/jer/ssi/`.

## Informations générales
Nombre de joueurs : 2 / Age minimum : 8 ans / Durée de partie : 15 minutes 

## Matériel
Vous (joueur blanc/noir) avez 14 cubes à votre couleur (sur la photo: noir => rouge). Les 6 mêmes faces d'un cube définissent son rôle (exemple : pierre). Vous avez :

- 4 "pierre", 4 "feuille" et 4 "ciseaux" (respectivement, les symboles "cercle/carré/croix").
- 2 "sage" (le symbole "infini").

Le plateau hexagonal suivant, de 45 cases et de 7 lignes, est disposé entre les 2 joueurs :

<img src="./pictures/pijersi-positions-initiales.png" style="zoom:50%;" />

## Mise en place
Sur les 2 lignes les plus proches de vous (“ab” pour blanc et “fg” pour noir), vous placez vos cubes comme indiqué ci-dessus. Vos cubes "sage" sont empilés. Vous remplissez votre ligne arrière de gauche à droite, avec deux séquences pierre-feuille-ciseaux. Puis, vous complétez vos deux lignes en construisant des triangles pierre-feuille-ciseaux.

Le joueur blanc entame la partie. 

<div style="page-break-after: always;"></div>

## But du jeu

Vous devez amener le premier au moins un de vos cubes “pierre/feuille/ciseaux” sur la dernière ligne adverse (blanc vise la ligne “g” et noir vise la ligne “a”) ou bien vous devez empêcher votre adversaire de jouer à son tour. La partie est nulle après 20 tours sans aucune capture, depuis l'entame ou la dernière capture.

## Règles de pile
Les déplacements de cubes (qui sont expliqués après) permettent de construire des piles qui doivent respecter les règles qui suivent.

Une pile est limitée à 2 cubes quelconques de même couleur, sauf qu'un cube “sage” s’empile seulement sur un cube “sage”. 

## Règles de déplacement
Un cube, seul ou au sommet d’une pile, se déplace d’une seule case, soit vers une case vide, soit vers une case occupée pour s’empiler sur un autre cube (en respectant les règles de pile) ou pour capturer un cube ou une pile adverse (en respectant les règles de capture qui sont expliquées après).

Une pile se déplace de 1 ou 2 cases, sans bifurquer, ni sauter par-dessus des cases occupées, soit vers une case vide, soit vers une case occupée pour capturer un cube ou une pile adverse (en respectant les règles de capture).

La pile construite pendant votre tour peut être déplacée, et réciproquement, la pile déplacée pendant votre tour peut être déconstruite en déplaçant son sommet. Cet enchaînement de 2 actions est possible une seule fois pendant votre tour.

## Règles de capture
Sachant qu'une "unité" désigne un cube ou une pile, seules les unités “pierre/feuille/ciseaux” se capturent entre elles, et indépendamment de leurs hauteurs (exemple : un cube peut capturer une pile). Les unités "sage" ne capturent jamais et ne sont jamais capturées.

Le rôle “pierre/feuille/ciseaux/sage" d’une pile est déterminé par le cube à son sommet. Le sommet d'une pile n'est jamais capturé seul : c'est toute la pile qui est capturée. 

Un cube "sage" peut être capturé s'il est en bas d'une pile "pierre/feuille/ciseaux".

Une unité capture une unité adverse par déplacement à condition de respecter l’ordre suivant des rôles : "pierre" capture "ciseaux" ; "ciseaux" capture "feuille" ; "feuille" capture "pierre".

Toute unité capturée est retirée définitivement du plateau.

## Copyright

[![Creative Commons License](./pictures/CC-BY-NC-SA.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/) Copyright (C) 2022 Lucas Borboleta. Pijersi, règles d'un jeu pour 2 joueurs, de Lucas Borboleta (https://github.com/LucasBorboleta/pijersi) est mis à disposition selon la licence Creative Commons Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International ; visitez http://creativecommons.org/licenses/by-nc-sa/4.0/. Les autorisations au-delà du champ de cette licence peuvent être obtenues à [lucas.borboleta@free.fr](mailto:lucas.borboleta@free.fr).
