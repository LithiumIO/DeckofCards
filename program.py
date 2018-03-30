import random

""" Program currently set up to create a deck of cards, 
randomize said deck, then draw from deck"""

def main():
    deck = Deck()
    deck.shuffle()
    #deck.show()

    Lu = Player("Lu")
    Lu.draw(deck).draw(deck)
    Lu.showHand()


    #card = deck.draw()
    #card.show()

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ("Spades", "Clubs", "Diamonds", "Hearts"):
            for v in range(1, 14):
                self.cards.append(Card(v,s))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


if __name__ == "__main__":
    main()