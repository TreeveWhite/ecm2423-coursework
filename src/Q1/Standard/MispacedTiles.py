"""
MisplacedTiles.py
=========================
This module is used to define the Misplaced Tiles heuristic function
and is a child of the HeuristicFunc class.
"""

from HeuristicFunc import HeuristicFunc

class MisplacedTiles(HeuristicFunc):
    """
    This class defined the claculateHScore method for the Misplaced
    Tiles algorithm. This clauclates the number of tiles which are not
    in the correct location.
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

            if (boardx != goalx) or (boardy != goaly):
                distance += 1
            
        return distance