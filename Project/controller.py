class GameController:
    def __init__(self, game, view):
        self.game = game
        self.view = view
        self.view.play_button.config(command=self.play_turn)

    def play_turn(self):
        # Method to handle playing a turn
        self.game.reset()
        self.game.play()
        self.view.update_display()