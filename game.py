class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        
    def print_bord(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for i in range(3)]
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

    def num_empty_spaces():
        return self.board.count(' ')
        # return len(self.avilable_moves())

def play(game, x_payer, o_payer, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_space():
        pass
