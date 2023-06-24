# Variantes aléatoires


[TOC]

## Motivation

Ce document explore des variantes de la **mise en place aléatoires des cubes**. La motivation de cette exploration est de renouveler la réflexion sur le jeu de "pijersi" en évitant les automatismes des ouvertures apprises pour la mise en place standard.

## Principes généraux

Les principes suivants guident les mélanges aléatoires proposées afin d'assurer une équilibre entre les blancs et le noirs :

- Les sages restent empilés de façon standard, au centre de la seconde rangée de départ.
- Les cubes blancs sont mélangés selon une procédure donnée, puis les cubes noirs sont placés en respectant une symétrie centrale vis-à-vis des blancs, comme dans la mise en place standard.

Les variantes qui suivent sont nommées d'après le nombre de combinaisons générées. Cependant, le nombre effectif de ces combinaisons devraient être divisé par 6, qui correspond aux nombres de permutations de Rock-Paper-Scissors (RPS). Ainsi, Pijersi-24 fournit $24/6=4$ combinaisons effectives.

## Pijersi-24

Cette variante applique les principes suivants :

- La deuxième rangée est déterminée par complétion par triangle, comme dans la mise en place standard, après la mise en place de la première rangée.
- Sur la première rangée : 
  - à gauche, un premier triplet RPS est mélangé, qui donne XYZ ; 
  - à droite, un second triplet RPS est mélangé, qui donne X'Y'Z' ;
  - si X' est égale à X alors un nouveau mélange est nécessaire.


Pour un triplet XYZ à gauche, les triplets X'Y'Z' possibles à droite sont au nombre de 4. En effet, les possibilités pour la première rangée sont les suivantes :

1. XYZ-XYZ
2. XYZ-XZY
3. XYZ-YXZ
4. XYZ-YXZ

La complétion de la deuxième rangée se fait séparément sur le triplet de gauche et sur le triplet de droite :

- Triplet la rangée 2 : -Z-X-Y
- Triplet la rangée 1 : X-Y-Z

Le nombre de combinaisons possibles est $24$.

En effet, il y a 6 combinaisons XYZ par mélange de RPS pour le triplet de gauche. Et, il y a 4 façons de mélanger le triplet de droite X'Y'Z' qui évite X'=X. Donc, $6\times 4 = 24$ combinaisons au total.

## Pijersi-36

Cette variante, qui reprend la variante Pijersi-24, mais en autorisant X'=X, fournit $36$ combinaisons.

## Pijersi-1296
Cette variante mélange séparément 4 triplets RPS. Ce qui donne $T_1=(X_1, Y_1, Z_1)$, $T_2=(X_2, Y_2, Z_2)$, $T_3=(X_3, Y_3, Z_3)$, $T_4=(X_4, Y_4, Z_4)$. La première rangée est définie par la séquence $T_1$, $T_2$. La deuxième rangée est définie par la séquence $T_3$, $T_4$.

Cette variante fournit $1296$ combinaisons, soit $6 \times 6 \times 6 \times 6$.

## Pijersi-8100
Cette variante mélange séparément l'aile gauche et l'aile droite. Chaque aile comprend un triplet sur la première rangée et un triplet sur la deuxième rangée. Chaque aile mélange RRPPSS.

Chaque triplet d'une aile aura au plus un cube répété, comme dans RRP.

Le nombre d'arrangements sur chaque aile correspond aux assignements par paires de 1, 2, 3, 4, 5, 6 vers RR, PP et SS, soit $(6\times 5)/2 \times (4\times 3)/2 = 15\times 6 = 90$. 

Cette variante fournit $8100$ combinaisons, soit $90\times 90$.
