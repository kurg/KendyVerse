# Kevin van Rensburg 29/10/2021
# Copyright 2001
# Testing Startup Script version 0.06
# kstart05.py
# Working on def KendyRobot()and clean up all related def's
# Decided to make def KendyRobot() instead of importing kendy12.py into this script.
# updated the following def's : Main(), Intro(), CopyRight(), Kendy(), KendyVerse(), KendyRobot(), Chooser()
# created the following def's Adventure(), Continue()


import sys

#import os
import random
from time import sleep

#import Kendy11.py

#kendy11.myfunc()

def Intro():
    print("\033c")
    #print("Welcome to Program 1: ")
    #print("Program 1: Intro  ")
    #print("")
    print("Intro:")
    print("------")
    print("")
    print("Welcome! ")
    CopyRight()
    #print("I am Kendy.")
    #print("My purpose is to serve and to obey.")
    print("")
    go=raw_input("Press any key to continue")
    

def Test():
    print("\033c")
    print("Test:")
    print("-----")
    #print("")
    print("")
    print("------------------------------")
    print("")
    print("This is the test startup script.")
    print("")
    print("Hello, welcome to my universe!")
    print("")
    print("------------------------------")
    print("")
    print("Add all relevant programming here...")
    print("")
    go=raw_input("Press any key to continue")
    GoAgain()
    #Chooser();

def CopyRight():
    print("Copyright Info Here [...].")
    print("")
    go=raw_input("Press any key to continue")
    GoAgain()
    
def Program1():
    Intro()
    print("")

def Program2():
    ChatBot();
    print("")
    
def Program3():
    Tank()
    print("")
    
def Program4():
    AI()
    print("")
    
def Program5():
    Surveillance()
    print("")
    
def Program6():
    Kendy()
    print("")
    sleep(2)
    #KyBot()
    print("")
    

def Program7():
    Wendy()
    sleep(2)
    #KendyVerse()
    #KyVerse()
    print("")
    
def Program8():
    KendyVerse()
    sleep(2)
    print("")
    
def Program9():
    KendyRobot()
    sleep(2)
    print("") 
    
def Program10():
    ToDoList()
    sleep(2)
    print("")

def Adventure():
    print("\033c")
    #print("Program 8: KendyVerse ")
    print("The Adventure begins.....")
    print("")
    print("Are you ready to enter the amazing adventure and gaming world - KendyVerse?")
    print("")
    #go=raw_input("Press any key to continue")
    Continue()
    name=raw_input("WHO ARE YOU???")
    #print("HELLO ",name, "WHAT DO YOU WANT?")
    print("HELLO "),name
    want=raw_input("WHAT DO YOU WANT???")
    print("WHY DO YOU WANT "),want
    print("")
    print("Considering options..")
    sleep(2)
    print("")
    print("OK, THAT'S ENOUGH!")
    print("")
    #Chooser();
    #sleep(3)
    GoAgain()

def ChatBot():
    print("\033c")
    print("Program 2: ChatBot ")
    print("I am a chat bot!")
    print("")
    go=raw_input("Press any key to continue")
    #sleep(5)
    GoAgain()
    
def Tank():
    print("\033c")
    print("Program 3: Tank ")
    print("I am a tank!")
    print("")
    go=raw_input("Press any key to continue")
    #Chooser();
    #sleep(3)
    GoAgain()
 
    
def AI():
    print("\033c")
    print("Program 4: D.A.I.S.E ")
    print("I am DAISE!")
    print("")
    #sleep(3)
    go=raw_input("Press any key to continue")
    #Chooser();
    GoAgain()
    
def Surveillance():
    print("\033c")
    print("Program 5: Surveillance ")
    print("I see you and I am watching you!")
    print("")
    #sleep(3)
    go=raw_input("Press any key to continue")
    #Chooser();
    GoAgain()

def Kendy():
    print("\033c")
    #print("Program 6: Kendy")
    print("Hello, I am Kendy!")
    #print("")
    print("I am developing and evolving into the following :")
    print("")
    print(" A) A program which will eventully encapsulate a D.A.I.S.E [Pronounced as Daisy](Digital Artificial Intelligent Sentient Entity) core.")
    print(" B) A physical construct to house a D.A.I.S.E. core and all relevant components. ")
    print(" C) A physical Robot/Android containing the D.A.I.S.E. core and all relevant components. ")
    print("")
    sleep(2)
    go=raw_input("Press any key to continue")
    #Chooser();
    #sleep(3)
    GoAgain()
    
def Wendy():
    print("\033c")
    print("Program 7: Wendy")
    print("I am Wendy!")
    print("")
    go=raw_input("Press any key to continue")
    #Chooser();
    #sleep(3)
    GoAgain()

def KendyVerse():
    print("\033c")
    #print("Program 8: KendyVerse ")
    print("Welcome to the wonderful Universe of Kendy the Android!")
    print("")
    print("Here you will enter the amazing adventure and gaming world - KendyVerse!")
    print("A Universe of many entities from earth, cyberspace, and the universe!")
    print("")
    go=raw_input("Press any key to continue")
    Adventure()
    #Chooser();
    #sleep(3)
    GoAgain()

def KendyRobot():
    print("\033c")
    #print("Program 9: Kendy Robot")
    print("")
    print("Welcome!")
    print("")
    print("Activating Startup Sequence.")
    print("----------------------------")
    print("")
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
    Adventure()
    #GoAgain()
    print("")
    print("Thank you for visiting me.")
    #Chooser();
    #sleep(3)
    GoAgain()

def StartMenu():
    print("\033c")
    print("StartMenu:")
    print("---------")
    print("")
    print("Program 1: Intro  ")
    #print("")
    print("Program 2: ChatBot ")
    #print("")
    print("Program 3: Tank ")
    #print("")
    print("Program 4: D.A.I.S.E ")
    #print("")
    print("Program 5: Surveillance ")
    #print("")
    print("Program 6: Kendy ")
    #print("")
    print("Program 7: Wendy ")
    #print("")
    print("Program 8: KendyVerse ")
    #print("")
    print("Program 9: Kendy Robot ")
    #print("")
    print("Program 10: ToDo List ")
    #print("End Program")
    #print("Please choose a program")


def Chooser():
    print("\033c")
    #print("Chooser:")
    print("--------")
    StartMenu()
    print("")
    #choice = 0;
    #terminator = "n";
    choice = int(raw_input("Please choose a program number from 1 - 10 and then press Enter: "))

    # Put input test here!

    if choice == 1:
        #print("You chose program ",choice)
        Program1();
    elif choice == 2:
        #print("You chose program ",choice)
        Program2()
    elif choice == 3:
        #print("You chose program ,",+choice)
        Program3();
    elif choice == 4:
        #print("You chose program ,",+choice)
        Program4()
    elif choice == 5:
        #print("You chose program ,",+choice)
        Program5();
    elif choice == 6:
        #print("You chose program ,",+choice)
        Program6();
    elif choice == 7:
        #print("You chose program ,",+choice)
        Program7();
    elif choice == 8:
        #print("You chose program ,",+choice)
        Program8();
    elif choice == 9:
        #print("You chose program ,",+choice)
        Program9();
    elif choice == 10:
        #print("You chose program ,",+choice)
        Program10();
    else:
        print("\033c")
        print("Invalid choice")
        GoAgain()
	#go =  raw_input("Press Enter to continue...")
    #Menu();
    #GoAgain()
    #Chooser()

def displayIntro():
    #print('Hello.')
    #sleep(2)
    #print("\033c")
    #print('Initializing - Please be patient.')
    sleep(4)
    print("\033c")
    print("I am Kendy the Robot")
    print('Welcome to my Universe.')
    sleep(8)
    #print('I am evolving into a Robot with a DAISE (Digital Artificial Intelligent Sentient Entity) core!')
    print(".")
    sleep(2)
    print("..")
    sleep(2)
    print("...")
    sleep(2)

def displaySearch():
    print("\033c")
    print("Preparing files for Initialization...")
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
    print('Initiating Programming Sequence')
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
    """code=int(raw_input) ""
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
   
#def playAgain():
    
    #print("Replace 'playAgain()' with 'Chooser()' from 'kstart03.py'")
    
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

def Continue():
    print("\033c")
    print("Return to Main Menu!")
    Continue = raw_input("Do you want to continue? Please enter y or n : ")
    # Put input test here

    if Continue == "y":
        return;
    else:
        break
    #stop()
    #sys.exit()
    
   
def GoAgain():
    print("\033c")
    print("Return to Main Menu!")
    goAgain = raw_input("Do you want to continue? Please enter y or n : ")

    # Put input test here

    if goAgain == "y":
        Chooser();
    else:
        End();
    
def MainEx():
    print("\033c")
    #print("")
    print("""  
    This is the Main function!
    ----------------------------
    It looks like this:
    
    Test();
    Intro();
    ToDoList();
    StartMenu();
    Chooser();
    End();
    ---
    """)
    print("")
    #go = raw_input("    Press Enter to continue...")
    #print("\033c")
    sleep(2)
    #print("")
    Chooser()
    
def ToDoList():
    print("\033c")
    print("")
    print("""  
    This is the To Do List!
    -----------------------
        
    1. Test kendy07-11.py,kstart01 through 3.py - DONE 3/29/2020
    2. Start using Adeept to program and test breadboards.
    3. Activate tank an test motors.
    4. Start building gripper arm.
    5. Test lights and sensors
    6. Add programs to GitHub. - DONE 3/29/2020 
    7. Fix and add info to GitHub Pages. DONE 3/29/2020
    8. Add this list to GitHub pages. 
    9. Add Github Pages to Kybot (Tank).
    10. Test and improve this program and add versions and headings.
    11. Update this list.
    12. Add more stuff here.....
    """)
    print("")
    go = raw_input("    Press Enter to continue...")
    print("\033c")
    #sleep(2)
    #print("")
    GoAgain()
        
def Main():

    #Test()
    Chooser()
    #Intro()
    #ToDoList()
    #StartMenu()
    #MainEx()
    #GoAgain()
    #End()


Main();
