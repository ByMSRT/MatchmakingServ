from xmlrpc.client import boolean


class Game:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName

    def test(): 
        tour = 0
        firstPlayer = boolean
        while tour < 9:
            tour += 1
            print(tour)
            if firstPlayer:
                print("Au tour du joueur 1")
            else:
                print("Au tour du joueur 2")
                break