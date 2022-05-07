from TicTacToe.Grid import Grid
from TicTacToe.Game_condition import Game_condition
from random import choice, randint
from BDD.BDD import BDD

class Game_ia:
    def __init__(self):
        pass
    def choose_pawn(self, player):
        pawn_player = input(
            f"Joueur {player} quel pion voulez-vous choisir ? Vous avez le choix entre : 1 = X ou 2 = O : ")
        player_pawn = ''
        if int(pawn_player) != 1 and int(pawn_player) != 2:
            print("Vous n'avez pas choisi une valeur correct")
            return
        else:
            if int(pawn_player) == 1:
                print("Votre pion est désormais 'X'")
                player_pawn += 'X'
            else:
                print("Votre pion est désormais 'O'")
                player_pawn += 'O'
        return player_pawn

    def connect_user(self):
        register = input("Etes-vous déjà inscrit ? 1 : Oui, 2 : Non ")
        player_name = ''
        if int(register) == 1:
            while len(player_name) == 0:
                player_name_input = input("Quel est votre nom ? ")
                for index, names in enumerate(db.select_player()):
                    if player_name_input == names[1]:
                        print("Correspondance")
                        player_name += player_name_input
                        return player_name
                    else:
                        print("Pas de correspondance")
                    length_request = len(db.select_player().fetchall())
                    if index == length_request and player_name != names[length_request]:
                        return ''
        else:
            new_name = input("Renseignez votre pseudo pour vous enregistrer : ")
            db.insert_player(new_name)
            new_player_id = db.get_player_info("ID", "Username", new_name)
            db.insert_stats(new_player_id, 0, 0, 0)
            print(f"\n Votre pseudo est donc : {new_name}")
            return new_name

    def random_player(self):
        player_1 = ''
        first_player = ''
        second_player = ''
        while len(player_1) == 0:
            new_name = self.connect_user()
            player_1 += new_name
        players = [player_1, "IA"]
        first_player += choice(players)
        if first_player == players[0]:
            second_player += players[1]
        else:
            second_player += players[0]
        print(f"Premier joueur : {first_player}, deuxième joueur : {second_player}")
        array_of_player = [first_player, second_player]
        return array_of_player
        # print(f"C'est {random_player} qui commence la partie !")

    # TODO
    def choose_case(self, line_or_row):
        response = input(f"Dans quelle {line_or_row} voulez-vous placer votre pion ?")
        if len(response) == 0:
            print("Vous n'avez rien rentré veuillez réessayer")
            return
        elif (int(response) <= 0 and int(response) > 3):
            print("Vous n'avez pas choisi une bonne valeur au tour de votre adversaire")
            return
        else:
            return int(response) - 1

    def computer_place_pawn(self, player_pawn):
        test = False
        line = randint(0, 2)
        column = randint(0, 2)
        while test == False:
            if self.can_place_pawn(line, column):
                grid.insert_pawn_in_grid(line, column, player_pawn)
                test = True
            else:
                line = randint(0, 2)
                column = randint(0, 2)

    def play(self):
        index_of_player = 0
        win_player_1 = False
        win_player_2 = False
        array_of_player = self.random_player()
        player_1_pawn = self.choose_pawn(array_of_player[0])
        player_2_pawn = ''
        if player_1_pawn == 'X':
            player_2_pawn += 'O'
        else:
            player_2_pawn += 'X'
        while win_player_1 == False and win_player_2 == False:
            if index_of_player % 2:
                index_of_player = self.place_pawn(array_of_player[1], player_2_pawn, index_of_player)
                win_player_2 = game_condition.win_or_null(player_2_pawn)
            else:
                index_of_player = self.place_pawn(array_of_player[0], player_1_pawn, index_of_player)
                win_player_1 = game_condition.win_or_null(player_1_pawn)
            if index_of_player == 9 and win_player_1 == False and win_player_2 == False:
                print("Match nul")
                grid.display_grid()
                return
            print(index_of_player)

        if win_player_1:
            print("Fin du match, gagnant player 1")
            grid.display_grid()
            return
        elif win_player_2:
            print("Fin du match, gagnant player 2")
            grid.display_grid()
            return

    def can_place_pawn(self, line, column):
        cant_place_pawn = False
        if (grid.grid[line, column] == '-'):
            cant_place_pawn = True
        return cant_place_pawn

    def place_pawn(self, player, player_pawn, index_of_player):
        print()
        print(f"---------------------- Joueur {player} à votre tour ------------------------------")
        print()

        if player == "IA":
            self.computer_place_pawn(player_pawn)
            index_of_player += 1
        else:
            column = self.choose_case('colonne')
            line = self.choose_case('ligne')
            if (self.can_place_pawn(line, column)):
                grid.insert_pawn_in_grid(line, column, player_pawn)
                index_of_player += 1
            else:
                print("Un pion est déjà placé à cette emplacement")
        grid.display_grid()
        return index_of_player


db = BDD()
grid = Grid()
game_condition = Game_condition(grid.grid)