class Grid:
    def __init__(self):
        self.column = 3
        self.line = 3
        self.grid = [['-']*self.line]*self.column

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

