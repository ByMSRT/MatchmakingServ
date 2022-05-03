from MatchMaking.Connection import Connection
from TicTacToe.Grid import Grid
from TicTacToe.Game import Game
from TicTacToe.BDD import BDD

#from TicTacToe.Pions import Pions

def main():
    result_input = menu()
    if result_input == 1:
        username = input("Quel est votre pseudo ? ")
        print()
        print("Info Player")
        db.select_player()
        print()
        print("Game info")
        db.select_game_info(username)
        print()
        print("Stat info")
        db.select_stats()
    elif result_input == 2:
        getter.play()
    elif result_input == 3:
        username = input("Quel est votre pseudo ? ")
        db.insert_player(username)
    elif result_input == 4:
        player_id = input("Quelle est votre ID ? ")
        win = input("Combien de partie avez-vous win ? ")
        loose = input("Combien de partie avez-vous loose ? ")
        null = input("Combien avez-vous fait de partie nul ? ")
        db.insert_stats(player_id, win, loose, null)
    elif result_input == 5:
        player_id = input("Quelle est votre ID ? ")
        opponent_id = input("Quelle est l'ID de votre adversaire ? ")
        result = input("Avez-vous gagné ? ")
        db.insert_game_info(player_id, opponent_id, result)
    elif result_input == 6:
        db.create_player_table()
        db.create_stats_table()
        db.create_game_info()
    elif result_input == 7:
        username = input("Quel est votre pseudo ? ")
        data_stats = "Win, Lose, Tie"
        data_game_info = "Player_id, Opponent_id, Result, Start_time"
        #user_id = input("Quel est votre ID ? ")
        #name = db.get_player_info("Username", "ID", int(user_id))
        #print(name)
        #id = db.get_player_info("ID", "Username", username)
        #print(id)
        for stat in db.get_stats_of_player(data_stats, username):
            print(stat)
        print()
        #for game_info in db.get_game_info(data_game_info, username):
         #   print("game_info")
        db.get_game_info(data_game_info, username)
    db.close_connexion()

def menu():
    print("1 : Info BDD")
    print("2 : Play")
    print("3 : Insert Player")
    print("4 : Insert Stat")
    print("5 : Insert Game Info")
    print("6 : Create all table")
    print("7 : Connect")
    result = input("Que veux-tu faire ?")
    return int(result)


getter = Game('Tic Tac Toe')
grid = Grid()
db = BDD()
connect = Connection()

main()