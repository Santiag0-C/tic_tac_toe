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
            position = input(self.symbol + '\'s Turn input move (0-9):')
            try:
                val = int(position)
                if val not in game.avilable_moves():
                    raise ValueError
                valid_pos = True
            except ValueError:
                print('invalid square. Try again')
        return val

