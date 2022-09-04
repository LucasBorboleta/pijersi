# Pijersi : rules of the game


![](./pictures/pijersi-2022-0723-0940.jpg)

Game kind: cross win condition + stacking + capturing

![](./pictures/schema.png)

<div style="page-break-after: always;"></div>

## Introduction

In the game "pijersi", two players, white and black, move their cubes, alone or in dynamic stacks, which compete in their roles of "rock", "paper", "scissors" and "wise man". Each player attempts to reach first the last opposing line. 

The game "[pijersi](https://github.com/LucasBorboleta/pijersi)" is a variant of the game "[jersi](https://github.com/LucasBorboleta/jersi)". In [Lojban](https://mw.lojban.org/), the root "prije" and its affix "pi" mean "wise", while the root "jersi" means "to chase" or "to pursue". Pronounce `/pee/jer/see/`.

## General information

Number of players: 2 / Minimum age: 8 years / Game duration: 15 minutes 

## Components

You (white/black player) have 14 cubes in your color (in the photo: black => red). The 6 same faces of a cube define its role (example: rock). You have:

- 4 "rock", 4 "paper" and 4 "scissors" (the letters "R/P/S" or the symbols "circle/square/cross").
- 2 "wise man", just called "wise" (the letter "W" or the symbol "infinity").

The following hexagonal board, of 45 spaces and 7 lines, is arranged between the 2 players:

```
   1 2 3 4 5 6      [line “g”]
  1 2 3 4 5 6 7     [line “f”]
   1 2 3 4 5 6      [line “e”]
  1 2 3 4 5 6 7     [line “d”]
   1 2 3 4 5 6      [line “c”]
  1 2 3 4 5 6 7     [line “b”]
   1 2 3 4 5 6      [line “a”]
```

## Set up

On the 2 lines closest to you ("ab" for white and "fg" for black), you put your cubes as shown below. Your "wise" cubes are stacked. The white player starts the game. 

Here the uppercase letters identify the cubes of white and the lowercase those of black.

```
      s.  p.  r.  s.  p.  r.
    p.  r.  s.  ww  r.  s.  p.
      ..  ..  ..  ..  ..  ..
    ..  ..  ..  ..  ..  ..  ..
      ..  ..  ..  ..  ..  ..
    P.  S.  R.  WW  S.  R.  P.
      R.  P.  S.  R.  P.  S.
```

## Goal of the game

You must bring first at least one of your "rock/paper/scissors" cubes to the last opposing line (white targets the "g" line and black targets the "a" line) or else must prevent your opponent from playing in turn. The game is a tie after 20 turns without any capture since the beginning or the last capture.

## Stacking rules

Cube movements (which are explained below) make it possible to build stacks that must comply with the following rules.

A stack is limited to any 2 cubes of the same color, except that a “wise” cube only stacks on top of a “wise” cube.

## Moving rules

A cube, alone or at the top of a stack, moves from a single space, either to an empty space or to an occupied space to stack on top of another cube (respecting the stacking rules) or to capture an opposing cube or stack (respecting the capturing rules that are explained below).

A stack moves straight 1 or 2 spaces, without forking or jumping over occupied spaces, either to an empty space or to an occupied space to capture an opposing cube or stack (respecting the capturing rules).

The stack built during your turn can be moved, and conversely, the stack moved during your turn can be unbuilt by moving its top. This sequence of 2 actions is possible only once during your turn.

## Capturing rules

Knowing that a "unit" refers to a cube or a stack, only the "rock/paper/scissors" units capture each other, and regardless of their heights (example: a cube can capture a stack). "Wise" units never capture and are never captured.

The role "rock/paper/scissors/wise" of a stack is determined by the cube at its top. The top of a stack is never captured alone: the entire stack is captured.

A unit captures an opposing unit by moving if it respects the following order of roles: "rock" captures "scissors"; "scissors" captures "paper"; "paper" captures "rock". 

A "wise" cube can be captured if it is at the bottom of a "rock/paper/scissors" stack.

Any captured unit is permanently removed from the board.

## Copyright

[![Creative Commons License](./pictures/CC-BY-NC-SA.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/) Copyright (C) 2022 Lucas Borboleta.

Pijersi, rules of a strategy game for two players, by Lucas Borboleta (https://github.com/LucasBorboleta/pijersi) is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

Permissions beyond the scope of this license may be available at [lucas.borboleta@free.fr](mailto:lucas.borboleta@free.fr).
