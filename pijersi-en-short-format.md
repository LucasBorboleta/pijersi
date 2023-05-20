# Pijersi : rules of the game

## Introduction

In the game "pijersi", two players, white and black, move their cubes, alone or in dynamic stacks, which compete in their roles of "rock", "paper", "scissors" and "wise man". Each player attempts to reach first the last opposing line. 

## Components

You (white/black player) have 14 cubes in your color. The 6 same faces of a cube define its role (example: rock). You have:

- 4 "rock", 4 "paper" and 4 "scissors" (respectively the symbols "circle/square/cross").
- 2 "wise man", just called "wise" (the symbol "infinity").

The following hexagonal board, of 45 spaces and 7 lines, is arranged between the 2 players:

<img src="./pictures/pijersi-positions-initiales.png" style="zoom:50%;" />

## Set up

On the 2 lines closest to you ("ab" for white and "fg" for black), you put your cubes as shown above. Your "wise" cubes are stacked. You fill in your back line from left to right, with two rock-paper-scissors sequences. Then, you complete your two lines by building rock-paper-scissors triangles.

The white player starts the game. 

## Goal of the game

You must bring first at least one of your "rock/paper/scissors" cubes to the last opposing line (white targets the "g" line and black targets the "a" line) or else must prevent your opponent from playing in turn. The game is a tie after 20 turns without any capture since the beginning or the last capture.

## Stacking rules

Cube movements (which are explained below) make it possible to build stacks that must comply with the following rules.

A stack is limited to any 2 cubes of the same color, except that a “wise” cube only stacks on top of a “wise” cube.

A stack is unbuilt by moving the cube at its top (respecting the moving rules).

## Moving rules

A cube, alone or at the top of a stack, moves from a single space, either to an empty space or to an occupied space to stack on top of another cube (respecting the stacking rules) or to capture an opposing cube or stack (respecting the capturing rules that are explained below).

A stack moves straight 1 or 2 spaces, without forking or jumping over occupied spaces, either to an empty space or to an occupied space to capture an opposing cube or stack (respecting the capturing rules).

The stack built during your turn can be moved, and conversely, the stack moved during your turn can be unbuilt by moving its top. This sequence of 2 actions is possible only once during your turn.

## Capturing rules

Knowing that a "unit" refers to a cube or a stack, only the units in role "rock/paper/scissors" capture each other, and regardless of their heights (example: a cube can capture a stack). Units in role "wise"  never capture and are never captured.

The role "rock/paper/scissors/wise" of a stack is determined by the cube at its top. The top of a stack is never captured alone: the entire stack is captured.

A unit captures an opposing unit by moving if it respects the following order of roles: "rock" captures "scissors"; "scissors" captures "paper"; "paper" captures "rock". 

A "wise" cube can be captured if it is at the bottom of a stack in role "rock/paper/scissors" .

Any captured unit is permanently removed from the board.

The rules for moving a stack and its top allow two captures in a turn.

[![Creative Commons License](./pictures/CC-BY-NC-SA.png)](http://creativecommons.org/licenses/by-nc-sa/4.0/) Copyright (C) 2022  [lucas.borboleta@free.fr](mailto:lucas.borboleta@free.fr) ; license Creative Commons BY-NC-SA
