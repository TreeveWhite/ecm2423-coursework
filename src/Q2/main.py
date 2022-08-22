"""
main.py
=========================
This is the main file for solving a Soduku using a Evolutionary Algorithm.
"""
from Grid import Grid
from Genetic import GeneticAlg
from FitnessFunc import FitnessFunc
from UserInterface import UserInterface

if __name__ == "__main__":

    # define the constants.
    POPULATION = 1000
    MUTATION_RATE = 0.025
    SELECTION_RATE = 0.2
    RESTART_THRESHOLD = 50
    MAX_RESTARTS = 5

    ui = UserInterface()

    # display constants.
    ui.outputParameters(POPULATION, MUTATION_RATE, SELECTION_RATE, RESTART_THRESHOLD, MAX_RESTARTS)

    # define initial board.
    suduko = Grid.fromFileName(ui.getFileLoc())

    ui.outputGrid(suduko, "Initial (No Changes)")

    suduko.fillPredetermined()

    ui.outputGrid(suduko, "Initial (With Predetermined Values)")

    fitnessFunc = FitnessFunc()

    genetic = GeneticAlg(SELECTION_RATE, MUTATION_RATE, RESTART_THRESHOLD, MAX_RESTARTS, fitnessFunc, suduko)

    population = genetic.getPopulation(POPULATION)

    result = genetic.solve(population, ui)

    ui.outputGrid(result, "Resulting")
