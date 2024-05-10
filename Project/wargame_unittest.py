import unittest
from model import Game, Player, Card

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_play_game(self):
        self.game.play()
        winner = self.game.get_winner()
        self.assertIsNotNone(winner, "No winner detected after playing the game.")

    def test_players_start_with_correct_number_of_cards(self):
        self.assertEqual(self.game.p1.num_cards(), 26, "Player 1 did not start with 26 cards.")
        self.assertEqual(self.game.p2.num_cards(), 26, "Player 2 did not start with 26 cards.")

    def test_enough_cards_after_war(self):
        # Manually create a situation where a war occurs
        self.game.p1.play_pile.add_card(Card(3, 1))  # 3 of Hearts
        self.game.p2.play_pile.add_card(Card(3, 3))  # 3 of Spades
        self.game.p1.play_pile.add_card(Card(4, 0))  # 4 of Diamonds
        self.game.p2.play_pile.add_card(Card(4, 2))  # 4 of Clubs
        self.game.play()  # Resolve the war
        self.assertTrue(self.game.enough_cards(1), "Not enough cards after resolving the war.")

    def test_war_scenario(self):
        # Manually create a war scenario
        self.game.p1.play_pile.add_card(Card(4, 1))  # 4 of Hearts
        self.game.p1.play_pile.add_card(Card(4, 3))  # 4 of Spades
        self.game.p1.play_pile.add_card(Card(4, 0))  # 4 of Diamonds
        self.game.p2.play_pile.add_card(Card(4, 2))  # 4 of Clubs
        self.game.p2.play_pile.add_card(Card(4, 2))  # 4 of Clubs
        self.game.p2.play_pile.add_card(Card(4, 2))  # 4 of Clubs
        self.game.play()  # Resolve the war
        # After the war, the player with the highest ranked card should win
        self.assertTrue(self.game.p1.num_cards() > self.game.p2.num_cards() or
                        self.game.p2.num_cards() > self.game.p1.num_cards(), "War not resolved correctly.")

if __name__ == '__main__':
    unittest.main()
