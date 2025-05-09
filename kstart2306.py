# Kevin van Rensburg 5/31/2022
# Copyright 2001
# Testing Kendy Startup Script version 23.06
# Changing version name to 23.06 
# kstart2306.py
# Added to and corrected scripts of kstart06.py, and relevant def's
# Testing ktart2306.py, and relevant def's

import sys
import os
import random
from time import sleep
import subprocess
import winsound

    
def Test():
    cls()
    print("")
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
    go=input("Press any key to continue")
    GoAgain()
    #Chooser();

def CopyRight():
    #cls()
    print("")
    print("Copyright - Kevin van Rensburg (2001)")
    print("")
    print("Kendy Robot, Kendy Android, KendyVerse, KendyVerse Games,  ")
    print("and Kendy & Wendy Games, were created by, and belong to, Kevin van Rensburg.")
    print("")
    go=input("Press any key to continue")
    #GoAgain()
    # -------- START THE REAL GAME HERE !!! -------   Kvep1()
    print("")
    Chooser()


def GoAgain():
    #cls()
    print("")
    #print("Return to Main Menu!")
    goAgain = input("Do you want to continue? Please enter y or n : ")
    # Put input test here
    if goAgain == "y":
        Chooser();
    else:
        End()
        #sys.exit()


def cls():
    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')


def End():
    cls()
    #print("End:")
    #print("----")
    print("")    
    print("")
    print("Thank you for your patronage!")
    sleep(2)
    print("")
    #input("Press Enter twice to end program : ")
    #print("")
    cls()
    print("")
    print("End of Program.")
    print("---------------")
    sleep(3)
    print("... 3")
    sleep(2)
    print("... 2")
    sleep(2)
    print("... 1")
    sleep(1)
    sys.exit()
    #return
    #print("")

def Continue():
    print("")
    Continue = input("Do you want to continue? Please enter y or n : ")
    # Put input test here
    if Continue == "y" or Continue == "Y":
        return;
    else:
        #stop()
        sys.exit()

def askForInput():
    print("")
    newInfo=str
    while newInfo != '1':
        print("")
        print('Please Enter Command.')
        newInfo = input(": ")
        print("")
        print ("",newInfo)
        return()
        print("")


def instructions():
   print("")
   cls()
   print("")
   print('DISCLAIMER: ')
   print("")
   print('Kendy or it\'s manufacturers and/or programmers ')
   print('are and will not be held responsible for any user faults.')
   sleep(5)
   print('Kendy or it\'s manufacturers and/or programmers')
   print('will not be held liable for any lawsuits due to malfunctions of any kind whatsoever!')
   sleep(10)
   cls()
   print("")
   print('SAFETY INSTRUCTIONS FOR OPERATING THIS UNIT TO FOLLOW!')
   print('-----------------------------------------------------')
   print("")
   sleep(5)
   cls()
   print("")
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

def entrycode():
    #code == 0
    cls()
    while True:
      try:  # Note: Python 2.x users should use input, the equivalent of 3.x's input
        code = int(input("Please enter your access code: "))
      except ValueError:
        print("Sorry, I didn't understand that.")
        #better try again... Return to the start of the loop
        continue
      else:
        #age was successfully parsed!
        #we're ready to exit the loop.
        print("Thank you, your code has been accepted.")
        return

def displayIntro():
    #print('Hello.')
    #sleep(2)
    cls()
    #print('Initializing - Please be patient.')
    sleep(4)
    cls()
    print("")
    print("I am Kendy the Robot / Android")
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
    cls()
    print("")
    print("Preparing files for Initialization...")
    print("")
    print(".")
    sleep(2)
    print("..")
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    cls()
    print("")
    print('Initializing StartUp Sequence...')
    print("..")
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    sleep(2)
    cls()
    print("")
    print('searching...')
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    sleep(2)
    cls()
    print("")
    print('Initiating Programming Sequence')
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    cls()
    print("")
    print('Initiating Diagnostics')
    sleep(2)
    print("...")
    sleep(1)
    print('....')
    cls()
    print("")
    print('searching...')
    sleep(2)
    print("...")
    sleep(2)
    print("....")
    sleep(2)
    print('....')
    cls()
    print("")
    print('Scanning ports...')
    sleep(2)
    print("...")
    sleep(2)
    print('....')



def Intro():
    cls()
    #print("Welcome to Program 1: ")
    print("Program 1: Intro  ")
    print("")
    print("Intro and Copyright:")
    print("--------------------")
    print("")
    print("Welcome! ")
    #go=input("Press any key to continue")
    CopyRight()
    #print("I am Kendy.")
    #print("My purpose is to serve and to obey.")
    #print("")
    #go=input("Press any key to continue")


def ChatBot():
    cls()
    print("")
    print("Program 2: ChatBot ")
    print("I am a chat bot!")
    print("")
    #print("So this script was called sucessfully from kstart20.py!!")
    print("making good progress so far!")
    print("I need to get the ChatBot program running")
    print("Hopefully I can do this in the December vacations :)")
    print("")
    go=input("Press any key to continue")
    #sleep(5)
    GoAgain()


def Tank():
    cls()
    print("")
    print("Program 3: Tank ")
    print("I am a tank!")
    print("")
    print("I am packing up the tank and taking it to Paraguay in April 2022!")
    print("")
    go=input("Press any key to continue")
    #Chooser();
    #sleep(3)
    GoAgain()
 
    
def AI():
    cls()
    print("")
    print("Program 4: D.A.I.S.E ")
    print("")
    print("I am DAISE! ")
    print("[Pronounced as Daisy]")
    print("(Digital Artificial Intelligent Sentient Entity)")
    print("")
    #sleep(3)
    go=input("Press any key to continue")
    #Chooser();
    GoAgain()


def Surveillance():
    cls()
    print("")
    print("Program 5: Surveillance ")
    print("I see you and I am watching you!")
    print("")
    #sleep(3)
    go=input("Press any key to continue")
    #Chooser();
    GoAgain()

def Kendy():
    cls()
    print("")
    print("Program 6: Kendy")
    print("")
    print("Hello, I am Kendy!")
    #print("")
    print("I am developing and evolving into the following :")
    print("")
    print(" A) A program which will eventully encapsulate a D.A.I.S.E")
    print("    [Pronounced as Daisy](Digital Artificial Intelligent Sentient Entity) core.")
    print(" B) A physical construct to house a D.A.I.S.E. core and all relevant components. ")
    print(" C) A physical Robot/Android containing the D.A.I.S.E. core and all relevant components. ")
    print("")
    print("NB::: TO ACCESS MY PROGRAM PLEASE OPEN THE FILE - Kendy1001.py")
    print("--------------------------------------------------------------")
    #sleep(2)
    go=input("Press any key to continue")
    #Chooser();
    #sleep(3)
    GoAgain()

def Adventure():
    cls()
    print("")
    print("Program 8: KendyVerse ")
    print("The Adventure begins.....")
    print("")
    print("")
    print("NB::: TO ACCESS MY PROGRAM PLEASE OPEN THE FILE - KendyVerse01.py")
    print("--------------------------------------------------------------")
    #print("Are you ready to enter the amazing adventure and gaming world")
    #print("- KendyVerse?")
    #print("")
    go=input("Press any key to continue")
    Continue()
    Chooser()


def KendyRobot():
    cls()
    print("Program 9: Kendy the Android Robot")
    print("")
    #print("OK now it is time to fix the next steps!!")
    print("")
    print("NB::: TO ACCESS MY PROGRAM PLEASE OPEN THE FILE - KendyDroid01.py")
    print("--------------------------------------------------------------")
    Continue()
    Chooser();
    cls()
    #print("robot in the room..find something to charge...any panels...?")
    #print("look for an input jack, hole, or battery...")
    print("")
    Continue()
    print("Welcome!")
    print("Activating Startup Sequence.")
    print("----------------------------")
    print("")
    displayIntro()
    cls()
    displaySearch()
    cls()
    sleep(5)
    #code()
    entrycode()
    cls()
    instructions()
    cls()
    askForInput()
    #Adventure()
    #GoAgain()
    print("")
    print("Thank you for visiting me.")
    #Chooser();
    #sleep(3)
    GoAgain()

def KendyVerse():
    cls()
    print("")
    #print("Program 8: KendyVerse ")
    print("Welcome to the wonderful Universe of Kendy the Android!")
    print("")
    print("Here you will enter the amazing adventure and gaming world - KendyVerse!")
    print("A Universe of many worlds, constructs, and entities,")
    print ("from earth, cyberspace, and the universe!")
    print("")
    go=input("Press any key to continue")
    Adventure()
    Chooser();
    #sleep(3)
    GoAgain()

def ToDoList():
    cls()
    print("")
    print("Program 10: ToDo List")
    print("")
    print("""  
    This is the To Do List!
    -----------------------
        
    1. Test kstart01.py through kstart20.py
    2. Add Intro and Copyright to kstart01.py through kstart20.py
    3. Pack up tank to take home in April 2022.
    4. Add new programs to GitHub -Dec 21. 
    5. Fix, update, and add info to GitHub Pages - Dec 21.
    6. Create and execute ChatBot and post to GitHub pages.
    7. Continue with Unity Tutorial Pathway
    8. Start Unity KendyVerse and develop Kendyverse Game.
    9. Find out how to integrate kstart20.py into Unity KendyVerse.
    10. Update this list for Dec 2021.
    11. Start Wendy Program!
    12. Add a done list :)
    13. more stuff here.....
    """)
    print("")
    go = input("    Press Enter to continue...")
    cls()
    #sleep(2)
    #print("")
    GoAgain()

def EnterName():
    cls()
    print("")
    print("CODENAME ")
    codename=input(":")
    if codename!= ("KEVIN VAN RENSBURG"):
        print("ACESS DENIED!")
        sleep(2)
        sys.exit()
    else:
        print("Thank you" ,codename)

def Direction():
    cls()
    print("")
    print("to turn left enter 'l' ..to turn right enter 'r'")
    direction=input(":")
    if direction==('l'):
        print("a passage")
        #print("ok,look to the right")
    else:
        print("a passage")


def Program1():
    print("")
    Intro()
    print("")

def Program2():
    print("")
    #subprocess.Popen("chatbot.py 1")
    #subprocess.run(["python", "chatbot.py'"]) # - did not work
    #import chatbot
    ChatBot()
    print("")
    
def Program3():
    print("")
    Tank()
    print("")
    
def Program4():
    print("")
    AI()
    print("")
    
def Program5():
    print("")
    Surveillance()
    print("")
    
def Program6():
    print("")
    Kendy()
    print("")
    sleep(2)
    #KyBot()
    print("")

def Program7():
    print("")
    Wendy()
    sleep(2)
    #KendyVerse()
    #KyVerse()
    print("")
    
def Program8():
    print("")
    KendyVerse()
    sleep(2)
    print("")
    
def Program9():
    print("")
    KendyRobot()
    sleep(2)
    print("") 
    
def Program10():
    print("")
    ToDoList()
    sleep(2)
    print("")


def StartMenu():
    cls()
    print("")
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
    print("Program 7: WendyVerse ")
    #print("")
    print("Program 8: KendyVerse ")
    #print("")
    print("Program 9: KendyDroid ")
    #print("")
    print("Program 10: ToDo List ")
    #print("End Program")
    print("Program 11: End Program ")
    #print("Please choose a program")


def Chooser():
    cls()
    #print("Chooser:")
    print("--------")
    StartMenu()
    print("")
    #choice = 0;
    #terminator = "n";
    choice = int(input("Please choose a program number from 1 - 10 and then press Enter: "))

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
    elif choice == 11:
        #print("You chose program ,",+choice)
        End();
    else:
        cls()
        print("")
        print("Invalid choice")
        sleep(2)
        End()
	#go =  input("Press Enter to continue...")
    #Menu();
    #GoAgain()
    #Chooser()



def Wendy():
    cls()
    print("")
    print("Program 7: Wendy")
    print("Hello, I am Wendy!")
    print("The Adventure begins in WendyVerse .....")
    print("")
    print("")
    print("NB::: TO ACCESS MY PROGRAM PLEASE OPEN THE FILE - Wendy01.py")
    print("--------------------------------------------------------------")
    print("")
    go=input("Press any key to continue")
    Chooser();
    #sleep(3)
    Wendyep1()

def MainEx():
    cls()
    print("")
    #print("")
    print("""  
    This is the Main function!
    ----------------------------
    It looks like this:
    
    Test();
    Intro();
    -----
    """)
    print("")
    sleep(5)
    Continue()
    #go = input("    Press Enter to continue...")
    #Test()
    Intro()
    #ToDoList()
    #StartMenu()
    #MainEx()
    #GoAgain()
    Chooser()
    #End()
    #cls()
    #sleep(2)
    #print("")
    #Chooser()
    
        
def Main():

    #Beep()
    #Test()
    Intro()
    #ToDoList()
    #StartMenu()
    #Chooser()
    #MainEx()
    #GoAgain()
    #End()


Main();
