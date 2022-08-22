"""
UserInterface.py
==================
This module contains the UserInterface class which defines all methods
which relate to interactions with the user.
"""

from Grid import Grid

class UserInterface:
    """
    This class defines the UserInterface object which handles all
    interactions with the user.
    """

    def __init__(self) -> None:
        """
        This is the initialiser for the UserInterface Object.
        """
        pass

    def getFileLoc(self):
        """
        This function gets the file path to the grid file.
        
        :return : The file path
        :rtype: str
        """
        return input("Enter path to grid file: ")

    def outputParameters(self, POPULATION : int, MUTATION_RATE : float, SELECTION_RATE : float, RESTART_THRESHOLD : int, MAX_RESTARTS : int):
        """
        This function is used to diplay the parameters for the Evolutionary Algorithm to the user.

        :param POPULATION: The size of the population.
        :type POPULATION: int
        :param MUTATION_RATE: The probability of mutation.
        :type MUTATION_RATE: float
        :param SELECTION_RATE: The percentage of the top of the population to be used as
        parents for the new population.
        :type SELECTION_RATE: float
        :param RESTART_THRESHOLD: The max number of generations before a restart is forced.
        :type RESTART_THRESHOLD: int
        :param MAX_RESTARTS: The maximum number of restarts allowed by the GA.
        :type MAX_RESTARTS: int
        """
        print(" --- Parameters for the Evolutionary Algorithm --- ")
        print("Population Size: ", POPULATION)
        print("Mutation Rate: ", MUTATION_RATE)
        print("Selection Rate: ", SELECTION_RATE)
        print("Restart Threshold: ", RESTART_THRESHOLD)
        print("Max Restarts: ", MAX_RESTARTS)

    def outputGrid(self, grid : Grid, gridDesc : str):
        """
        This function outputs a grid with a label including its given descrition in the form:

            ' --- [gridDesc] Grid ---'
        
        :param grid: The grid to be displayed.
        :type grid: Grid
        :param gridDesc: The description of the grid.
        :type gridDesc: str
        """
        print(f" --- {gridDesc} Grid --- ")
        print(grid.toString())
        print("The Grid's Fitness Value was: ", grid.fitnessVal)

    def outputGenerationDetails(self, restartNum : int, genNum : int, bestFitness : int, worstFitness : int):
        """
        This function is used to output the current generation with its best and worst fitness values.
        
        :param restartNum: The restart currently on.
        :type restartNum: int
        :param genNum: The generation currently on.
        :type genNum: int
        :param bestFitness: The best fitness value in the current generation's population.
        :type bestFitness: int
        :param worstFitness: The worst fitness value in the current generation's population.
        :type worstFitness: int"""
        print(f"Restart {restartNum} - Generation {genNum}: best fitness value = {bestFitness} | worst fitness value = {worstFitness}")

    def error(self, errorMsg : str):
        """
        This function alerts the user there has been an arror in the EA.
        """
        raise Exception(errorMsg)

    def outputSolved(self):
        """
        A function to alert the user the initial grid has been solved.
        """
        print("The EA was Successful, the board has been solved.")
    
    def outputNotSolved(self):
        """
        A function to alert the user the initial grid could not be solved with given parameters..
        """
        print("The EA was Unsuccessful, the board has been not solved.\nThe resulting grid is the closest the EA came to solving.")