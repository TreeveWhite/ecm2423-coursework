"""
UserInterface.py
====================
This module contains the methods for any interactions with the User.
"""

class UserInterface:

    def __init__(self) -> None:
        """
        This initialised the UserInterface"""
        pass 
    
    def getHeuristicMethod(self):
        """"
        This functions gets the identifier of the heuristic function the user
        wants to use during the algorithm.

        :return : The identifier of chosen heuristic.
        :rtype: str
        """
        return input("Would you like to use Manhattan Distance (MD) or Misplaced Tiles (MT) :")

    def printSolution(self, solution : list, goal : list):
        """
        This function prints out the solution in a formated and easy
        to follow way. This allows the user to easily follow the steps
        being taken.
        """

        print("Solution to given Initial and Goal States")

        print("Moves to reach Goal: ", len(solution))

        for move in solution:
            print(move.toString())

            print(" | ")
            print(" | ")
            print(" | ")
            print(" V \n")

        print("---")
        for row in goal:
            print("|", end=" ")
            for num in row:
                print(num, "|", end=" ")
            print("")
        print("---")
    
