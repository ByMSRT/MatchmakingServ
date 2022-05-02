from TicTacToe.Game import Game
from TicTacToe.Grid import Grid
from TicTacToe.BDD import BDD
from MatchMaking.Connection import Connection

def main():
    #print(getter.name)
    #getter.play()
    #connect.get_client_ip()
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
connect = Connection()

main()