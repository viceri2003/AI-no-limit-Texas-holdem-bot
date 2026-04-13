import tkinter as tk
import pokerEnvironment
from pokerEnvironment import heads_up_poker

game = heads_up_poker("User", "Bot")
root = tk.Tk()
root.title("Poker")
root.config(bg="white")

pot_label = tk.Label(root, text="Pot: 0", font=("Helvetica", 16, "bold"), bg="white", fg="black")
pot_label.pack(pady=20)

bot_label = tk.Label(root, text="Bot Cards: [ ? ] [ ? ]", font=("Helvetica", 14), bg="white", fg="black")
bot_label.pack(pady=10)

board_label = tk.Label(root, text="Board: [   ] [   ] [   ] [   ] [   ]", font=("Helvetica", 18, "bold"), bg="white", fg="black")
board_label.pack(pady=20)

player_label = tk.Label(root, text="Your Cards: [   ] [   ]", font=("Helvetica", 14), bg="white", fg="black")
player_label.pack(pady=10)

# Button Actions
def deal_button_clicked():
    game.play_hand()
    pot_label.config(text=f"Pot: {game.current_pot}")

    board_label.config(text="Board: [   ] [   ] [   ] [   ] [   ]")

    bot_hand_str = ", ".join(str(card) for card in game.players[1].hand)
    player_hand_str = ", ".join(str(card) for card in game.players[0].hand)

    bot_label.config(text=f"{game.players[1].name} Cards: {bot_hand_str} | Chips: {game.players[1].chips}")
    player_label.config(text=f"{game.players[0].name} Cards: {player_hand_str} | Chips: {game.players[0].chips}")

root.mainloop()



