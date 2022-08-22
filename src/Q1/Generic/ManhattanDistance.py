"""
ManhattanDistance.py
=============================
This module contains the code for a ManhattanDistance class which is a 
child of the HeuristicFunc class."""

from HeuristicFunc import HeuristicFunc


class ManhattanDistance(HeuristicFunc):
    """
    This class defined the heurstic function for 
    Manhattan distance which is the sum of distances
    each tile must move to reach its position in the goal.
    """

    def __init__(self, goal) -> None:
        #Docstrings inherited from HeuristicFunc
        #See HeuristicFunc.py for further details
        super().__init__(goal)

    def calculateHScore(self, board):
        #Docstrings inherited from HeuristicFunc
        #See HeuristicFunc.py for further details
        distance = 0

        for num in range(1, 9, 1):
            boardx, boardy = self.find(str(num), board.board)
            goalx, goaly = self.find(str(num), self.goal)

            distance += abs(boardx - goalx) + abs(boardy - goaly)
        
        boardx, boardy = self.find("*", board.board)
        goalx, goaly = self.find("*", self.goal)

        distance += abs(boardx - goalx) + abs(boardy - goaly)

        return distance
