from dis import dis
from battleship.ship import ship
from config import Config
from math import inf

class engine:
    def __init__(self):
        self.shipsOnBoard = []
        self.tries = int(Config.NUMBER_OF_TRIES)
        self.setShips()
        self.start()

    def setShips(self):
        ind = 0
        while ind  < int(Config.NUMBER_OF_SHIPS):
            tempShip = ship()
            if(tempShip not in self.shipsOnBoard):
                self.shipsOnBoard.append(tempShip)
                ind += 1

    def calculate(self, inputList: list):
        try:
            distance = inf
            for ship in self.shipsOnBoard:
                x,y = ship.getCoordinates(True)
                nDistance = abs(inputList[0]-x) + abs(inputList[1]-y)
                if nDistance<distance:
                    distance = nDistance
            if distance == 0:
                return "Hit"
            elif distance < 3:
                return "Hot"
            elif distance < 5:
                return "Warm"
            else:
                return "Cold"
        except Exception as e:
            print(f"The error: ({e}) has occured")

    def start(self):
        print("---------------------------------------------------------------------------")
        print(f"There are {len(self.shipsOnBoard)} ships on a {Config.BOARD_SIZE_X} x {Config.BOARD_SIZE_Y} board...")
        print("You have to guess the co-ordinates (eg: 2,5)\nTYPE leave TO QUIT GAME")
        print("---------------------------------------------------------------------------\n")
        while self.tries != 0 and len(self.shipsOnBoard) != 0:
            try:
                userInput = input(f"{self.tries} tries left...Make your guess: ").replace(" ","")  
                if(userInput.lower() == "leave"):
                    break
                
                elif userInput in self.shipsOnBoard:
                    ind = self.shipsOnBoard.index(userInput)
                    self.shipsOnBoard.pop(ind)
                    print("Hit")

                else:
                    inputListTemp = userInput.split(",")
                    if(len(inputListTemp)>2):
                        raise Exception
                    inputList = [int(x) for x in inputListTemp]
                    print(self.calculate(inputList))                #Prints hot,warm or cold

                self.tries -=1
                
            except:
                print(f"Incorrect input, please write coordinates like: 2,4")

        if len(self.shipsOnBoard) == 0:
            print(f"Congratulations...You have sunk all ships in {int(Config.NUMBER_OF_TRIES)-self.tries} tries")
        else:
            print(f"Sinking Unsuccessful...{len(self.shipsOnBoard)} remaining")
            print(*self.shipsOnBoard, sep = ", ")