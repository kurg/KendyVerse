# Kevin van Rensburg  @KendyVerse2016
# kendy.py version 0.07
# This is KendyVerse.
# Soon it will evolve into an AI Program!

import random
import time

def displayIntro():
    #print('Hello.')
    #time.sleep(2)
    #print('Please be patient.')
    #time.sleep(5)
    print('Welcome to my Universe.')
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
        print()
        print('Enter Access Code.') # There are four spaces in front of print.
        code = input()
        code = int(code)

def instructions():
   print()
   print('DISCLAIMER: ')
   print()
   print('Kendy or it\'s manufacturers and/or programmers are and will not be responsible for any user faults.')
   time.sleep(5)
   print('Kendy or it\'s manufacturers and/or programmers will not be held liable for any lawsuits due to malfunctions of any kind whatsoever!')
   time.sleep(18)
   print()
   print('Please adhere strictly to the following instructions!')
   time.sleep(15)
   print()
   print('Eat eggs regularly.')
   time.sleep(5)
   print('Eggs must be eaten with Spam.')
   time.sleep(10)
   print()
   print('Spam and Eggs must be eaten on toast!')
   time.sleep(10)
   print()
   
def askForInput():
    print()
   newInfo=str
    while newInfo != ' ':
        print()
        print('Enter your request here.')
        newInfo = input()
        print(newInfo)
        print()
   
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

    displayIntro()
    displaySearch()
    time.sleep(5)
    accessCode()
    instructions()
    askForInput()
    # goToAdventure()
        
    # caveNumber = chooseCave()

    # checkCave(caveNumber)

    print('Do you want to restart the IPS? (yes or no)')
    playAgain = input()
