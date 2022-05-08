from TicTacToe.Game import Game
from BDD.BDD import BDD
from MatchMaking.Network import *
from TicTacToe.Grid import Grid


class Menu:

    def __init__(self):
        pass

    def display_menu(self):
        menu_option = {
            1: "Jouer en local",
            2: "Jouer en réseau",
            3: "Jouer avec l'ordinateur",
            4: "Info BDD",
            5: "Quitter",
        }

        for key in menu_option.keys():
            print(key, '--', menu_option[key])

    def play_local(self):
        print("Jouer en local")
        getter.play()

    def play_network(self):
        connect()

    def play_with_computer(self):
        print("Jouer avec l'ordinateur")
        getter.play("IA")

    def quit(self):
        print("Quitter")
        exit()

    def get_info_db(self):
        username = input("Quel est votre pseudo ? ")
        print()
        print("Info Player \n")
        print("Username = ", username)
        print()
        print("Game info")
        db.select_game_info(username)
        print()
        print("Stat info")
        db.select_stats()

    def get_menu_choice(self):
        while(True):
            self.display_menu()
            option = ''
            try:
                option = int(input("Choisissez une option: "))
            except:
                print("Veuillez entrer un nombre entre 1 et 5")
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
                self.get_info_db()
                break
            elif option == 5:
                self.quit()


grid = Grid()
getter = Game('Tic Tac Toe')
db = BDD()
