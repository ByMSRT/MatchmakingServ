import sqlite3
import datetime


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
                          "Game_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," 
                          "Player_id INTEGER, "
                          "Opponent_id INTEGER NOT NULL, "
                          "Result TEXT NOT NULL,"
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
        return cursor
        # for row in cursor:
        #     print()
        #     print(f"Player {row[0]} = {row[1]} \n")

    
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

    def select_game_info(self, username):
        user_id = self.get_player_info("ID", "Username", username)
        cursor = self.conn.execute(f"SELECT * FROM Game_info WHERE Player_id = {user_id}")
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

    def get_stats_of_player(self, data, username):
        user_id = self.get_player_info("ID", "Username", username)
        for test in str(user_id):
            print(test[0])
            request = self.conn.execute(
                f"SELECT {data} FROM Stats INNER JOIN Player ON Player.ID = Stats.Player_ID WHERE Stats.Player_ID = {test[0]}")
            for player_stats in request:
                return player_stats

    def get_game_info(self, data, username):
        user_id = self.get_player_info("ID", "Username", username)

        for test in str(user_id):

            request = self.conn.execute(
                f"SELECT {data} FROM Game_info WHERE Player_id = {test[0]}")

            for game_stats in request:
                print(game_stats)
                return game_stats

    def get_player_info(self, information, parameter=None, parameter_value=None):
        user_info = None
        if isinstance(parameter_value, int):
            if parameter != None and parameter_value != None:
                user_info = self.conn.execute(f"SELECT {information} FROM Player WHERE {parameter} = {parameter_value}")
            else:
                user_info = self.conn.execute(f"SELECT {information} FROM Player")
        else:
            if parameter != None and parameter_value != None:
                user_info = self.conn.execute(f"SELECT {information} FROM Player WHERE {parameter} = '{parameter_value}'")
            else:
                user_info = self.conn.execute(f"SELECT {information} FROM Player")

        for info in user_info:
            return info[0]


    def update_stats_info(self, column_to_change, value, player_id):
        self.conn.execute(f"UPDATE Stats SET {column_to_change} = {value} WHERE Player_ID = {player_id}")
        self.conn.commit()
