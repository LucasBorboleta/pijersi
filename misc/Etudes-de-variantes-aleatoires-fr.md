# Etudes de variantes aléatoires

## Motivation

Ce document explore des variantes de la **mise en place aléatoires des cubes**. La motivation de cette exploration est de renouveler la réflexion sur le jeu de "pijersi" en évitant les automatismes des ouvertures apprises pour la mise en place standard/classique.

## Principes libéraux : full-random et half-random

Les principes suivants procurent beaucoup de liberté et sont très simples à mettre en œuvre :

* Une pile légale est constituée au centre de la seconde rangée de départ.

* Une fois les cubes blancs mise en place aléatoirement :
  * **` full-random`**: les cubes noirs sont soit tirés aléatoirement et indépendamment des cubes blancs ;
  *  **` half-random`**: les cubes noirs sont positionnés par symétrie centrale vis-à-vis des cubes blancs.


## Principes conservateurs

Les principes suivants guident les mélanges aléatoires proposées afin d'assurer un certain équilibre entre les blancs et les noirs :

- Les sages restent empilés de façon standard, au centre de la seconde rangée de départ.
- Les cubes blancs sont mélangés selon une procédure donnée, puis les cubes noirs sont placés en respectant une symétrie centrale vis-à-vis des blancs, comme dans la mise en place standard.

Les variantes qui suivent sont nommées d'après le nombre de combinaisons générées. Cependant, le nombre effectif de ces combinaisons devrait être divisé par 6, qui correspond aux nombres de permutations de Rock-Paper-Scissors (RPS). Ainsi, Pijersi-24 fournit $24/6=4$ combinaisons effectives.

## Pijersi-24

Cette variante applique les principes suivants :

- La deuxième rangée est déterminée par complétion par triangle, comme dans la mise en place standard, après la mise en place de la première rangée.
- Sur la première rangée : 
  - à gauche, un premier triplet RPS est mélangé, qui donne XYZ ; 
  - à droite, un second triplet RPS est mélangé, qui donne X'Y'Z' ;
  - si X' est égale à X alors un nouveau mélange est nécessaire.


Pour un triplet XYZ à gauche, les triplets X'Y'Z' possibles à droite sont au nombre de 4. En effet, les possibilités de complétion pour la première rangée sont les suivantes :

| Index complétion | Complétion |
| ---------------- | ---------- |
| 0                | XYZ-XYZ    |
| 1                | XYZ-XZY    |
| 2                | XYZ-YXZ    |
| 3                | XYZ-YXZ    |

La complétion de la deuxième rangée se fait séparément sur le triplet de gauche et sur le triplet de droite :

- Triplet la rangée 2 : -Z-X-Y
- Triplet la rangée 1 : X-Y-Z

Le nombre de combinaisons possibles est $24$.

En effet, il y a 6 combinaisons XYZ par mélange de RPS pour le triplet de gauche. Et, il y a 4 façons de mélanger le triplet de droite X'Y'Z' qui évite X'=X. Donc, $6\times 4 = 24$ combinaisons au total.

## Pijersi-36

Cette variante, qui reprend la variante Pijersi-24, mais en autorisant X'=X, fournit $36$ combinaisons.

## Pijersi-1296
Cette variante mélange séparément 4 triplets RPS. Ce qui donne $t_1=(X_1, Y_1, Z_1)$, $t_2=(X_2, Y_2, Z_2)$, $t_3=(X_3, Y_3, Z_3)$, $t_4=(X_4, Y_4, Z_4)$. La première rangée est définie par la séquence $t_1$, $t_2$. La deuxième rangée est définie par la séquence $t_3$, $t_4$.

Cette variante fournit $1296$ combinaisons, soit $6 \times 6 \times 6 \times 6$.

## Pijersi-8100
Cette variante mélange séparément l'aile gauche et l'aile droite. Chaque aile comprend un triplet sur la première rangée et un triplet sur la deuxième rangée. Chaque aile mélange RRPPSS.

Chaque triplet d'une aile aura au plus un cube répété, comme dans RRP.

Le nombre d'arrangements sur chaque aile correspond aux assignements par paires de 1, 2, 3, 4, 5, 6 vers RR, PP et SS, soit $(6\times 5)/2 \times (4\times 3)/2 = 15\times 6 = 90$. 

Cette variante fournit $8100$ combinaisons, soit $90\times 90$.

## Notation positionnelle

La notation d'une partie de Pijersi avec positions aléatoires nécessite un préambule qui identifie les positions de départ des cubes. La notation positionnelle suivante remplie ce rôle, et pourra même être utilisée pour noter des exercices qui démarre en milieu de partie.

Voici les principes de notation des positions :

- L'absence de notation de positions indique que les positions de départ sont standard.
- Les positions sont toutes notées avant le premier mouvement.
- Une même ligne ne peut pas noter une position et un mouvement.
- Une même ligne peut noter plusieurs positions séparées par un ou plusieurs espaces.
- Une position commence par un label, tel que "a1" pour une case, ou tel que  "a13" pour les 3 cases "a1", "a2", "a4" d'une même rangée.
- Le label de position est suivi du caractère ":", puis d'un cube ou d'une pile pour un label simple, tel que "a1", ou d'autant de cubes ou piles que requis par un label multiple tel que "a13".
- Une pile est notée entre en commençant pas son sommet, tel que "RW" qui désigne une "pierre" empilée sur un "sage". 
- Une pile est toujours notée sur une position dédiée, non combinée avec d'autres cubes ou d'autres piles.
- Les cubes blancs sont notés par des lettres majuscules, à l'anglaise : R (pierre), P(feuille=papier), S(ciseaux), W(sage). Les cubes noirs sont notés par les mêmes lettres, mais en minuscules : r, p, s, w.

Exemples :

-  a1:R  b4:RW  f4:ww  f13:rps
- a16:RPSRPS b13:RPS  b4:WW  b56:RPS
