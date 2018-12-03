# Let's play CHECKERS !!!

## How to play
Ready for the challenge? Just run the ``main.py`` file and a board will be displayed.

First player has the yellow pieces, the second, the blues ones.

To play, just select one of your pieces. It will be marked in green. Then select where you want to move it, in the right order. Sure about your move? Just press ``Return`` on your keyboard and there we go!

Not sure? Did you clicked in a bad square? Do you want to change something? No problem! Just click again one of your pieces and *voilà*: a fresh new start for you.

A message appears when there is a winner.
## Code structure
There are two main objects
- ``Game``

Holds the logical structure of the game. Verifies if a given move is valid or not and execute it.
The board is represented on a 8x8 structure. 0 represents a empty space, 1 and 2 the players 1 and 2 and 11 and 12 are for checkers. 

- ``Board``

Responsable for visually represent the game. It has a 8x8 matrix of ``Squares`` and can change their background colors and pieces. Each Square has a default background color (black or white) and can or not have a piece.

There is a forth objetc there is ``GameState``. It holds informations about each move: who is the actual player, the pieces he has selected and how much remaining pieces each of then have.

Finaly we have the ``main`` file, who unites those classes.
