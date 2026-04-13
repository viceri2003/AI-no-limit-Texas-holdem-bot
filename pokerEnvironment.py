class Player:
    def __init__(self, name, starting_chips):
        self.name = name
        self.chips = starting_chips
        self.hand = []
        self.current_bet = 0
        self.in_play = True

    def __str__(self):
        return f" {self.name} (Chips: {self.chips})"

