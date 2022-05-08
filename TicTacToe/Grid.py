import numpy as np

class Grid:
    def __init__(self):
        self.column = 3
        self.line = 3
        self.grid = np.array([['-']*self.line]*self.column)

    def display_number(self):
        number = ['1', '2', '3']
        for x in number:
            print(x)

    def display_grid(self):
        index = 0
        grid = ''
        for grid_line in self.grid:
            for grid_column in grid_line:
                index += 1
                if int(index / 3):
                    grid += grid_column + "\n"
                    #print(grid_column)
                    index = 0
                else:
                    grid += grid_column + " | "
                    #print(grid_column + " |", end=' ')
        print(grid)

    def grid_creation(self):
        index = 0
        grid = ''
        for grid_line in self.grid:
            for grid_column in grid_line:
                index += 1
                if int(index / 3):
                    grid += grid_column + "\n"
                    # print(grid_column)
                    index = 0
                else:
                    grid += grid_column + " | "
                    # print(grid_column + " |", end=' ')
        return grid

    def insert_pawn_in_grid(self, line, column, pawn_value):
        self.grid[line, column] = pawn_value
