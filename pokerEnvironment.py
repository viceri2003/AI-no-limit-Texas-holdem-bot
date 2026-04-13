import eval7


# A class representing a player
class Player:
    def __init__(self, name, starting_chips):
        self.name = name
        self.chips = starting_chips
        self.hand = []
        self.current_bet = 0
        self.in_play = True

    def __str__(self):
        return f" {self.name} (Chips: {self.chips})"

# A class representing the poker environment
class heads_up_poker():
    def __init__(self, player1, player2):
        self.players = [Player(player1, 1000), Player(player2, 1000)]

        self.deck = eval7.Deck()
        self.board = []
        self.is_preflop = True
        self.is_flop = False
        self.is_turn = False
        self.is_river = False
        self.current_pot = 0
        self.current_bet = 0

        # Index 0 means Player 1 has the button, Index 1 means Player 2
        self.has_button_index = 0

        # Blind sizing
        self.sb_amount = 10
        self.bb_amount = 20

    def post_blinds(self):

        # Identifying which player has blinds
        sb_player = self.players[self.has_button_index]
        bb_player = self.players[1 - self.has_button_index]

        sb_player.chips -= self.sb_amount
        sb_player.current_bet = self.sb_amount

        bb_player.chips -= self.bb_amount
        bb_player.current_bet = self.bb_amount


        self.current_pot += (self.bb_amount + self.sb_amount)

        return sb_player, bb_player

    # Creating logic to play a hand, using the eval7 library.
    # It is used to simulate a deck where you can shuffle, deal and
    # count ranges etc
    def play_hand(self):
        self.deck.shuffle()
        self.board = []
        self.current_pot = 0
        for p in self.players:
            p.hand = [self.deck.deal(2)]
            p.in_play = True
            p.current_bet = 0

        sb_player, bb_player = self. post_blinds()

        self.has_button_index = 1 - self.has_button_index

    def deal_board(self):
        if(self.is_preflop):
            self.board = [self.deck.deal(3)]
            self.is_preflop = False
            self.is_flop = True
        elif(self.is_flop):
            new_card = self.deck.deal(1)
            self.board.extend([new_card])
            self.is_flop = False
            self.is_turn = True
        elif(self.is_turn):
            new_card = self.deck.deal(1)
            self.board.extend([new_card])
            self.is_turn = False
            self.is_river = True
        elif(self.is_river):
            self.reset_board()
            self.is_river = False
            self.is_pre_flop = True

    def reset_board(self):
        self.board = []

