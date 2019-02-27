import playhand

def main():
    #print ("Welcome to the COSC 1336 collaborative \
          # blackjack simulation thingy")
    PlayAgain = "Y"
    wins = 0
    losses = 0
    while (PlayAgain == "Y"):
        if (playhand.PlayHand()):
            wins += 1
        else:
            losses += 1
        PlayAgain = input("\nPlay again? (Y/N) ").upper()

    print('\n\nYou won',wins,'hands and lost',losses,'hands.')
    input('')

main()
