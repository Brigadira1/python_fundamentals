from collections import namedtuple

Card = namedtuple("Card", ["rank", "suit"])


class Deck:
    ranks = [str(i) for i in range(2, 11)] + list("JQKA")
    suits = "clubs diamonds hearts spades".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


deck = Deck()
print(deck._cards)
print(len(deck))

number = 1
for card in deck:
    print(f"Card {number} - ({card.rank}) ({card.suit})")
    number += 1

print(deck[::-1])
