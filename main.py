from TicTacToe.Game import Game
from TicTacToe.Grid import Grid
from TicTacToe.BDD import BDD

def main():
    #print(getter.name)
    getter.play()
    #db.create_player_table()
    #db.create_game_info()
    #db.insert_player("Elouan")
    #db.insert_player("Kevin")
    #db.insert_game_info(1, 2)
    #db.insert_game_info(2, 1, 0)
    #db.select_player()
    #db.select_game_info()
    #db.close_connexion()


getter = Game('Tic Tac Toe')
grid = Grid()
db = BDD()

main()