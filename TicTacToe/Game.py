from TicTacToe.Grid import Grid
from random import choice

class Game:

    def __init__(self, name):
        self.name = name

    def choose_pawn(self, player):
        pawn_player = input(f"Joueur {player} quel pion voulez-vous choisir ? Vous avez le choix entre : 1 = X ou 2 = O : ")
        player_pawn = ''
        if int(pawn_player) != 1 and int(pawn_player) != 2:
            print("Vous n'avez pas choisi une valeur correct")
            return
        else:
            if int(pawn_player) == 1:
                print("Votre pion est désormais 'X'")
                player_pawn = 'X'
            else:
                print("Votre pion est désormais 'O'")
                player_pawn = 'O'
        return player_pawn

    def random_player(self):
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
        first_player = choice(players)
        second_player = ''
        if first_player == players[0]:
            second_player = players[1]
        else:
            second_player = players[0]
        print(f"Premier joueur : {first_player}, deuxième joueur : {second_player}")
        array_of_player = [first_player, second_player]
        return array_of_player


        #print(f"C'est {random_player} qui commence la partie !")

    #TODO
    def choose_case(self, line_or_row):
        response = input(f"Dans quelle {line_or_row} voulez-vous placer votre pion ?")
        if len(response) == 0:
            print("Vous n'avez rien rentré veuillez réessayer")
            return
        elif (int(response) <= 0 and int(response) > 3):
            print("Vous n'avez pas choisi une bonne valeur au tour de votre adversaire")
            return
        else:
            return int(response)-1

    def play(self):
        index_of_player = 0
        win_player_1 = False
        win_player_2 = False
        array_of_player = self.random_player()
        player_1_pawn = self.choose_pawn(array_of_player[0])
        player_2_pawn = ''
        if player_1_pawn == 'X':
            player_2_pawn = 'O'
        else:
            player_2_pawn = 'X'
        while win_player_1 == False and win_player_2 == False:
            if index_of_player % 2:
                index_of_player = self.place_pawn(array_of_player[1], player_2_pawn, index_of_player)
                win_player_2 = self.win_or_null(player_2_pawn)
            else:
                index_of_player = self.place_pawn(array_of_player[0], player_1_pawn, index_of_player)
                win_player_1 = self.win_or_null(player_1_pawn)
            if index_of_player == 9 and win_player_1 == False and win_player_2 == False:
                print("Match nul")
                grid.display_grid()
                return
            print(index_of_player)

        if win_player_1:
            print("Fin du match, gagnant player 1")
            grid.display_grid()
        elif win_player_2:
            print("Fin du match, gagnant player 2")
            grid.display_grid()

    def can_place_pawn(self, line, column):
        cant_place_pawn = False
        if (grid.grid[line, column] == '-'):
            cant_place_pawn = True
        return cant_place_pawn

    def place_pawn(self, player_id, player_pawn, index_of_player):
        print()
        print(f"---------------------- Joueur {player_id} à votre tour ------------------------------")
        print()
        grid.display_grid()
        column = self.choose_case('colonne')
        line = self.choose_case('ligne')
        if (self.can_place_pawn(line,column)):
            grid.insert_pawn_in_grid(line, column, player_pawn)
            index_of_player += 1
        else:
            print("Un pion est déjà placé à cette emplacement")
        return index_of_player


    # ---------------------------------- Victory Condition ---------------------------------------------

    def horizontal_victory(self, pawn_sign):
        first_horizontal_win = [grid.grid[0, 0],grid.grid[0, 1],grid.grid[0, 2]]
        second_horizontal_win = [grid.grid[1, 0],grid.grid[1, 1],grid.grid[1, 2]]
        third_horizontal_win = [grid.grid[2, 0],grid.grid[2, 1],grid.grid[2, 2]]
        victory = False
        if first_horizontal_win[0] == pawn_sign and first_horizontal_win[0] == first_horizontal_win[1] and first_horizontal_win[1] == first_horizontal_win[2]:
            print("Victory horizontal ligne 1")
            victory = True
        elif second_horizontal_win[0] == pawn_sign and second_horizontal_win[0] == second_horizontal_win[1] and second_horizontal_win[1] == second_horizontal_win[2]:
            print("Victory horizontal ligne 2")
            victory = True
        elif third_horizontal_win[0] == pawn_sign and third_horizontal_win[0] == third_horizontal_win[1] and third_horizontal_win[1] == third_horizontal_win[2]:
            print("Victory horizontal ligne 3")
            victory = True
        return victory


    def vertical_victory(self, pawn_sign):
        first_vertical_win = [grid.grid[0, 0],grid.grid[1, 0],grid.grid[2, 0]]
        second_vertical_win = [grid.grid[0, 1],grid.grid[1, 1],grid.grid[2, 1]]
        third_vertical_win = [grid.grid[0, 2],grid.grid[1, 2],grid.grid[2, 2]]
        victory = False
        if first_vertical_win[0] == pawn_sign and first_vertical_win[0] == first_vertical_win[1] and first_vertical_win[1] == first_vertical_win[2]:
            print("Victory vertical ligne 1")
            victory = True
        elif second_vertical_win[0] == pawn_sign and second_vertical_win[0] == second_vertical_win[1] and second_vertical_win[1] == second_vertical_win[2]:
            print("Victory vertical ligne 2")
            victory = True
        elif third_vertical_win[0] == pawn_sign and third_vertical_win[0] == third_vertical_win[1] and third_vertical_win[1] == third_vertical_win[2]:
            print("Victory vertical ligne 3")
            victory = True
        return victory

    def diagonal_victory(self, pawn_sign):
        first_diagonal_win = [grid.grid[0, 0], grid.grid[1, 1], grid.grid[2, 2]]
        second_diagonal_win = [grid.grid[0, 2], grid.grid[1, 1], grid.grid[2, 0]]
        victory = False
        if first_diagonal_win[0] == pawn_sign and first_diagonal_win[0] == first_diagonal_win[1] and first_diagonal_win[1] == first_diagonal_win[2]:
            print("Victory diagonal haut gauche -> bas droite")
            victory = True
        elif second_diagonal_win[0] == pawn_sign and second_diagonal_win[0] == second_diagonal_win[1] and second_diagonal_win[1] == second_diagonal_win[2]:
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


grid = Grid()