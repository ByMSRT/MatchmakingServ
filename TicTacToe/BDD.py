import sqlite3
import datetime
from TicTacToe.Game import Game


class BDD:

    def __init__(self):
        self.conn = sqlite3.connect('TicTacToe.db')



    #print ("Opened database successfully")


    #? CREATE TABLE

    def create_player_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS Player (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username TEXT)");
        print ("Table created successfully")
    
    def create_stats_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS Stats (Player_ID INTEGER, Win INTEGER, Lose INTEGER, Tie INTEGER, FOREIGN KEY (Player_ID) REFERENCES Player(ID) ON DELETE CASCADE)");
        print ("Table created successfully")
        

    def create_game_info(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS Game_info ("
                          "Player_id INTEGER, "
                          "Opponent_id INTEGER NOT NULL, "
                          "Result BOOLEAN NOT NULL,"
                          "Start_time timestamp, "
                          "FOREIGN KEY (Player_id) REFERENCES Player(ID))")
        print("Table Game_info created successfully")



    #? INSERT FOR TEST

    def insert_player(self, username):
        self.conn.execute("INSERT INTO Player (Username) VALUES (?)", (username,))
        self.conn.commit()
        print("Records created successfully player")

    def insert_game_info(self, player_id, opponent_id, result):
        self.conn.execute("INSERT INTO Game_info (Player_id, Opponent_id, Result, Start_time) VALUES(?,?,?,?)", (player_id, opponent_id, result, datetime.datetime.now()))
        self.conn.commit()
        print("Records created successfully game info")


    def insert_stats(self, player_id, win, lose, tie):
        self.conn.execute("INSERT INTO Stats (Player_ID, Win, Lose, Tie) VALUES (?,?,?,?)", (player_id, win, lose, tie))
        self.conn.commit()
        print("Records created successfully")


    #? Select Table

    def select_player(self):
        cursor = self.conn.execute("SELECT * FROM Player")
        for row in cursor:
            print()
            print(f"Player {row[0]} = {row[1]} \n")
    
    def select_stats(self):
        cursor = self.conn.execute("SELECT Player_ID, Win, Lose, Tie, Username FROM Stats INNER JOIN Player ON Player.ID = Stats.Player_ID")
        for row in cursor:
            print()
            print("Player_ID = ", row[0])
            print("Win = ", row[1])
            print("Lose = ", row[2])
            print("Tie = ", row[3])
            print("Username = ", row[4])
            print("\n")

    def select_game_info(self):
        cursor = self.conn.execute("SELECT * FROM Game_info")
        for row in cursor:
            print()
            print("Player ID = ", row[0])
            print("Opponent ID = ", row[1])
            print("Result = ", row[2])
            print("Start time = ", row[3])

    #? Delete table

    def delete_all_table(self):
        self.conn.execute("DROP TABLE IF EXISTS Player")
        self.conn.execute("DROP TABLE IF EXISTS Stats")
        print ("Table deleted successfully")

    #? Close connection
    def close_connexion(self):
        self.conn.close()
        print ("Closed database successfully")


    # -------------------------- SQLite request -------------------------

    def get_stats_of_player(self, username):
        user_id = self.get_player_info("ID", "Username", username)
        for test in str(user_id):
            print(test[0])

            request = self.conn.execute(
                f"SELECT Player_ID, Win, Lose, Tie FROM Stats INNER JOIN Player ON Player.ID = Stats.Player_ID WHERE Stats.Player_ID = {test[0]}")
            for player_stats in request:
                print(f"Joueur : '{username}' \n"
                      f"ID : {player_stats[0]} \n"
                      f"Partie Gagné : {player_stats[1]} \n"
                      f"Partie Perdu : {player_stats[2]} \n"
                      f"Partie Nul : {player_stats[3]} \n")

    def get_game_info(self, username):
        user_id = self.get_player_info("ID", "Username", username)
        for test in str(user_id):
            request = self.conn.execute(
                f"SELECT Player_id, Opponent_id, Result, Start_time FROM Game_info INNER JOIN Player ON Player.ID = Player_id WHERE Player_id = {test[0]}")
            for game_stats in request:
                print(f"Joueur : '{username}' \n"
                      f"ID : {game_stats[0]} \n"
                      f"Adversaire ID : {game_stats[1]} \n"
                      f"Nom Adversaire : {self.get_player_info('Username', 'ID', game_stats[1])} \n"
                      f"Resultat : {game_stats[2]} \n"
                      f"Debut de partie : {game_stats[3]} \n")

    def get_player_info(self, information, parameter, parameter_value):
        user_info = None
        if isinstance(parameter_value, int):
            user_info = self.conn.execute(f"SELECT {information} FROM Player WHERE {parameter} = {parameter_value}")
        else:
            user_info = self.conn.execute(f"SELECT {information} FROM Player WHERE {parameter} = '{parameter_value}'")

        for info in user_info:
            return info[0]
        #Return string and not tuplr


game = Game("Tic Tac Toe")