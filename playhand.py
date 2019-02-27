import card
import deck
import hand
import time

def PlayHand():

        d = deck.deck()
        uhand = hand.hand()
        dhand = hand.hand()

        d.shuffle()

        uhand.hit(d)
        uhand.hit(d)
        dhand.hit(d)
        lastcard = dhand.hit(d)

        print('\n')
        print('------------------------------')
        print('Dealer is showing', lastcard, '\n')
        
#What's in your hand

        print('Your hand:')
        uhand.Print()
        print('You have a total of', uhand.value(),'\n')
        
        if uhand.blackjack():
            input('You have a blackjack!')
        else:
            hit = input('Enter \'h\' to hit or \'s\' to stand: ')
 

#User hits until bust, 21, or stand
        while hit == 'h':
            lastcard = uhand.hit(d)
             
            print('You got the', lastcard,'\n')
            print('Your hand:')
            uhand.Print()
            print('You have a total of', uhand.value(),'\n')    
        
            if uhand.bust() == True:
                print('You have a bust.')
                hit = 'n'
            elif uhand.have21() == True:
                print('You have 21.')
                hit = 'n'
            else:
                hit = input('Type \'h\' for hit or \'s\' for stand: \n')

#Dealer's turn
        print('Dealer has:')
        dhand.Print()
        print('Dealer has a total of', dhand.value(),'\n')

        time.sleep(.5)
        
        while dhand.value() < 17:
            lastcard = dhand.hit(d)
            print('Dealer hits, gets the',lastcard)
            print('Dealer has a total of', dhand.value())

        time.sleep(.5)

#Decide the winner
        if uhand.bust():
            print('Game Over, you busted!')
            return False
        if uhand.bust()== False and dhand.value() > 21:
            print('Dealer Busted, you win!')
            return True
        if uhand.value()<= 21 and uhand.value()> dhand.value():
            print('You scored higher than the dealer, you win!')
            return True
        if dhand.blackjack() == False and uhand.blackjack():
            print('You have a blackjack. You win!')
            return True
        if dhand.value() == uhand.value():
            print('It\'s a tie! Nobody wins.')
        else:
            print('You lose.')
            return False
        
