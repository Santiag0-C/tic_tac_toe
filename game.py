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
        column =[self.board[colum_ind]]

def play(game, x_payer, o_payer, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_space():
        if letter == 'O':
            space = o_player.get_move(game)
        else:
            space = x_player_get_move(game)
    
    if game.make_move(space, letter):
        if print_game:
            print(letter + f' make a move to space {space}')
            game.print_bord()
            print('\n')

        if game.current_winner:
            if print_game:
                print(letter, + 'Wins!!!')
            return letter

        letter = 'O' if letter == 'X' else 'X'
    
    if print_game:
        print('its a tie')