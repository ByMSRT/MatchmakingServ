from TicTacToe.Game import Game
from BDD.BDD import BDD
from MatchMaking.Network import *


class Menu:

    def __init__(self):
        pass

    def display_menu(self):
        menu_option = {
            1: "Jouer en local",
            2: "Jouer en réseau",
            3: "Jouer avec l'ordinateur",
            4: "Quitter",
            5: "Info BDD",
            6: "Create all table",
            7: "Connect",
            8: "Insert Player",
            9: "Insert Stat",
            10: "Insert Game Info",
        }

        for key in menu_option.keys():
            print(key, '--', menu_option[key])

    def play_local(self):
        print("Jouer en local")
        IA = input("Voulez-vous jouer contre une IA ? 1 : Oui, 2 : Non")
        if int(IA) == 1:
            print("Go IA")
        else:
            getter.play()

    def play_network(self):
        print("Jouer en réseau")

    def play_with_computer(self):
        print("Jouer avec l'ordinateur")

    def quit(self):
        print("Quitter")
        exit()

    def get_info_db(self):
        # db.create_player_table()
        # db.create_stats_table()
        # db.create_game_info()
        username = input("Quel est votre pseudo ? ")
        print()
        print("Info Player")
        db.select_player()
        print()
        print("Game info")
        db.select_game_info(username)
        print()
        print("Stat info")
        db.select_stats()

    def insert_player(self):
        print("Insert Player")
        username = input("Quel est votre pseudo ? ")
        db.insert_player(username)

    def insert_stat(self):
        print("Insert Stat")
        player_id = input("Quel est votre ID ? ")
        win = input("Combien de partie avez-vous win ? ")
        loose = input("Combien de partie avez-vous loose ? ")
        null = input("Combien avez-vous fait de partie nul ? ")
        db.insert_stats(player_id, win, loose, null)

    def insert_game_info(self):
        print("Insert Game Info")
        player_id = input("Quel est votre ID ? ")
        opponent_id = input("Quelle est l'ID de votre adversaire ? ")
        result = input("Avez-vous gagné ? ")
        db.insert_game_info(player_id, opponent_id, result)

    def create_all_table(self):
        print("Create all table")
        db.create_player_table()
        db.create_stats_table()
        db.create_game_info()

    def connect_client(self):
        connect()

    def get_menu_choice(self):
        while(True):
            self.display_menu()
            option = ''
            try:
                option = int(input("Choisissez une option: "))
            except:
                print("Veuillez entrer un nombre entre 1 et 4")
            if option == 1:
                self.play_local()
                break
            elif option == 2:
                self.play_network()
                break
            elif option == 3:
                self.play_with_computer()
                break
            elif option == 4:
                self.quit()
            elif option == 5:
                self.get_info_db()
                break
            elif option == 6:
                self.create_all_table()
                break
            elif option == 7:
                self.connect_client()
                break
            elif option == 8:
                self.insert_player()
                break
            elif option == 9:
                self.insert_stat()
                break
            elif option == 10:
                self.insert_game_info()
                break


getter = Game('Tic Tac Toe')
db = BDD()
