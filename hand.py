import random
import card
import deck

class hand:
    def __init__(self):
        self.handlist = []

    def hit(self,deck):
        hitcard = deck.deal()
        self.handlist.append(hitcard)
        return hitcard
                      
    def value(self):

        val = 0
        for c in self.handlist:
            val += c.hival()
        if val > 21:
            val = 0
            for c in self.handlist:
                val += c.loval()
        return val

    def Print(self):

        for cardobject in self.handlist:
            print(cardobject)

    def bust(self):
        if self.value() > 21:
            return True
        else:
            return False

    def blackjack(self):

        if len(self.handlist) == 2 and self.value() == 21:
            return True
        else:
            return False

    def have21(self):

        if self.value() == 21:
            return True
        else:
            return False

