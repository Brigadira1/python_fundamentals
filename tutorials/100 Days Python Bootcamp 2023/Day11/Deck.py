import random
from Card import Card
from Hand import Hand


class Deck:
    def __init__(self):
        self.cards_deck = []
        suits = ["heart", "spade", "diamond", "club"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "D", "value": 10},
            {"rank": "K", "value": 10},
        ]
        for suit in suits:
            for rank in ranks:
                self.cards_deck.append(Card(suit, rank))

    def shuffle(self):
        if len(self.cards_deck) > 1:
            return random.shuffle(self.cards_deck)

    def deal(self, number):
        cards_dealt = []
        for card in range(number):
            if len(self.cards_deck) > 0:
                current_card = self.cards_deck.pop()
                cards_dealt.append(current_card)
        return cards_dealt


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    hand = Hand()
    hand.add_cards(deck.deal(2))
    hand1 = Hand(is_dealer=True)
    hand1.add_cards(deck.deal(2))
    hand.display()
    hand1.display()
