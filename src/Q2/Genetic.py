"""
Genetic.py
=========================
This module contains the GeneticAlg function which is is used 
to carry out the evolutional algorithm to solve the solution.
"""

import random

from Grid import Grid
from FitnessFunc import FitnessFunc
from UserInterface import UserInterface

class GeneticAlg:
    """
    This class contains all the attricutes and methods required to solve a
    soduku problem using an evolutionary algorithm.
    """

    """
    The percentage of top candiates to take forward from the population.
    """
    selectionRate = None

    """
    The Fitness function Class to be used.
    """
    fitnessFunc = None

    """
    The probability of a child mutating.
    """
    mutationProb = None

    """
    The initial starting grid which is used to create the first
    (any restart) population.
    """
    initialGrid = None

    """
    The number of generations to allow before forcing a restart.
    """
    restartThreshold = None

    """
    The maximum number of restarts allowed
    """
    maxRestarts = None

    """
    The current best end state.
    """
    bestState = None

    """
    The current generation the GA is on. 
    """
    generation = 0

    """
    The number of restarts.
    """
    restarts = 0

    def __init__(self, selectionRate : int, mutationProb : int, restartThreshold : int, maxRestarts : int, fitnessFunc : FitnessFunc, initialGrid : Grid) -> None:
        """
        This is the initialiser for a GeneticAlg and asigns all of the
        attributes given as paraers to their values in the object.

        :param selectionRate: This is the percentage of grids with the top fitness value 
        which should be selected.
        :type selectionRate: float
        :param mutationRate: This is the probablity of a child mutating.
        :type selectionRate: float
        :param restartThreshold: This is the number of generations allowed before a restart
        is forced.
        :type selectionRate: float
        :param maxRestarts: The maximum number of restarts allowed.
        :type maxRestarts: int
        :param fitnessFunc: This is the FitnessFunc object which defines the fitness function to be used
        to rank the population.
        :type fitnessFunc: FitnessFunc
        :param initialGrid: This is the starting Grid.
        :type initialGrid: Grid
        """
        self.selectionRate = selectionRate
        self.mutationProb = mutationProb
        self.maxRestarts = maxRestarts
        self.fitnessFunc = fitnessFunc
        self.initialGrid = initialGrid
        self.restartThreshold = restartThreshold

    def getPopulation(self, numPopulation : int) -> list[Grid]:
        """
        This functions returns a population, which is a list of randomly filled version of the
        initial board where any 0 is replaced by a digit from 1 to 9.

        :param numPopulation: The size of the population.
        :type numPopulation: int

        :return : The population (list of possible solutions)
        :rtype: list
        """
        
        population = []

        for i in range(numPopulation):
            newGrid = []
            for row in self.initialGrid.grid:
                allDigits = [num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9] if num not in row]
                newRow = []
                for item in row:
                    if item == 0:
                        newItem = random.choice(allDigits)
                        newRow.append(newItem)
                        allDigits.remove(newItem)
                    else:
                        newRow.append(item)
                newGrid.append(newRow)

            newGridObj = Grid(newGrid)
            newGridObj.fitnessVal = self.fitnessFunc.evaluate(newGridObj)
            population.append(newGridObj)
        return population
    
    def getTotalFitness(self, population : list[Grid]) -> int:
        """
        This method is used to sum all the fitness values of all the possible
        solutions in the population.

        :param population: The population of possible solutions.
        :type population: list

        :return : The sum of all the itness values of the boards in population.
        :rtype: int
        """
        total = 0
        for item in population:
            total += item.fitnessVal
        return total

    def select(self, population : list[Grid]) -> Grid:
        """
        This function returns a possible solution from the population where the 
        probability of a solution being picked is inversely proportional to the 
        fitnes value. This means the smaller the fitness value, the more likely
        it is to be selected however it is possible to select any board in the 
        population.

        :param population: This is the list of possible solutions.
        :type population: list

        :return : The selected Grid which will be used as a parent.
        :rtype: Grid
        """
        probability = 1/self.getTotalFitness(population)
        weights = []
        for state in population:
            weights.append(state.fitnessVal*probability)
        selected = random.choices(population, weights, k=1)[0]
        return selected
        
    def reproduce(self, x : Grid, y : Grid) -> tuple[Grid, Grid]:
        """
        This function is used to create two children grids from two parent
        grids using a random crossover point and a crossover opperator. This
        works by selecteing a random index and taking the start of one parent's gene 
        (row) up that that random index and combining with the remaining index's of the
        other parent's gene (row) for every row in the board. This happens vice versa to
        also produce the second child.

        :param x: The X parent to produce the children.
        :type x: Grid
        :param y: The Y parent to produce the children.
        :type y: Grid

        :return : Two Child Grids producd from the parent grids
        :rtype: tuple
        """
        n = len(x.grid)
        child1 = []
        child2 = []
        for i in range(len(x.grid)):
            c = random.randint(0, n-1)
            child1Row = x.grid[i][: c] + y.grid[i][c: ]
            child2Row = y.grid[i][: c] + x.grid[i][c: ]
            # Check none of the initial values have been changed.
            for j in range(len(child1Row)):
                if child1Row[j] != self.initialGrid.grid[i][j] and self.initialGrid.grid[i][j] != 0:
                    child1Row[j] = self.initialGrid.grid[i][j]
                if child2Row[j] != self.initialGrid.grid[i][j] and self.initialGrid.grid[i][j] != 0:
                    child2Row[j] = self.initialGrid.grid[i][j]
            child1.append(child1Row)
            child2.append(child2Row)
        
        child1Obj = Grid(child1)
        child1Obj.fitnessVal = self.fitnessFunc.evaluate(child1Obj)
        child2Obj = Grid(child2)
        child2Obj.fitnessVal = self.fitnessFunc.evaluate(child2Obj)
        return child1Obj, child2Obj

    def getIndexToSwap(self, childSquare : Grid) -> list[int]:
        """
        This function is used to get the two index's of the items in a child
        which are to be swapped when a mutation occurs.

        :param childSquare: The square the mutation is happening on.
        :type childSquare: Grid

        :return : A list of lenth 2 with the two indexs' to be swapped.
        :rtype: list        
        """
        swapItemsIndex = []
        invalidIndex = []

        for num in childSquare:
            if num != 0:
                invalidIndex.append(childSquare.index(num))

        posIndex = [num for num in [0,1,2,3,4,5,6,7,8] if num not in invalidIndex]
        
        #If all the row is predetermined
        if len(posIndex) == 0:
            return None
        else:
            for i in range(2):
                swapItemIndex = random.choice(posIndex)
                swapItemsIndex.append(swapItemIndex)
            return swapItemsIndex

    def mutate(self, child : Grid) -> None:
        """
        This function carries out mutations on a child on a random number of 
        subgrids, a mutation is where two elements in a 3x3 subgrid are swapped.
        Initial values cannot be affected by a mutation, only numbers in the gene.

        :param child: The grid being mutated.
        :type child: Grid

        :return : There is nothing returned as the child calling the method is modified.
        :rtype: None
        """
        squares = child.getSquares()

        numMutations = random.randint(0, len(squares)-1)
        
        for i in range(numMutations):
            sqrId = random.randint(0, len(squares)-1)

            swapIndex = self.getIndexToSwap(squares[sqrId])

            if swapIndex != None:
                temp = squares[sqrId][swapIndex[0]]
                child.updateSquare(squares.index(squares[sqrId]), swapIndex[0], squares[sqrId][swapIndex[1]])
                child.updateSquare(squares.index(squares[sqrId]), swapIndex[1], temp)

    def solve(self, population : list[Grid], ui : UserInterface) -> Grid:
        """
        This function uses the given population of possible solutions to produce a solution 
        to the soduku board. 

        If the population contains a solution with a fitness value of 0 then this solution solves
        the board hence is returned. Else a new population is made using the given population which
        is then recursivley used on this function. This new population is made by selecting the top
        percentage (defined by selectionRate) then creating children and possibly (probability defined
        by mutationRate) mutating them  which populate the new population.

        :param population: This is the population of solutions which contains the solution or will be
        used to make the new population.
        :type population: list
        :param ui: This is the user interface object being used and defines all the methods which involve
        interactions with the user. (Must have a outputGenerationDetails method).
        :type ui: UserInterface

        :return : The solution to the sodoku board.
        :rtype: Grid
        """

        if self.generation > self.restartThreshold:

            if self.restarts >= self.maxRestarts:
                ui.outputNotSolved()
                return self.bestState

            self.generation = 0
            self.restarts += 1
            restartPop = self.getPopulation(len(population))
            return self.solve(restartPop, ui)

        population.sort(key=lambda grid:grid.fitnessVal, reverse=False)

        ui.outputGenerationDetails(self.restarts, self.generation, population[0].fitnessVal, population[len(population)-1].fitnessVal)

        if population[0].fitnessVal == 0:
            ui.outputSolved()
            return population[0]
        
        if self.bestState == None:
            self.bestState = population[0]
        elif population[0].fitnessVal < self.bestState.fitnessVal:
            self.bestState = population[0]

        populationSize = len(population)

        newPopulation = []

        population = population[: int(len(population) * self.selectionRate)]

        if len(population) <= 1:
            ui.error("Selection Rate too small for given population size. (Must produce at least 2 children).")

        for i in range(int(populationSize/2)):
            x = self.select(population)

            y = self.select([grid for grid in population if grid != x])
            
            child1, child2 = self.reproduce(x, y)

            if (random.randint(0, 100)/100) < self.mutationProb:
                self.mutate(child1)
                self.mutate(child2)
            
            newPopulation.append(child1)
            newPopulation.append(child2)
        
        self.generation += 1

        solution = self.solve(newPopulation, ui)

        return solution
