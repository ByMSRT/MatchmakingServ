from TicTacToe.Game import Game
class Menu: 

    def __init__(self):
        pass

    getter = Game('Tic Tac Toe')

    def display_menu(self):
        menu_option = {
            1: "Jouer en local",
            2: "Jouer en réseau",
            3: "Jouer avec l'ordinateur",
            4: "Quitter"
        }

        for key in menu_option.keys():
            print(key, '--', menu_option[key])

    def play_local(self):
        print("Jouer en local")
        self.getter.play()

    def play_network(self):
        print("Jouer en réseau")
    
    def play_with_computer(self):
        print("Jouer avec l'ordinateur")
    
    def quit(self):
        print("Quitter")
        exit()

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
            
