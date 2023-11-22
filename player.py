import math
import random

class Player():
    def __init__(self,symbol):
        #la letra es X y O)
        self.symbol = symbol

    def getMove(self, game):
        pass

class CpmpPlayer(Player):#
    def __init__(self, simbol):
        super().__init__(symbol)
    
    def get_move(self, game):
        pass
    
class Humanplayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def getMove(self, game):
        pass