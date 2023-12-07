import math
import random

class Player():
    def __init__(self,symbol):
        #la letra es X y O)
        self.symbol = symbol

    def getMove(self, game):
        position = random.choice(game.avilable_moves())
        return position

class CompPlayer(Player):#
    def __init__(self, symbol):
        super().__init__(symbol)
    
    def get_move(self, game):
        space = random.choice(game.avilable_moves())
        return space
    
class Humanplayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)
    

    #######################################
    def get_move(self, game):
        valid_pos = False
        val = None
        while not valid_pos:
            square = input(self.symbol + '\'s Turn input move (0-9):')

            try:
                #val has the number of the index that of where
                #you want to go and the  enumerated array that 
                #game.avilable_moves() returns with all the valid index 
                #positions and val is not in the game.avilable_moves():
                val = int(square)
                if val not in game.avilable_moves():
                    raise ValueError
                valid_pos = True
            except ValueError:
                print('invalid square. Try again')
        return val

