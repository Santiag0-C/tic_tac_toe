import time
from player import Humanplayer, CompPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        
    def print_bord(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')               

    def avilable_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         move.append(i)
        # return moves
    def empty_space(self):
        return ' ' in self.board

    def num_empty_spaces(self):
        return self.board.count(' ')
        # return len(self.avilable_moves())

    def make_move(self, space, letter):
        if self.board[space] == ' ':
            self.board[space] = letter
            if self.winner(space, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index*3 : (row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        colum_ind = square % 3
        column =[self.board[colum_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_space():

        if letter == 'O':
            space = o_player.get_move(game)
        else:
            space = x_player.get_move(game)
        if game.make_move(space, letter):
            if print_game:
                print(letter + f' make a move to space {space}')
                game.print_board_nums() if letter == 'O' else None
                print('\n')
                game.print_bord()
                print('\n')

            if game.current_winner:
                if print_game:
                    print(letter + ' Wins!!!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(0.9)

    if print_game:
        print('its a tie')

if __name__ == '__main__':
    x_player = Humanplayer('X')
    o_player = CompPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)