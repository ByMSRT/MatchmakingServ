from BDD.BDD import BDD
from Menu.Menu import Menu
from TicTacToe.Grid import Grid
from TicTacToe.Game import Game


def main():
    menu = Menu()
    menu.get_menu_choice()
    db.close_connexion()

    
getter = Game('Tic Tac Toe')
grid = Grid()
db = BDD()


main()