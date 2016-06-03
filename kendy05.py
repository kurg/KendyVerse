# Kevin van Rensburg  @KendyVerse2016
# kendy.py version 0.05
# This is KendyVerse.
# Soon it will evolve into an AI Program!

import random
import time

def displayIntro():
    print('Hello.')
    time.sleep(2)
    print('Please be patient.')
    time.sleep(5)
    print('This is KendyVerse.')
    time.sleep(8)
#print('Soon it will evolve into an AI Program!')
    print()

def displaySearch():
    print('-',end='')
    time.sleep(2)
    print('-',end='')
    time.sleep(2)
    print('-')
    time.sleep(2)
    print('searching...',end='')
    time.sleep(2)
    print('...',end='')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('Initiating Program Sequence')
    time.sleep(2)
    print('...',end='')
    time.sleep(1)
    print('...')
    print('Initiating Diagnostics')
    time.sleep(1)
    print('...',end='')
    time.sleep(1)
    print('...')
    print('searching...',end='')
    time.sleep(2)
    print('...',end='')
    time.sleep(2)
    print('...',end='')
    time.sleep(2)
    print('...')
    print('Scanning ports...',end='')
    time.sleep(2)
    print('...',end='')
    time.sleep(2)
    print('...')

def accessCode():
    code=int
    while code != 1824:
        print('Enter Access Code.') # There are four spaces in front of print.
        code = input()
        code = int(code)

def instructions():

   print('DISCLAIMER: ')
   print('Kendy or it\'s manufacturers or programmers are and will not be responsible for any user faults ',end='')
   time.sleep(5)
   print('and will not be held liable for any lawsuits due to misfunctions of any kind whatsoever!')
   time.sleep(18)
   print()
   print('Please adhere strictly to the following instructions!')
   time.sleep(15)
   print()
   print('Eat eggs regularly.',end='')
   time.sleep(1)
   print(' Eggs should be eaten with Spam.')
   time.sleep(10)
   print('Spam and Eggs must be eaten on toast!')
   time.sleep(10)
   print()
   
   
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()
    displaySearch()
    time.sleep(5)
    accessCode()
    instructions()
    
    # caveNumber = chooseCave()

    # checkCave(caveNumber)

    print('Do you want to restart the IPS? (yes or no)')
    playAgain = input()
