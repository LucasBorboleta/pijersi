# pijersi
Dans le jeu “pijersi”, deux joueurs, blanc et noir, manœuvrent leurs cubes, seuls ou en piles dynamiques, qui s’affrontent dans leurs rôles de pierre, feuille, ciseaux et sages. Chaque joueur s’efforce d’atteindre le premier la dernière ligne adverse. 

Le jeu "[pijersi](https://github.com/LucasBorboleta/pijersi)” est une variante du jeu “[jersi](https://github.com/LucasBorboleta/jersi)”. En [lojban](https://mw.lojban.org), la racine “prije” et son affixe “pi” signifient “sage”, tandis que la racine “jersi” signifie “chasse” ou “poursuite”. Prononcer `/pi/jer/ssi/`.

## Informations générales
Nombre de joueurs : 2 / Age minimum : 8 ans / Durée de partie : 30 minutes 

## Matériel
Chaque joueur, blanc ou noir, dispose de 14 cubes à sa couleur, chacun avec le même signe sur ses 6 faces et répartis en 2 qualités :

- Les cubes de la qualité “ciel” : 4 pierres “R”, 4 feuilles “P” et 4 ciseaux “S”.
- Les cubes de la qualité “terre” : 2 sages “W”.

Le plateau hexagonal suivant, de 51 cases, est disposé entre les 2 joueurs:

```
   1 2 3 4 5 6    [ligne “g”]
  1 2 3 4 5 6 7   [ligne “f”]
 1 2 3 4 5 6 7 8  [ligne “e”]
1 2 3 4 5 6 7 8 9 [ligne “d”]
 1 2 3 4 5 6 7 8  [ligne “c”]
  1 2 3 4 5 6 7   [ligne “b”]
   1 2 3 4 5 6    [ligne “a”]
```

## Mise en place
Sur les 2 lignes les plus proches d’eux (“ab” pour blanc et “fg” pour noir), les joueurs placent leurs cubes comme indiqué ci-dessus. Les sages sont empilés. Le joueur blanc entame la partie.

```
      s.  p.  r.  s.  p.  r.
    p.  r.  s.  ww  r.  s.  p.
..  ..  ..  ..  ..  ..  ..  ..
..  ..  ..  ..  ..  ..  ..  ..  ..
  ..  ..  ..  ..  ..  ..  ..  ..
    P.  S.  R.  WW  S.  R.  P.
      R.  P.  S.  R.  P.  S.
```

## But du jeu
Pour gagner, un joueur doit amener au moins un de ses cubes “ciel” sur la dernière ligne adverse (blanc vise la ligne “g” et noir vise la ligne “a”) ou bien doit empêcher le joueur adverse de jouer à son tour.

## Règles de pile
Les déplacements de cubes (expliqués ci-dessous) permettent de construire des piles qui doivent respecter les règles suivantes:

- Une pile est limitée à 2 cubes de même couleur.
- Un cube “ciel” s’empile sur un cube “ciel” ou  sur un cube “terre”.
- Un cube “terre” s’empile seulement sur un cube “terre”.

## Règles de déplacement
Un cube, seul ou au sommet d’une pile, se déplace d’une seule case, soit vers une case vide, soit vers une case occupée pour s’empiler sur un autre cube (en respectant les règles de pile) ou pour capturer un cube ou une pile adverse (en respectant les règles de capture).

Une pile se déplace, sans bifurquer, ni sauter par dessus des cases occupées, de 1 ou 2 cases, soit vers une case vide, soit vers une case occupée pour capturer un cube ou une pile adverse (en respectant les règles de capture).

Toute pile constituée pendant son tour peut être déplacée. Toute pile déplacée pendant son tour peut être dépilée. Cette seconde action enchaînée n’est possible qu’une seule fois par tour. 

## Règles de capture
Seules les unités (cube ou pile) “ciel” se capturent entre elles, et indépendamment de leurs hauteurs (par exemple, un cube peut capturer une pile).

La qualité “ciel” ou “terre” et le rôle pierre, feuille ou ciseaux d’une pile sont déterminés par le cube à son sommet. Le sommet d'une pile n'est jamais capturé seul : c'est toute la pile qui est capturée.

Une unité “ciel” capture une unité “ciel” adverse par déplacement à condition de respecter l’ordre suivant des rôles : pierre capture ciseaux ; ciseaux capture feuille ; feuille capture pierre.

Toute unité capturée est retirée définitivement du plateau.

## Copyright
[![Creative Commons License](./pictures/CC-BY-NC-SA.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/)

Copyright (C) 2022 Lucas Borboleta.

PIJERSI, rules of a strategy game for two players, by Lucas Borboleta (https://github.com/LucasBorboleta/pijersi) is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Permissions beyond the scope of this license may be available at [lucas.borboleta@free.fr](mailto:lucas.borboleta@free.fr).
