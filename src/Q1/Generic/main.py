"""
main.py
====================
This module contains the runner methods which run the entire system.
"""

from Board import Board
from ManhattanDistance import ManhattanDistance
from MispacedTiles import MisplacedTiles
from UserInterface import UserInterface
from Puzzel import Puzzel

if __name__ == "__main__":

    ui = UserInterface()

    board = ui.getBoard("Initial")

    goal = ui.getBoard("Goal")

    board = Board(board, 0, goal)

    heuristicMeth = ui.getHeuristicMethod()

    if heuristicMeth == "MD":
        heuristic = ManhattanDistance(goal)
    elif heuristicMeth == "MT":
        heuristic = MisplacedTiles(goal)
    else:
        raise Exception("Error : Entered value does not relate to one of the given options.")

    puzzel = Puzzel(board, heuristic)

    if puzzel.checkSolvable():

        solution = puzzel.solve()

        ui.printSolution(solution, goal)
    
    else:

        ui.puzzleNotSolvable()
    