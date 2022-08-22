"""
Grid.py
==================
This module contains the Grid class which defines what a grid (Sodoku Board)
should look like and all methods related to handling a Grid object.
"""

class Grid:
    """
    This class defined a Grid which represents a Sodoku Board
    and all methods used to handle and manipulate a Grid obejct.
    """

    """
    This data for a Grid. It is in the form of a 2D array with nine
    subarrays representing rows in the grid.
    """
    grid = []

    """
    The fitness value of the grid, calculated used a Fitness
    Function.
    """
    fitnessVal = None

    def __init__(self, grid : list) -> None:
        """
        This is the initialiser for a Grid object, it asigns the given grid data
        to the grid attribute of the object.
        
        :param grid: The list of data which specifies the data in the board.
        :type grid: list
        """
        self.grid = grid

    @classmethod
    def fromFileName(cls, gridFile : str):
        """
        This classmethod is used to initiaise a grid from a given file, reading in
        the data from the file where the file is in the form with x being initial
        values or a '.' for unknown values: 
        
            xxx!xxx!xxx
            xxx!xxx!xxx
            xxx!xxx!xxx
            ---!---!---
            xxx!xxx!xxx
            xxx!xxx!xxx
            xxx!xxx!xxx
            ---!---!---
            xxx!xxx!xxx
            xxx!xxx!xxx
            xxx!xxx!xxx

        :param gridFile: The filename / path to file holding the grid data.
        :type gridFile: str

        :return : A grid object containing the grid specified in the file.
        :rtype: Grid
"""
        grid = []
        with open(gridFile, "r") as f:
            for line in f.readlines():
                row = []
                for char in line.strip():
                    if (char != "!") and (char != "-"):
                        if char == ".":
                            row.append(0)
                        else:
                            row.append(int(char))
                if row != []:
                    grid.append(row)
        return cls(grid)

    def fillPredetermined(self):
        """
        This function is used to fill in any predeterminable values in the
        grid when it is first initialised before the Evolutional Algorithm
        starts. This helps to give the best possible initial state.

        It does this by for every cell in the grid, removing the digits in its
        row, column and square from the avaliable digits (1 to 9) and therefore
        after this has finnished if only one digit is avaliable, that digit has to
        belong in the cell. This loops until no changes are made and hence all cells
        which have the ability to be predetermined have been calculated and asigned.
        """

        numChanges = 1

        while numChanges != 0:
            numChanges = 0
            for row in self.grid:
                for numIndex in range(len(row)):
                    avaliableDigits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    # remove all digits in row
                    for digit in row:
                        if digit != 0:
                            avaliableDigits.remove(digit)
                    # remove all digits in column
                    for digit in self.getColumns()[numIndex]:
                        if digit != 0 and digit in avaliableDigits:
                            avaliableDigits.remove(digit)
                    # remove all digits in square
                    for digit in self.getSquares()[self.getSquareDigitIn(self.grid.index(row), numIndex)]:
                        if digit != 0 and digit in avaliableDigits:
                            avaliableDigits.remove(digit)

                    if len(avaliableDigits) == 1 and row[numIndex] == 0:
                        row[numIndex] = avaliableDigits[0]
                        numChanges += 1

    def getSquareDigitIn(self, digitRIndex : int, digitCIndex : int) -> int:
        """
        This function is used to return the index of a subgrid in getSquares of a specific
        cell which is specifed by its row index (digitRIndex) and column index (digitCIndex).

        :param digitRIndex: The row index of the cell.
        :type digitRIndex: int
        :param digitCIndex: The column index of the cell.
        :type digitCIndex: int

        :return : The index of the square the cell is in.
        :rtype: int
        """
        squareNum = 0
        for y in range(3):
            for x in range(3):
                for squareRow in range(y*3, (y+1)*3, 1):
                    for i in range(x*3, (x+1)*3, 1):
                        if i == digitCIndex and squareRow == digitRIndex:
                            squareIndex = squareNum
                squareNum += 1
        return squareIndex

    def updateSquare(self, squareID : int, posID : int, value : int):
        """
        This function is used to update a cell in the grid where the cell is 
        taken from a specific square from the getSquares method.
        
        :param squareID: The index of the square the value is in.
        :type squareID: int
        :param posID: The index of the value the square is in.
        :type posID: int
        :param value: The value itself.
        :type value: int
        """
        for y in range(3):
            for x in range(3):
                if (x+y) == squareID:
                    for squareRow in range(y*3, (y+1)*3, 1):
                        for i in range(x*3, (x+1)*3, 1):
                            if (squareRow + i) == posID:
                                self.grid[squareRow][i] = value
                       
    def getColumns(self) -> list[int]:
        """
        This function returns a list of all the columns.

        :return : A list of all columns.
        :rtype: list
        """
        columns = []
        for num in range(len(self.grid)):
            column = []
            for row in self.grid:
                column.append(row[num])
            columns.append(column)
        return columns

    def getSquares(self) -> list[int]:
        """
        This function returns a list of all the subgrids (squares).

        :return : A list of all squares.
        :rtype: list
        """
        squares = []
        for y in range(3):
            for x in range(3):
                square = []
                for squareRow in range(y*3, (y+1)*3, 1):
                    for i in range(x*3, (x+1)*3, 1):
                        square.append(self.grid[squareRow][i])
                squares.append(square)
        return squares

    def toString(self) -> str:
        """
        This function returns a grid as a formatted string.

        :return : A formatted version of the grid attribute.
        :rtype: str
        """
        string = f""
        for j in range(len(self.grid)):
            if j % 3 == 0 and j != 0:
                string +=  " | - - - | - - - | - - -\n"
            for i in range(len(self.grid[j])):
                if i % 3 == 0:
                    string += f" | {self.grid[j][i]}"
                else:
                    string += f" {self.grid[j][i]}"
            string += "\n"
        return string
