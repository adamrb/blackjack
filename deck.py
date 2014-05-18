#!/usr/bin/env python
import random

class Deck:
    def __init__(self, decks=1):
        self.cards = []
        self.addDeck(decks)

    def addDeck(self, decks):
        allcards = [
            "Ace of Diamonds","King of Diamonds","Queen of Diamonds","Jack of Diamonds","10 of Diamonds","9 of Diamonds","8 of Diamonds","7 of Diamonds","6 of Diamonds","5 of Diamonds","4 of Diamonds","3 of Diamonds","2 of Diamonds",
            "Ace of Clubs","King of Clubs","Queen of Clubs","Jack of Clubs","10 of Clubs","9 of Clubs","8 of Clubs","7 of Clubs","6 of Clubs","5 of Clubs","4 of Clubs","3 of Clubs","2 of Clubs",
            "Ace of Spades","King of Spades","Queen of Spades","Jack of Spades","10 of Spades","9 of Spades","8 of Spades","7 of Spades","6 of Spades","5 of Spades","4 of Spades","3 of Spades","2 of Spades",
            "Ace of Hearts","King of Hearts","Queen of Hearts","Jack of Hearts","10 of Hearts","9 of Hearts","8 of Hearts","7 of Hearts","6 of Hearts","5 of Hearts","4 of Hearts","3 of Hearts","2 of Hearts"
            ]
        count = 0
        while count < decks:
            self.cards.extend(allcards)
            count+=1

        self.shuffle()
        return self.cards
        
    def showDeck(self):
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def getCard(self, count = 1):
        yourcard = []
        counter = 0
        while counter < count:
            yourcard.append(self.cards.pop())
            counter+=1

        return yourcard

    def count(self):
        return len(self.cards)

#cards = Deck(2)

#print cards.count()
#mycard = cards.getCard(3)
#print mycard

#print cards.count()
