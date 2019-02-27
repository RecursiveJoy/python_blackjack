import random
import card

class deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        names = ['Ace','Two','Three', 'Four', 'Five', 'Six', \
                 'Seven', 'Eight', 'Nine', 'Jack', 'Queen', 'King']
        self.cardlist = []
        for suit in suits:
            for name in names:
                newCard = card.card(name, suit)
                self.cardlist.append(newCard)

    def Print(self):
        for cardobject in self.cardlist:
            print(item)
            
    def deal(self):
        firstcard = self.cardlist[0]
        del self.cardlist[0]
        return firstcard

    def shuffle(self):
        random.shuffle(self.cardlist)

