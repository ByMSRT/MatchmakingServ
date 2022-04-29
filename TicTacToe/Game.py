from TicTacToe.Grid import Grid

class Game:

    def __init__(self, name):
        self.name = name

    def choose_pawn(self):
        pawn_player_1 = input("Joueur 1 quel pion voulez-vous choisir ? Vous avez le choix entre : 1 = X ou 2 = O")
        if(pawn_player_1 != 1 and pawn_player_1 != 2):
            print("Vous n'avez pas choisi une valeur correct")
            return
        else:
            if(pawn_player_1 == 1):
                print("Votre pion est désormais 'X'")
            else:
                print("Votre pion est désormais 'O'")

    #TODO
    def choose_case(self, line_or_row):
        response = input(f"Dans quelle {line_or_row} voulez-vous placer votre pion ?")
        if (int(response) <= 0 and int(response) > 3):
            print("Vous n'avez pas choisi une bonne valeur au tour de votre adversaire")
            return
        else:
            return int(response)-1

    def play(self):
        not_finish = True
        index_of_player = 1
        column = 0
        line = 0

        while not_finish:

            if(index_of_player%2):
                self.place_pawn('1', 'O', column, line)
                self.horizontal_victory('O')
                index_of_player += 1
            else:
                self.place_pawn('2', 'X', column, line)
                self.horizontal_victory('X')
                index_of_player += 1

    def place_pawn(self, player_id, player_pawn, column, line):
        print()
        print(f"---------------------- Joueur {player_id} à votre tour ------------------------------")
        print()
        grid.display_grid()
        column += self.choose_case('colonne')
        line += self.choose_case('ligne')
        if (grid.grid[line, column] == '-'):
            grid.insert_pawn_in_grid(line, column, player_pawn)
        else:
            print("Déjà placé")

    def victory_condition(self, pawn_player):
        index = 0
        for grid_line in grid.grid:
            for case in grid_line:
                index += 1
                if (case == pawn_player and case+1 == pawn_player and case+2 == pawn_player):
                    print("Win")
    def horizontal_victory(self, pawn_sign):
        first_horizontal_win = [grid.grid[0, 0],grid.grid[0, 1],grid.grid[0, 2]]
        second_horizontal_win = [grid.grid[1, 0],grid.grid[1, 1],grid.grid[1, 2]]
        third_horizontal_win = [grid.grid[2, 0],grid.grid[2, 1],grid.grid[2, 2]]

        if first_horizontal_win[0] == pawn_sign and first_horizontal_win[0] == first_horizontal_win[1] and first_horizontal_win[1] == first_horizontal_win[2]:
            print("Victory")
        elif second_horizontal_win[0] == pawn_sign and second_horizontal_win[0] == second_horizontal_win[1] and second_horizontal_win[1] == second_horizontal_win[2]:
            print("Victory")
        elif third_horizontal_win[0] == pawn_sign and third_horizontal_win[0] == third_horizontal_win[1] and third_horizontal_win[1] == third_horizontal_win[2]:
            print("Victory")
        else:
            print("No victory")


    def vertical_victory(self, pawn_sign):
        first_vertical_win = [grid.grid[0, 0],grid.grid[1, 0],grid.grid[2, 0]]
        second_vertical_win = [grid.grid[1, 1],grid.grid[1, 1],grid.grid[2, 1]]
        third_vertical_win = [grid.grid[2, 2],grid.grid[2, 2],grid.grid[2, 2]]


        if first_vertical_win[0] == pawn_sign and first_vertical_win[0] == first_vertical_win[1] and first_vertical_win[1] == first_vertical_win[2]:
            print("Victory")
        elif second_vertical_win[0] == pawn_sign and second_vertical_win[0] == second_vertical_win[1] and second_vertical_win[1] == second_vertical_win[2]:
            print("Victory")
        elif third_vertical_win[0] == pawn_sign and third_vertical_win[0] == third_vertical_win[1] and third_vertical_win[1] == third_vertical_win[2]:
            print("Victory")
        else:
            print("No victory")






grid = Grid()