import tkinter as tk
from tkinter import messagebox

class CardGameView(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.title("Card Game")

        self.canvas = tk.Canvas(self, width=800, height=430)
        self.canvas.pack()

        # Create a frame to hold the text widgets and scrollbars
        self.frame = tk.Frame(self)
        self.frame.place(x=10, y=50, width=780, height=800)

        # Create a Text widget for player 1
        self.player1_text = tk.Text(self.frame, font=("Arial", 12), height=20, width=40)
        self.player1_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Create a Scrollbar for player 1
        self.player1_scrollbar = tk.Scrollbar(self.frame, command=self.player1_text.yview)
        self.player1_scrollbar.grid(row=0, column=1, sticky="ns")
        self.player1_text.config(yscrollcommand=self.player1_scrollbar.set)

        # Create a Text widget for player 2
        self.player2_text = tk.Text(self.frame, font=("Arial", 12), height=20, width=40)
        self.player2_text.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

        # Create a Scrollbar for player 2
        self.player2_scrollbar = tk.Scrollbar(self.frame, command=self.player2_text.yview)
        self.player2_scrollbar.grid(row=0, column=3, sticky="ns")
        self.player2_text.config(yscrollcommand=self.player2_scrollbar.set)

        self.play_button = tk.Button(self, text="Play", command=self.play_turn, bg="black", fg="white", font=("Arial", 16))
        self.play_button.place(x=350, y=5, width=100, height=30)

    def update_display(self):
        max_cards = max(self.game.p1.num_cards(), self.game.p2.num_cards())
        text_height = max(20, max_cards // 5 + 1)

        self.player1_text.config(height=text_height)
        self.player2_text.config(height=text_height)

        player1_pile_text = f"{self.game.p1.get_name()}: {self.game.p1.num_cards()} cards\n"
        for card in self.game.p1.play_pile.pile:
            player1_pile_text += str(card) + "\n"
        self.player1_text.delete(1.0, tk.END)
        self.player1_text.insert(tk.END, player1_pile_text)

        player2_pile_text = f"{self.game.p2.get_name()}: {self.game.p2.num_cards()} cards\n"
        for card in self.game.p2.play_pile.pile:
            player2_pile_text += str(card) + "\n"
        self.player2_text.delete(1.0, tk.END)
        self.player2_text.insert(tk.END, player2_pile_text)

        # Check for winner after every turn
        if self.game.turn_count >= 100:
            winner = self.game.get_winner()
            if winner:
                winner_name = winner.get_name()
                messagebox.showinfo("Game Over", f"The winner is {winner_name}!")
            else:
                messagebox.showinfo("Game Over", "It's a tie!")

        # Display war scenario
        if self.game.enough_cards(1):  # Check if there are enough cards to start a war
            c1 = self.game.p1.play_card()
            c2 = self.game.p2.play_card()
            if c1 == c2:  # War happened
                war_message = "--------------WAR--------------\n"
                war_message += f"({c1.get_rank()} of {c1.get_suit()} for {self.game.p1.get_name()})\n"
                war_message += f"({c2.get_rank()} of {c2.get_suit()} for {self.game.p2.get_name()})\n"
                self.player1_text.insert(tk.END, war_message)
                self.player2_text.insert(tk.END, war_message)
                self.game.play()  # Proceed with the war
                
    def play_turn(self):
        self.game.reset()
        self.game.play()
        self.update_display()
