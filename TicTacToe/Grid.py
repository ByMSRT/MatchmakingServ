import numpy as np


class Grid:
    def __init__(self):
        self.column = 3
        self.line = 3
        self.grid = np.array([['-']*self.line]*self.column)

    def display_grid(self):
        index = 0
        grid = ''
        for grid_line in self.grid:
            for grid_column in grid_line:
                index += 1
                if int(index / 3):
                    print(grid_column)
                    index = 0
                else:
                    print(grid_column + " |", end=' ')

    def grid_creation(self):
        # Useful function for matchmaking
        index = 0
        grid = ''
        for grid_line in self.grid:
            for grid_column in grid_line:
                index += 1
                if int(index / 3):
                    grid += grid_column + "\n"
                    index = 0
                else:
                    grid += grid_column + " | "
        return grid

    def insert_pawn_in_grid(self, line, column, pawn_value):
        self.grid[line, column] = pawn_value
