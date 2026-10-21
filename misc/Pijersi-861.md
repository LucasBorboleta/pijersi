# Variante : Pijersi 861

Ce document décrit « Pijersi 861 », une variante de la mise en place standard du jeu abstrait Pijersi.

## Motivation

Conçue pour répondre aux craintes des joueurs et des éditeurs redoutant le « syndrome des échecs modernes » — où la mémorisation mécanique des ouvertures étouffe la créativité — cette variante s'inscrit dans la droite lignée de la philosophie de Bobby Fischer et de ses célèbres Échecs 960 (Fischer Random Chess). Pijersi 861 ramène le jeu à son essence pure : l'adaptation tactique immédiate face à l'inconnu et le talent brut d'analyse, plutôt que l'apprentissage par cœur de lignes théoriques précalculées.

## 1. Protocole de Mise en Place

Afin de limiter la mémorisation des théories d'ouverture tout en préservant l'équilibre tactique, la préparation du plateau repose sur le processus suivant :

1. **L'Invariant des Sages :** Les cubes sages de chaque camp sont empilés et positionnés au centre de leur rangée de départ avant, conformément au placement classique.
2. **Le Tirage Aléatoire :** Les cubes restants de chaque camp sont indépendamment mélangés dans des sacs séparés. Ils sont ensuite piochés à l'aveugle et placés à plat sur la grille en remplissant les 12 cases restantes, d'abord la première ligne de gauche à droite.
3. **La Phase d'Échange (Swaps) :** Un joueur (désigné temporairement "Blanc") peut échanger les positions de deux de ses cubes (à l'exception des sages), ou bien passer son tour. Le joueur adverse (temporairement "Noir") effectue la même action de son côté. Ce processus de permutation est répété une seconde fois. En configuration de tournoi, un chronomètre dédié (ex: 1 minute de crédit par joueur) peut encadrer cette phase.
4. **L'Attribution (Blind Draft) :** L'identité définitive des camps (qui joue les Blancs, et donc qui a l'avantage du trait) est déterminée par un tirage au sort aléatoire une fois les configurations de départ verrouillées par les swaps.
5. **Le Coup d'Envoi :** Le joueur ayant reçu les Blancs débute la partie.

## 2. L'Espace d'Ouverture : Les 34 650 Tirages

La pioche aveugle génère une diversité contrôlée des ouvertures possibles.

●   **L'inventaire initial :** Chaque joueur dispose de 14 cubes (4 Pierres, 4 Feuilles, 4 Ciseaux et 2 Sages).

●   **La topologie :** La zone de déploiement s'étale sur 13 cases réparties sur les deux premières rangées. L'invariant des Sages monopolisant la case centrale de la rangée avant, il reste **12 cases distinctes** pour placer les 12 cubes restants.

### Démonstration

Le calcul s'appuie sur une permutation avec répétition, distribuant 12 éléments répartis en trois sous-groupes d'éléments identiques (4 Pierres, 4 Feuilles, 4 Ciseaux).

N = 12! / (4! × 4! × 4!)
 N = 479 001 600 / (24 × 24 × 24)
 N = 479 001 600 / 13 824
 N = 34 650 tirages
 

Il existe donc **34 650 configurations brutes possibles** pour remplir le camp d'un joueur avant la phase d'ajustement.

## 3. La Phase de Correction : Les 861 États Accessibles

La phase d'échange autorise jusqu'à deux permutations successives (swaps) pour corriger d'éventuelles anomalies statistiques du tirage. Échanger deux cubes possédant le même rôle équivaut visuellement à une action neutre ("ne rien faire").

### Démonstration de la couverture du voisinage

Sur l'espace du groupe symétrique des 12 cubes, l'application de ≤ 2 transpositions définit un voisinage composé des dérangements valides suivants (situations où les cubes modifient réellement leur rôle visuel sur la grille) :

1. **L'Identité (0 case modifiée) :** Le joueur choisit de ne pas modifier sa pioche.

○   Total : **1 configuration**

2. **Une Transposition (2 cases modifiées) :** Le joueur effectue un seul swap effectif en échangeant deux cubes de rôles différents. Ce swap s'opère parmi les 3 paires de rôles croisées (R-P, R-S, P-S), chacune offrant (4 × 4) = 16 combinaisons.

○   Total : 16 × 3 = **48 configurations**

3. **Un Cycle de longueur 3 (3 cases modifiées) :** Obtenu par 2 swaps s'intersectant. Pour modifier l'aspect visuel de 3 cases, le cycle doit inclure un cube de chaque rôle (1 R, 1 P, 1 S). Il y a (4 × 4 × 4) = 64 sélections possibles pour ces trois pièces, et pour chacune, 2 sens de rotation valides (R→P→S ou R→S→P).

○   Total : 64 × 2 = **128 configurations**

4. **Deux Transpositions disjointes (4 cases modifiées) :** Obtenues par 2 swaps indépendants, divisées en deux catégories :

○   *4A - Révision de deux paires complètes :* 3 combinaisons de rôles possibles. Exemple pour (Pierres, Feuilles) : (6 sélections de paires R) × (6 sélections de paires P) × (1 dérangement où les paires s'échangent intégralement) = 36. Soit 36 × 3. Total : **108 configurations**.

○   *4B - Révision impliquant une paire majoritaire et deux isolés :* 3 rôles possibles pour la paire majoritaire. Exemple pour la paire (R) échangée contre (1 P, 1 S) : (6 sélections de paires R) × (4 sélections de P) × (4 sélections de S) = 96 sélections. L'échange croisé impose 2 distributions valides (R→P, R→S ou l'inverse). Soit 96 × 2 × 3. Total : **576 configurations**.

L'addition des états accessibles uniques (1 + 48 + 128 + 108 + 576) donne un rayon d'action total de **861 configurations locales**.

Cette jauge limite le champ d'action du joueur sans briser la nécessité d'adaptation face à la pioche aléatoire brute, justifiant ainsi le nom technique de la variante.
