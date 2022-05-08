from TicTacToe.Grid import Grid
from TicTacToe.Game_condition import Game_condition
from random import choice, randint
from BDD.BDD import BDD


class Game:
    def __init__(self, name):
        self.name = name

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
                        player_name += player_name_input
                        return player_name
                    length_request = len(db.select_player().fetchall())
                    if index == length_request and player_name != names[length_request]:
                        return ''
        else:
            new_name = input(
                "Renseignez votre pseudo pour vous enregistrer : ")
            db.insert_player(new_name)
            new_player_id = db.get_player_info("ID", "Username", new_name)
            db.insert_stats(new_player_id, 0, 0, 0)
            print(f"\n Votre pseudo est donc : {new_name}")
            return new_name

    def random_player(self, ia=None):
        player_1 = ''
        player_2 = ''
        second_player = ''
        while len(player_1) == 0:
            new_name = self.connect_user()
            player_1 += new_name
        if ia != "IA":
            while len(player_2) == 0:
                new_name = self.connect_user()
                player_2 += new_name
            players = [player_1, player_2]
        else:
            players = [player_1, "IA"]
        first_player = choice(players)
        if first_player == players[0]:
            second_player += players[1]
        else:
            second_player += players[0]
        print(
            f"Premier joueur : {first_player}, deuxième joueur : {second_player}")
        array_of_player = [first_player, second_player]
        return array_of_player

    def choose_case(self, line_or_row):
        response_user = input(
            f"Dans quelle {line_or_row} voulez-vous placer votre pion ?")
        final_response = None
        if len(response_user) == 0:
            print("Vous n'avez rien rentré veuillez réessayer")
        elif (int(response_user) <= 0 and int(response_user) > 3):
            print("Vous n'avez pas choisi une bonne valeur au tour de votre adversaire")
        else:
            final_response = int(response_user)-1
        return final_response

    def play(self, ia=None):
        index_of_player = 0
        win_player_1 = False
        win_player_2 = False
        player_1_pawn = ''
        array_of_player = self.random_player(ia)
        if ia != "IA":
            player_1_pawn += self.choose_pawn(array_of_player[0])
        else:
            if array_of_player[0] == "IA":
                player_1_pawn += self.choose_pawn(array_of_player[1])
            else:
                player_1_pawn += self.choose_pawn(array_of_player[0])
        player_2_pawn = ''
        player_1_id = 0
        player_2_id = 0
        player_1_stat = []
        player_2_stat = []
        if player_1_pawn == 'X':
            player_2_pawn += 'O'
        else:
            player_2_pawn += 'X'
        while win_player_1 == False and win_player_2 == False:
            if index_of_player % 2:
                index_of_player = self.place_pawn(
                    array_of_player[1], player_2_pawn, index_of_player)
                win_player_2 = game_condition.win_or_null(player_2_pawn)
            else:
                index_of_player = self.place_pawn(
                    array_of_player[0], player_1_pawn, index_of_player)
                win_player_1 = game_condition.win_or_null(player_1_pawn)
            if index_of_player == 9 and win_player_1 == False and win_player_2 == False:
                print("Match nul")
                grid.display_grid()
                if ia != "IA":
                    self.insert_and_update_db(player_1_id, player_1_stat, player_2_id,
                                              player_2_stat, array_of_player, 0, 1, "Tie", "Tie", "Nul", "Nul")
                return
            print(index_of_player)

        if win_player_1:
            print(f"Fin du match, gagnant {array_of_player[0]}")
            grid.display_grid()
            if ia != "IA":
                self.insert_and_update_db(player_1_id, player_1_stat, player_2_id, player_2_stat,
                                          array_of_player, 0, 1, "Win", "Lose", "Victoire", "Défaite")
            return
        elif win_player_2:
            print(f"Fin du match, gagnant {array_of_player[1]}")
            grid.display_grid()
            if ia != "IA":
                self.insert_and_update_db(player_2_id, player_2_stat, player_1_id, player_1_stat,
                                          array_of_player, 1, 0, "Win", "Lose", "Victoire", "Défaite")
            return

    def can_place_pawn(self, line, column):
        cant_place_pawn = False
        if 0 <= line <= 2 and 0 <= column <= 2:
            if grid.grid[line, column] == '-':
                cant_place_pawn = True
        return cant_place_pawn

    def place_pawn(self, player, player_pawn, index_of_player):
        print()
        print(
            f"---------------------- Joueur {player} à votre tour ------------------------------")
        print()
        grid.display_grid()
        print()
        if player == "IA":
            self.computer_place_pawn(player_pawn)
            index_of_player += 1
        else:
            column = None
            line = None
            while column == None:
                column = self.choose_case('colonne')
            while line == None:
                line = self.choose_case('ligne')
            if (self.can_place_pawn(line, column)):
                grid.insert_pawn_in_grid(line, column, player_pawn)
                index_of_player += 1
            else:
                print("Un pion est déjà placé à cette emplacement")
        return index_of_player

    def computer_place_pawn(self, player_pawn):
        # ------------ IA creation ---------------
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

    def insert_and_update_db(self, winner_id, winner_stat, looser_id, looser_stat, array_of_player, winner_index, looser_index, win, lose, victory, defeat):
        # ---------------- Get player information -------------------------
        winner_id += db.get_player_info("ID",
                                        "Username", array_of_player[winner_index])
        looser_id += db.get_player_info("ID",
                                        "Username", array_of_player[looser_index])
        winner_stat += db.get_stats_of_player(win,
                                              array_of_player[winner_index])
        looser_stat += db.get_stats_of_player(lose,
                                              array_of_player[looser_index])
        # ----------------------- Update stat of player -------------------------
        db.update_stats_info(win, winner_stat[0] + 1, winner_id)
        db.update_stats_info(lose, looser_stat[0] + 1, looser_id)
        db.insert_game_info(winner_id, looser_id, victory)
        db.insert_game_info(looser_id, winner_id, defeat)


db = BDD()
grid = Grid()
game_condition = Game_condition(grid.grid)
