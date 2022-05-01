from TicTacToe.Game import Game
from TicTacToe.Grid import Grid
from TicTacToe.BDD import *

def main():
    print(getter.name)
    getter.play()


getter = Game('Tic Tac Toe')
grid = Grid()
db = BDD()

main()