from TicTacToe.Game import Game
from TicTacToe.Grid import Grid

def main():
    print(getter.name)
    print("Change name of Game")
    getter.setName("New Tic Tac Toe")
    print(getter.name)
    print(grid.display_grid())
getter = Game('Tic Tac Toe')
grid = Grid()

main()