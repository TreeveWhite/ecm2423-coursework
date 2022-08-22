"""
Board.py
====================
This module contains the class used to define a Board and
all the operation which can be applied to a Board object.
"""

class Board:
    """
    This class defines a board and 
    all the possible operations which
    can be applied to a board.
    """

    """
    The actual data on the board.
    """
    board = []

    """
    The data representation of the goal
    state the board is attempting to
    reach.
    """
    goal = []

    """
    The level (depth) of the board.
    """
    level = 0

    """
    The heuristic value of the board.
    """
    hValue = None

    """
    The parent node (grid) of the child.
    """
    parent = None

    def __init__(self, board : list,level : int, goal : list, parent = None) -> None:
        """
        This function is the initaliser for the class
        and asigns the board, level and goal to their 
        respective attributes in the class.

        :param board: The data of the board / state.
        :type goal: Board
        :param level: The level (depth) of the board.
        :type goal: int
        :param goal: The goal board / state.
        :type goal: list

        :return: Nothing is returned
        :rtype: None
        """
        self.board = board
        self.level = level
        self.goal = goal
        self.parent = parent

    def isSolved(self) -> bool:
        """
        This method checks if the board has reached
        its goal.

        :return : If the goal is reached.
        :rtype: bool
        """
        solved = False
        if self.board == self.goal:
            solved = True
        return solved

    def getChildrenBoards(self) -> list:
        """
        This function gets all the possible child boards which
        can be made from the current board. The possible moves
        are moving the space either up, down, left or right.

        :return : A list of all possible child Boards.
        :rtype: list
        """
        children = []

        x, y = self.find()

        posMoves = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]

        for move in posMoves:
            childBoard = self.makeMoves(self.board, x, y, move[0], move[1])
            if childBoard != None:
                children.append(Board(childBoard, self.level+1, self.goal, self))
        
        return children

    def find(self) -> tuple:
        """
        This function finds where the empty tile
        (represented by a "*" in the data) is in the
        board and returns its x,y coordinates.

        :return : The x and y coordinates.
        :rtype: tuple
        """
        for row in self.board:
            if "*" in row:
                return row.index("*"), self.board.index(row)

    def makeMoves(self, puzzel : list, x : int, y : int, xToSwap : int, yToSwap : int) -> list:
        """
        This function carries out a move, and swaps te values in two coordinates
        where one of those values is the empty tile (*).

        :param puzzel: This is the data in the board.
        :type puzzel: list
        :param x: This is the x co-ordinate of the empty tile.
        :type x: int
        :param y: This is the y co-ordinate of the empty tile.
        :type y: int
        :param xToSwap: This is the x co-ordinate where the empty tile is moving to.
        :type xToSwap: int
        :param yToSwap: This is the y co-ordinate where the empty tile is moving to.
        :type y: int

        :return : The board after the move is made
        :rtype: list
        """
        #Check that the move fits into the board.
        if xToSwap >= 0 and xToSwap <= 2 and yToSwap >= 0 and yToSwap <= 2:
            tempBoard = []
            tempBoard = self.copy(puzzel)
            tempValue = tempBoard[yToSwap][xToSwap]
            tempBoard[yToSwap][xToSwap] = tempBoard[y][x]
            tempBoard[y][x] = tempValue
        else:
            tempBoard = None

        return tempBoard

    def copy(self, puzzel : list) -> list:
        """
        This function copies the data from one list into
        a new list which is returned.#

        :param puzzel: This is the data to be copied.
        :type puzzel: list

        :return : The copy of the list.
        :rtype: list
        """
        copy = []
        for row in puzzel:
            newRow = []
            for item in row:
                newRow.append(item)
            copy.append(newRow)
        return copy

    
    def getParents(self) -> list:
        """
        This function recursively returns all the parent nodes
        which have come before this current one. It is used to get
        all the moves to reach the solved puzzle.
        
        :return : The list of how to solve the board.
        :rtype: list
        """
        if self.parent == None:
            return []
        else:
            return self.parent.getParents() + [self.parent]

    def toString(self) -> str:
        """
        This function returns the board as a formatted string.
        """
        string = "---\n"
        for row in self.board:
            string += "| "
            for num in row:
                string += num + " | "
            string += "\n"
        string += "---"

        return string