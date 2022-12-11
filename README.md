# PokleSolver
Set of python scripts that will output all possible solutions for a given Pokle game

To input the information relevant to the current game, there are variables at the top of the PokleSolver.py file representing the player's hands,
and the relative rankings of each players hands after the flop, turn, and river.

For each player, there is a two element array of Card objects representing their hand, and an array of integers representing their rank at each stage

A card object is created using an integer representation of its rank and its suit(more info in the comments of Card.py).

After set-up is completed run the PokleSolver.py script, and it will create 3 ouput files representing the possible cards for the flop, turn, and river.
