from TicTacToe.Game import Game
from TicTacToe.Grid import Grid
from BDD.BDD import BDD
from Menu.Menu import Menu
from TicTacToe.Grid import Grid
from TicTacToe.Game import Game


#from TicTacToe.Pions import Pions

def main():
    menu = Menu()
    menu.get_menu_choice()
    db.close_connexion()

    
getter = Game('Tic Tac Toe')
grid = Grid()
db = BDD()
#connect = Connection()

main()