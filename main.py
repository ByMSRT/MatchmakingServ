from BDD.BDD import BDD
from Menu.Menu import Menu
from TicTacToe.Game import Game


def main():
    menu = Menu()
    menu.get_menu_choice()
    db.close_connexion()


getter = Game('Tic Tac Toe')

db = BDD()


main()
