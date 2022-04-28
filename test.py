def test(): 
        tour = 0
        firstPlayer = True
        while tour < 9:
            tour += 1
            
            if firstPlayer:
                print("Au tour du joueur 1")
                print(tour)
                firstPlayer = False
            else:
                print("Au tour du joueur 2")
                print(tour)
                firstPlayer = True
            

test()