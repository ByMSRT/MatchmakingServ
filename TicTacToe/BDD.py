import sqlite3
import datetime


class BDD:

    def __init__(self):
        self.conn = sqlite3.connect('TicTacToe.db')



    print ("Opened database successfully")


    #? CREATE TABLE

    def create_player_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS Player (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username TEXT)");
        print ("Table created successfully")
    
    def create_stats_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS Stats (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Player_ID INTEGER, Win INTEGER, Lose INTEGER, Tie INTEGER, FOREIGN KEY (Player_ID) REFERENCES Player(ID) ON DELETE CASCADE)");
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
        print ("Records created successfully")


    #? Select Table

    def select_player(self):
        cursor = self.conn.execute("SELECT * FROM Player")
        for row in cursor:
            print ("ID = ", row[0])
            print ("Username = ", row[1])
    
    def select_stats(self):
        cursor = self.conn.execute("SELECT Stats.ID, Player_ID, Win, Lose, Tie, Username FROM Stats INNER JOIN Player ON Player.ID = Stats.Player_ID")
        for row in cursor:
            print ("ID = ", row[0])
            print ("Player_ID = ", row[1])
            print ("Win = ", row[2])
            print ("Lose = ", row[3])
            print ("Tie = ", row[4])
            print ("Username = ", row[5])
            print ("\n")  

    def select_game_info(self):
        cursor = self.conn.execute("SELECT * FROM Game_info")
        for row in cursor:
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