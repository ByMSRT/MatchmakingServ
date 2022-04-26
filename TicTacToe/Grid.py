import numpy as np
import math
from TicTacToe.Pions import Pions

class Grid:
    def __init__(self):
        self.column = 3
        self.line = 3
        #self.grid = 5
        self.grid = np.array([['-']*self.line]*self.column)


    def display_grid(self):
        index = 0
        for grid_line in self.grid:
            for grid_column in grid_line:
                index += 1
                if int(index / 3):
                    print(grid_column)
                    index = 0
                else:
                    print(grid_column + " |", end=' ')


    def print_one_element(self):
        #print(math.pi)
        #print(str(self.grid[1, 0]))
        self.grid[newPion.column-1, newPion.line-1] = 'O'
        self.grid[1, 2] = 'X'
        print("Le symbole est " + self.grid[1,2])

newPion = Pions(2, 1, '1')