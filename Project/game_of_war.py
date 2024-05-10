from model import Game
from view import CardGameView
from controller import GameController

# This is the main entry point of the application

if __name__ == "__main__":
    # Initialize the Model, View, and Controller
    game = Game()
    view = CardGameView(game)
    controller = GameController(game, view)
    
    # Start the application
    view.mainloop()
