import tkinter as tk
import pokerEnvironment
from pokerEnvironment import heads_up_poker

game = heads_up_poker("User", "Bot")
root = tk.Tk()
root.title("Poker")
root.config(bg="#2b7a0b")

pot_label = tk.Label(root, text="Pot: 0", font=("Helvetica", 16, "bold"), bg="#2b7a0b", fg="white")
pot_label.pack(pady=20)

bot_label = tk.Label(root, text="Bot Cards: [ ? ] [ ? ]", font=("Helvetica", 14), bg="#2b7a0b", fg="white")
bot_label.pack(pady=10)

player_label = tk.Label(root, text="Your Cards: [   ] [   ]", font=("Helvetica", 14), bg="#2b7a0b", fg="white")
player_label.pack(pady=10)

def deal_button_clicked():
    game.play_hand()

    pot_label.config(text=f"Pot: {game.current_pot}")

    bot_label.config(text=f"{game.players[1].name} Cards: {game.players[1].hand} | Chips: {game.players[1].chips}")
    player_label.config(text=f"{game.players[0].name} Cards: {game.players[0].hand} | Chips: {game.players[0].chips}")


deal_button = tk.Button(root, text="Deal Pre-Flop", command=deal_button_clicked, font=("Helvetica", 14))
deal_button.pack(pady=30)

root.mainloop()

