"""
FitnessFunc.py
=======================
This module is used to define the FitnessFunc class which evaluates the
fitness value of a Suduku grid.
"""

from Grid import Grid

class FitnessFunc:
    """
    This class contains all methods required to determine the
    fitness value of a soduku board.
    """

    def __init__(self) -> None:
        """
        This is the initialiser for a FitnessFunc object
        but does not have any attributes."""
        pass

    def getDuplicates(self, totals : dict) -> int:
        """
        This function gets the number of duplicates, it does this by
        searching through the values of the totals dict and for every
        value greater than 1 it increases.

        :param totals: This is the dict of the number of occurances of each digit.
        :type totals: dict

        :return : The number of duplicates.
        :rtype: int
        """
        numDuplicates = 0
        for value in totals.values():
            if value > 1:
                numDuplicates += value-1
        return numDuplicates

    def evaluate(self, grid : Grid):
        """
        This function evaluates the fitness value of a given grid.

        :param grid: The grid to evaluate a fitness score for.
        :type grid: Grid

        :return : The fitness value of the grid.
        :rtype: int
        """
        numDuplicates = 0

        for row in grid.grid:
            totals = {}
            for item in row:
                if item in totals.keys():
                    totals[item] += 1
                else:
                    totals[item] = 1
            
            numDuplicates += self.getDuplicates(totals)
        
        for column in grid.getColumns():
            totals = {}
            for item in column:
                if item in totals.keys():
                    totals[item] += 1
                else:
                    totals[item] = 1
            numDuplicates += self.getDuplicates(totals)

        for sqr in grid.getSquares():
            totals = {}
            for item in sqr:
                if item in totals.keys():
                    totals[item] += 1
                else:
                    totals[item] = 1
            numDuplicates += self.getDuplicates(totals)
        
        return numDuplicates
