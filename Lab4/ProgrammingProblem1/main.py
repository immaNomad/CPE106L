import os
import random
import oxo_data

class Game:
    def __init__(self):
        self.board = self.new_game()

    def new_game(self):
        return list(" " * 9)

    def save_game(self):
        oxo_data.saveGame(self.board)

    def restore_game(self):
        try:
            self.board = oxo_data.restoreGame()
            if len(self.board) != 9:
                self.board = self.new_game()
        except IOError:
            self.board = self.new_game()

    def user_move(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
            if self._is_winning_move(self.board):
                return 'X'
            else:
                return ""

    def computer_move(self):
        cell = self._generate_move(self.board)
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._is_winning_move(self.board):
            return 'O'
        else:
            return ""

    def _generate_move(self, game):
        options = [i for i in range(len(game)) if game[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _is_winning_move(self, game):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6))

        for a, b, c in wins:
            chars = game[a] + game[b] + game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False
