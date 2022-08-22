"""
Heuristic.py
====================
This module holds the HeuristicFucn class which defines the features of all
Heuristic Function objects which are children of this class. It is inhertited
by both the ManhattanDistance and MisplacedTiles classes.
"""

from Board import Board


class HeuristicFunc:
    """
    This class defines what a Heuristic 
    Function Class must define and do.

    The calculate HScore must be defined
    by the child class.
    """

    """
    This is the goal state the puzzle
    wants to reach. 
    """
    goal = None

    def __init__(self, goal : list) -> None:
        """
        This is the initialiser for a heuristif function
        and sets the given goal to the goal attribute
        of the object.

        :param goal: The goal state.
        :type goal: list

        :return: Nothing is returned
        :rtype: None
        """
        self.goal = goal

    def calculateHScore(self, board : Board) -> int:
        """
        This function calculates the output of the heuristic
        fuction which is currently being run.

        :param board: The current board / state.
        :type goal: Board

        :return: The heuristic score of the given board
        :rtype: int
        """
        pass

    def calculate(self, board):
        """
        This function returns the sum of the heuristic score
        and the level (depth) the current board (state) is on.

        :param board: The current board / state.
        :type goal: Board

        :return: The total heuristic score
        :rtype: int
        """
        return self.calculateHScore(board) + self.calculateGScore(board)

    def calculateGScore(self, board : Board) -> int:
        """
        This function outputs te current level (depth)
        the puzzle is on.

        :param board: The current board / state.
        :type goal: Board

        :return: The level (depth) o the current state.
        :rtype: int
        """
        return board.level
    
    def find(self, value : str, board : Board) -> tuple:
        """
        This function finds the x and y coordinate of a value
        in a board.

        :param value: The value being searched for.
        :type value: str
        :param board: The current board / state.
        :type goal: Board

        :return: The x and y coordinate of the value
        :rtype: tuple
        """
        for row in board:
            if value in row:
                return row.index(value), board.index(row)