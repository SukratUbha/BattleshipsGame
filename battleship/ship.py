import random
from config import Config

class ship():
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def setRandomPosition(self):
        self.x = random.randint(1,int(Config.BOARD_SIZE))
        self.y = random.randint(1,int(Config.BOARD_SIZE))
        
    def __repr__(self):
        return "This ship is located at {} {}  ".format(self.x, self.y)

    def __eq__(self, other):
        print(other)
        if isinstance(other,ship):
            print("Checking equality...")
            if other.x == self.x and other.y == self.y:
                return True
            else:
                return False
        else:
            return "Invalid Type Comparison"
