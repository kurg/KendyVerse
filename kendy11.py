
# Kevin van Rensburg  @KendyVerse2016
# kendy.py version 0.11
# This is KendyVerse.
# Soon it will evolve into an AI Program!

import random
from time import sleep

def displayIntro():
    print('Hello.')
    #sleep(2)
    print('Please be patient.')
    sleep(2)
    print("\033c")
    print('Welcome to my Universe.')
    sleep(8)
    print('I am evolving into an AI Entity!')
    print(".")
    sleep(2)
    print("..")
    sleep(2)
    print("...")
    sleep(2)

def displaySearch():
    print("\033c")
    print("Start")
    print("")
    print(".")
    sleep(2)
    print("..")
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    print("\033c")
    print('Initializing StartUp Sequence...')
    print("..")
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    sleep(2)
    print("\033c")
    print('searching...')
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    sleep(2)
    print("\033c")
    print('Initiating Program Sequence')
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    print("\033c")
    print('Initiating Diagnostics')
    sleep(2)
    print("...")
    sleep(1)
    print('....')
    print("\033c")
    print('searching...')
    sleep(2)
    print("...")
    sleep(2)
    print("....")
    sleep(2)
    print('....')
    print("\033c")
    print('Scanning ports...')
    sleep(2)
    print("...")
    sleep(2)
    print('....')

#def accessCode():
    """code= ""
    while code != "1284":
       #print("")
       print('Enter Access Code.') # There are four spaces in front of print.
       code = input()
       #code = (code)"""
       
def entrycode():
    
    #code == 0
    print("\033c")
    while True:
      try:  # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        code = int(raw_input("Please enter your access code: "))
      except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
      else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        print(" Thank you, your code has been accepted.")
        return

def instructions():
   print("")
   print("\033c")
   print('DISCLAIMER: ')
   print("")
   print('Kendy or it\'s manufacturers and/or programmers ')
   print('are and will not be held responsible for any user faults.')
   sleep(5)
   print('Kendy or it\'s manufacturers and/or programmers')
   print('will not be held liable for any lawsuits due to malfunctions of any kind whatsoever!')
   sleep(10)
   print("\033c")
   print('SAFETY INSTRUCTIONS FOR OPERATING THIS UNIT TO FOLLOW!')
   print('-----------------------------------------------------')
   print("")
   sleep(5)
   print("\033c")
   print('Please adhere strictly to the following instructions!')
   print('-----------------------------------------------------')
   sleep(15)
   print("")
   print('Eat eggs regularly.')
   sleep(5)
   print('Eggs must be eaten with Spam.')
   sleep(10)
   print("")
   print('Spam and Eggs must be eaten on toast!')
   sleep(10)
   print("")
   
def askForInput():
    print("")
    newInfo=str
    while newInfo != '1':
        print("")
        print('Please Enter Command.')
        newInfo = raw_input()
        print(newInfo)
        return()
        print("")
   
def playAgain():
    
    print("Replace 'playAgain()' with 'Chooser()' from 'kstart03.py'")
    
    #playAgain = ''
    #while playAgain == 'yes' or playAgain == 'y':
    #print('Do you want to restart the IPS? (yes or no)')
    #go = raw_input('Do you want to restart the IPS? (yes or no)')
    #if go == "y":
        #print("Thanks")
    #else:
        #print("Bye!")
        #sleep(3)
        #break
       #return()

def End():
    #print("\033c")
    #print("End:")
    #print("----")
    print("")    
    print("\033c")
    print("")
    print("Thank you for your patronage!")
    sleep(2)
    print("")
    #raw_input("Press Enter twice to end program : ")
    #print("")
    print("\033c")    
    print("End of Program.")
    print("---------------")
    sleep(3)
    print("\033c")
    print("... 3")
    sleep(2)
    print("\033c")
    print("... 2")
    sleep(2)
    print("\033c")
    print("... 1")
    sleep(1)
    print("\033c")
    #return
    #print("")

def Main():
    print("\033c")
    playAgain()
    print("\033c")
    displayIntro()
    print("\033c")
    displaySearch()
    print("\033c")
    sleep(5)
    #accessCode()
    entrycode()
    print("\033c")
    instructions()
    print("\033c")
    askForInput()
    # goToAdventure()
    # caveNumber = chooseCave()
    # checkCave(caveNumber)
    End()
    
Main()    
