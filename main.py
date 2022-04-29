from TicTacToe.Game import Game
from TicTacToe.Grid import Grid
from TicTacToe.BDD import *

def main():
    #print(getter.name)
    #getter.play()
    db.create_player_table()
    """ db.insert_player("Elouan") """
    db.select_player()
    db.close_connexion()


getter = Game('Tic Tac Toe')
grid = Grid()
db = BDD()

main()