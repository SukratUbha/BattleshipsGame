import random
from config import Config

class ship():
    def __init__(self):
        self.x = random.randint(1,int(Config.BOARD_SIZE_X))
        self.y = random.randint(1,int(Config.BOARD_SIZE_Y))
    
    def getCoordinates(self, flag: bool):
        if flag == True:
            return self.x, self.y
        return f"{self.x},{self.y}"
        
    def __repr__(self):
        return f"This ship is located at {self.x},{self.y}"

    def __eq__(self, other):
        #Using isinstance for user input comparison below
        if isinstance(other,str):
            if other == self.getCoordinates(False):
                return True
            else:
                return False
        try:
            if other.x == self.x and other.y == self.y:
                return True
            else:
                return False
        except:
            return "Invalid Type Comparison"
