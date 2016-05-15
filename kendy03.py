# Kevin van Rensburg  @KendyVerse2016
# kendy.py version 0.03
# This is KendyVerse.
# Soon it will evolve into an AI Program!


import random
import time

def displayIntro():
    print('This is KendyVerse.')
    print()

    
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()
    time.sleep(5)
    
    # caveNumber = chooseCave()

    # checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
