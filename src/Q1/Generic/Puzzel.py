"""
Puzzel.py
========================
This module contains the Puzzel class which runs the A* search and
finds the solution to the given Board and to reach the given goal.
"""

from Board import Board
from HeuristicFunc import HeuristicFunc

class Puzzel():
    """
    This class runs the A* algorithm to complete
    the puzzel.
    """

    """
    This contains all the possible boards and 
    is ordered from min to max heuristic score.
    """
    open = []

    """
    This contains all the boards / states which have
    been traversed.
    """
    closed = []

    """
    This is the start state (starting board).
    """
    initial = None

    """
    This is the huristic function which is being used.
    """
    heuristic = None

    def __init__(self, board : Board, heuristic : HeuristicFunc) -> None:
        """
        This is the initaliser for the Puzzel and asigns the first board
        to the initail attribute and adds it to the list of open boards.
        The heuristic is asigned to its attribute and then used to calculate
        the heuristic score of the initial board.

        :param board: The starting board (state).
        :type board: Board
        :param heuristic: The heuristic function being used.
        :type board: HeuristicFunc
        """
        self.initial = board
        self.heuristic = heuristic
        board.hValue = self.heuristic.calculate(board)
        self.open.append(self.initial)
    
    def notInClosed(self, board):
        """
        This function checks if a board is in the closed list,
        meaning that it has already been explored.

        :param board: The board being checked if in closed.
        :type board: Board

        :return : If Board is in closed.
        :rtype: bool
        """
        for item in self.closed:
            if item.board == board.board:
                return False
        
        return True

    def getMinHValue(self, children):
        """
        This function is used to get the minimul heuristic value of
        the all the children in children.

        :param children: A list of all the child boards.
        :type children: list

        :return : the minimum heuristic function value
        :rtype: int
        """
        if len(children) > 0:

            minValue = children[0].hValue

            for child in children:
                if child.hValue < minValue:
                    minValue = child.hValue
        
        else:
            minValue = -1
            
        return minValue

    def getEarlyCount(self) -> int:
        """
        This function calculates the number of early pairs in the initial
        board, this is used to then calculate if the board is solvable
        or impossible to solve.

        :return : The number of early pairs.
        :rtype: int
        """
        earlyCount = 0

        combinedInitial = []

        for row in self.initial.board:
            for item in row:
                combinedInitial.append(item)

        for i in range(0, 9):
            for j in range(i+1, 9):
                if combinedInitial[j] != "*" and combinedInitial[i] != "*" and combinedInitial[i] > combinedInitial[j]:
                    earlyCount += 1

        return earlyCount

    def checkSolvable(self) -> bool:
        """
        This function is used to check if the intial board is solvable.

        :return : If the initial board is solvable.
        :rtype: bool
        """
        earlyCount = self.getEarlyCount()

        return (earlyCount % 2 == 0)

    def solve(self) -> None:
        """
        This function carries out the A* search and solves the
        board to reach the end goal.

        The function displays all the moves that it is making.
        """
        solution = []

        while True:
            curBoard = self.open[0]

            if curBoard.isSolved():
                solution = curBoard.getParents()
                break

            children = curBoard.getChildrenBoards()

            validChildren = []

            for child in children:
                if self.notInClosed(child):
                    child.hValue = self.heuristic.calculate(child)
                    validChildren.append(child)

            minHVal = self.getMinHValue(validChildren)

            for child in children:
                if child.hValue == minHVal:
                    self.open.append(child)

            self.open.remove(curBoard)

            self.closed.append(curBoard)

            self.open.sort(key=lambda b:b.hValue, reverse=False)

        return solution
