import tkinter as tk
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

# Removes eval 7 formatting
def format_cards(card_list):
    clean_cards = []
    for card in card_list:
        card_str = str(card)
        card_str = card_str.replace('Card("', '').replace('")', '')
        card_str = card_str.replace("Card('", "").replace("')", "")
        clean_cards.append(card_str)

    return ", ".join(clean_cards)

# Button Actions
def deal_button_clicked():
    game.play_hand()
    pot_label.config(text=f"Pot: {game.current_pot}")

    bot_hand_str = format_cards(game.players[1].hand)
    player_hand_str = format_cards(game.players[0].hand)
    board_label.config(text="Board: [   ] [   ] [   ] [   ] [   ]")


    bot_label.config(text=f"{game.players[1].name} Cards: {bot_hand_str} | Chips: {game.players[1].chips}")
    player_label.config(text=f"{game.players[0].name} Cards: {player_hand_str} | Chips: {game.players[0].chips}")


def advance_game_clicked():
    game.deal.board()

    board_str = format_cards(game.board)
    board_label.config(text=f"Board: {board_str}")


deal_button = tk.Button(root, text="Deal Pre-Flop", command=deal_button_clicked, font=("Helvetica", 14))
deal_button.pack(pady=10)

advance_button = tk.Button(root, text="Deal Next Street", command=advance_game_clicked, font=("Helvetica", 14))
advance_button.pack(pady=5)

root.mainloop()



