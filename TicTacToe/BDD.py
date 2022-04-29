import sqlite3

class BDD:

    def __init__(self):
        self.conn = sqlite3.connect('TicTacToe.db')



    print ("Opened database successfully")


    #? CREATE TABLE

    def create_player_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS Player (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Username TEXT)");
        print ("Table created successfully")



    #? INSERT FOR TEST

    def insert_player(self, username):
        self.conn.execute("INSERT INTO Player (Username) VALUES (?)", (username,))
        self.conn.commit()
        print ("Records created successfully")



    #? Select Player

    def select_player(self):
        cursor = self.conn.execute("SELECT * FROM Player")
        for row in cursor:
            print ("ID = ", row[0])
            print ("Username = ", row[1])


    #? Close connection
    def close_connexion(self):
        self.conn.close()