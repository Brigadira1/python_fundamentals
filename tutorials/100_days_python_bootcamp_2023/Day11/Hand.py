class Hand:
    def __init__(self, is_dealer=False):
        self.cards = []
        self.score = 0
        self.is_dealer = is_dealer

    def add_cards(self, cards_dealt):
        self.cards.extend(cards_dealt)

    def calculate_score(self):
        self.score = 0
        has_ace = False
        for card in self.cards:
            self.score += card.rank["value"]
            if card.rank["rank"] == 'A':
                has_ace = True
        if has_ace and self.score > 21:
            self.score -= 10

    def get_score(self):
        self.calculate_score()
        return self.score

    def is_blackjack(self):
        return self.get_score() == 21

    def display(self):
        print(f'''{"Dealer's" if self.is_dealer else "Your's"} hand is:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.is_dealer and not self.is_blackjack():
                print("Hidden")
            else:
                print(card)
        if not self.is_dealer:
            print(f"The score is: {self.get_score()}")
        print()