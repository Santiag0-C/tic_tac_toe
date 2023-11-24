import math
import random

class Player():
    def __init__(self,symbol):
        #la letra es X y O)
        self.symbol = symbol

    def getMove(self, game):
        position = random.choice(game.avilable_moves())
        return position

class CpmpPlayer(Player):#
    def __init__(self, simbol):
        super().__init__(symbol)
    
    def get_move(self, game):
        pass
    
class Humanplayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def getMove(self, game):
        valid_pos = False
        val = None
        while not valid_pos:
            position = input(self.symbol)
