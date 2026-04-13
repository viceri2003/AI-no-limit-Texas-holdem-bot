class Player:
    def __init__(self, name, starting_chips):
        self.name = name
        self.chips = starting_chips
        self.hand = []
        self.current_bet = 0
        self.in_play = True

    def __str__(self):
        return f" {self.name} (Chips: {self.chips})"

class heads_up_poker():
    def __init__(self, player1, player2):
        self.player1 = Player(player1.name, player1.chips)
        self.player2 = Player(player2.name, player2.chips)
        self.board = []
        self.is_preflop = True
        self.is_flop = False
        self.is_turn = False
        self.is_river = False
        self.current_pot = 0
        self.current_bet = 0

        # Index 0 means Player 1 has the button, Index 1 means Player 2
        self.has_button_index = 0
        self.sb_amount = 0
        self.bb_amount = 0