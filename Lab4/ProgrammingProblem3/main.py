import unittest
from unittest.mock import patch
from io import StringIO
import oxo_logic
import oxo_data

class TestOXOLogic(unittest.TestCase):
    def setUp(self):
        self.game = oxo_logic.Game()

    def test_new_game(self):
        try:
            self.assertEqual(self.game._game, [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        except AssertionError as e:
            self.fail(f"Assertion failed: {str(e)}")

    def test_save_and_restore_game(self):
        try:
            self.game._game = ['X', 'O', ' ', 'X', ' ', 'O', ' ', ' ', 'X']
            self.game.saveGame()
            self.game.restoreGame()
            self.assertEqual(self.game._game, ['X', 'O', ' ', 'X', ' ', 'O', ' ', ' ', 'X'])
        except Exception as e:
            self.fail(f"Exception occurred: {str(e)}")

    @patch('builtins.input', side_effect=['4'])
    def test_user_move(self, mock_input):
        try:
            self.game._game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            result = self.game.userMove(4)
            self.assertEqual(self.game._game, [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' '])
            self.assertEqual(result, '')
        except Exception as e:
            self.fail(f"Exception occurred: {str(e)}")

    @patch('builtins.input', side_effect=['0'])
    def test_user_move_invalid(self, mock_input):
        try:
            self.game._game = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            with self.assertRaises(ValueError):
                self.game.userMove(0)
        except Exception as e:
            self.fail(f"Exception occurred: {str(e)}")

    def test_computer_move(self):
        try:
            self.game._game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            result = self.game.computerMove()
            self.assertIn('O', self.game._game)
        except Exception as e:
            self.fail(f"Exception occurred: {str(e)}")

    def test_is_winning_move(self):
        try:
            self.game._game = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
            self.assertTrue(self.game._isWinningMove())

            self.game._game = ['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
            self.assertTrue(self.game._isWinningMove())

            self.game._game = ['X', ' ', 'O', 'X', ' ', 'O', 'X', ' ', 'O']
            self.assertFalse(self.game._isWinningMove())
        except Exception as e:
            self.fail(f"Exception occurred: {str(e)}")

    @patch('sys.stdout', new_callable=StringIO)
    @patch('builtins.input', side_effect=['4', '0', '2', '1', '3', '5', '6'])
    def test_game_flow(self, mock_input, mock_stdout):
        try:
            self.game.test()
            output = mock_stdout.getvalue()
            self.assertIn('Winner is:', output)
            self.assertIn('X', output)
            self.assertNotIn('O', output)
        except Exception as e:
            self.fail(f"Exception occurred: {str(e)}")

if _name_ == '_main_':
    unittest.main()
