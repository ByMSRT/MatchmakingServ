from TicTacToe.Grid import Grid
from random import choice

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

    def random_player():
        player_1 = ""
        player_2 = ""
        while player_1 == "":
                player_1 = input("Joueur 1 quel est votre nom ? ")
                if player_1 == "":
                    print("Veuillez rentrer un nom")
                else:
                        print("Vous avez choisi : " + player_1)
        while player_2 == "":
                player_2 = input("Joueur 2 quel est votre nom ? ")
                if player_2 == "":
                        print("Veuillez rentrer un nom")
                else:
                        print("Vous avez choisi : " + player_2)
        players = [player_1, player_2]
        random_player = choice(players)
        print(f"C'est {random_player} qui commence la partie !")

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
            self.horizontal_victory('X')
            if(index_of_player%2):
                self.place_pawn('1', 'O', column, line)
                index_of_player += 1
            else:
                self.place_pawn('2', 'X', column, line)
                index_of_player += 1

    def place_pawn(self, player_id, player_pawn, column, line):
        print()
        print(f"---------------------- Joueur {player_id} à votre tour ------------------------------")
        print()
        grid.display_grid()
        column += self.choose_case('colonne')
        line += self.choose_case('ligne')
        grid.insert_pawn_in_grid(line, column, player_pawn)

    def victory_condition(self, pawn_player):
        index = 0
        for grid_line in grid.grid:
            for case in grid_line:
                index += 1
                if (case == pawn_player and case+1 == pawn_player and case+2 == pawn_player):
                    print("Win")
    def horizontal_victory(self, pawn_sign):
        count_pawn = 1
        line = 0
        for x in range(2):
            if(grid.grid[line, x] ==  pawn_sign and grid.grid[line, x+1] == pawn_sign):
                count_pawn += 1
            if(count_pawn < 3 and x+1 == 2 and line < 2):
                count_pawn = 0
                line += 1
            if (count_pawn == 3):
                print(count_pawn)
                return False
            else:
                print(count_pawn)
                return True





grid = Grid()