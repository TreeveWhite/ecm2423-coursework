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

    goal = [
        ["*", "1", "2"],
        ["3", "4", "5"],
        ["6", "7", "8"]
    ]

    ui = UserInterface()

    board = Board.fromFilename("puzzle.txt", 0, goal)

    heuristicMeth = ui.getHeuristicMethod()

    if heuristicMeth == "MD":
        heuristic = ManhattanDistance(goal)
    elif heuristicMeth == "MT":
        heuristic = MisplacedTiles(goal)
    else:
        raise Exception("Error : Entered value does not relate to one of the given options.")

    puzzel = Puzzel(board, heuristic)

    solution = puzzel.solve()

    ui.printSolution(solution, goal)
    