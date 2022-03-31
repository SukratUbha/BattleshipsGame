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
        return "This ship is located at " + str(self.x) + " " + str(self.y)

