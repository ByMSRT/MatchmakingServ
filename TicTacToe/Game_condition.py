class Game_condition:
    def __init__(self, grid):
        self.grid = grid

        # ---------------------------------- Victory Condition ---------------------------------------------

    def horizontal_victory(self, pawn_sign):
        first_horizontal_win = [self.grid[0, 0], self.grid[0, 1], self.grid[0, 2]]
        second_horizontal_win = [self.grid[1, 0], self.grid[1, 1], self.grid[1, 2]]
        third_horizontal_win = [self.grid[2, 0], self.grid[2, 1], self.grid[2, 2]]
        victory = False
        if first_horizontal_win[0] == pawn_sign and first_horizontal_win[0] == first_horizontal_win[1] and \
                first_horizontal_win[1] == first_horizontal_win[2]:
            print("Victory horizontal ligne 1")
            victory = True
        elif second_horizontal_win[0] == pawn_sign and second_horizontal_win[0] == second_horizontal_win[1] and \
                second_horizontal_win[1] == second_horizontal_win[2]:
            print("Victory horizontal ligne 2")
            victory = True
        elif third_horizontal_win[0] == pawn_sign and third_horizontal_win[0] == third_horizontal_win[1] and \
                third_horizontal_win[1] == third_horizontal_win[2]:
            print("Victory horizontal ligne 3")
            victory = True
        return victory

    def vertical_victory(self, pawn_sign):
        first_vertical_win = [self.grid[0, 0], self.grid[1, 0], self.grid[2, 0]]
        second_vertical_win = [self.grid[0, 1], self.grid[1, 1], self.grid[2, 1]]
        third_vertical_win = [self.grid[0, 2], self.grid[1, 2], self.grid[2, 2]]
        victory = False
        if first_vertical_win[0] == pawn_sign and first_vertical_win[0] == first_vertical_win[1] and \
                first_vertical_win[1] == first_vertical_win[2]:
            print("Victory vertical ligne 1")
            victory = True
        elif second_vertical_win[0] == pawn_sign and second_vertical_win[0] == second_vertical_win[1] and \
                second_vertical_win[1] == second_vertical_win[2]:
            print("Victory vertical ligne 2")
            victory = True
        elif third_vertical_win[0] == pawn_sign and third_vertical_win[0] == third_vertical_win[1] and \
                third_vertical_win[1] == third_vertical_win[2]:
            print("Victory vertical ligne 3")
            victory = True
        return victory

    def diagonal_victory(self, pawn_sign):
        first_diagonal_win = [self.grid[0, 0], self.grid[1, 1], self.grid[2, 2]]
        second_diagonal_win = [self.grid[0, 2], self.grid[1, 1], self.grid[2, 0]]
        victory = False
        if first_diagonal_win[0] == pawn_sign and first_diagonal_win[0] == first_diagonal_win[1] and \
                first_diagonal_win[1] == first_diagonal_win[2]:
            print("Victory diagonal haut gauche -> bas droite")
            victory = True
        elif second_diagonal_win[0] == pawn_sign and second_diagonal_win[0] == second_diagonal_win[1] and \
                second_diagonal_win[1] == second_diagonal_win[2]:
            print("Victory diagonal bas gauche -> haut droite")
            victory = True
        return victory

    def win_or_null(self, pawn_sign):
        victory = False
        if self.horizontal_victory(pawn_sign):
            victory = True
        elif self.vertical_victory(pawn_sign):
            victory = True
        elif self.diagonal_victory(pawn_sign):
            victory = True
        return victory