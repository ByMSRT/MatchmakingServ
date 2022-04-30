import sqlite3
import datetime


class BDD:

    def __init__(self):
        self.conn = sqlite3.connect('TicTacToe.db')



    print ("Opened database successfully")


    #? CREATE TABLE

    def create_player_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS Player (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username TEXT)");
        print ("Table Player created successfully")

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




    #? Select Player

    def select_player(self):
        cursor = self.conn.execute("SELECT * FROM Player")
        for row in cursor:
            print("ID = ", row[0])
            print("Username = ", row[1])

    def select_game_info(self):
        cursor = self.conn.execute("SELECT * FROM Game_info")
        for row in cursor:
            print("Player ID = ", row[0])
            print("Opponent ID = ", row[1])
            print("Result = ", row[2])
            print("Start time = ", row[3])



    #? Close connection
    def close_connexion(self):
        self.conn.close()