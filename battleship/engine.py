from battleship.ship import ship
from config import Config

class engine:
    def __init__(self):
        self.shipsOnBoard = [None] * int(Config.NUMBER_OF_SHIPS)

    def setShips(self):
        """Need to add number of ships in a list, and all ships must be at unique positions"""
        # while self.shipsOnBoard[-1] is None:
        for i in range(0,5):
            newShip = ship()
            if(self.checkShip(newShip)):
                self.shipsOnBoard.append(ship())
            

            # if(shipOne == shipTwo):
            #     shipTwo = ship()
            #     shipsOnBoard[1] = shipTwo
            # else: 
            #     break
    def checkShip(self, ship):
        for s in self.shipsOnBoard:
            if(s == ship):
                return True
        return False

# def main():
begin = engine()
begin.setShips()
print(begin.shipsOnBoard)

