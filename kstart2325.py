# kstart2325.py
# Kevin van Rensburg
# 29 June 2024
# fixing def Chooser and other things

import sys
import os
from time import sleep

# Assuming cls() clears the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Define your programs here

def Intro():
    cls()
    print("Program 1: Intro")
    print("")
    print("Intro and Copyright:")
    print("--------------------")
    print("")
    print("Welcome!")
    print("Copyright - Kevin van Rensburg (2001)")
    print("")
    input("Press Enter to continue...")
    Chooser()

def ChatBot():
    cls()
    print("")
    print("Program 2: ChatBot")
    print("I am a chat bot!")
    print("")
    
    while True:
        print("What would you like to do?")
        print("1. Say hello")
        print("2. Tell a joke")
        print("3. Exit ChatBot")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print("Hello there!")
        elif choice == '2':
            print("Why don't scientists trust atoms? Because they make up everything!")
        elif choice == '3':
            print("Exiting ChatBot.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")
        
        input("Press Enter to continue...")

def Tank():
    cls()
    print("")
    print("Program 3: Tank")
    print("I am a tank!")
    print("")
    input("Press Enter to continue...")
    Chooser()

def AI():
    cls()
    print("")
    print("Program 4: D.A.I.S.E")
    print("I am DAISE! [Pronounced as Daisy]")
    print("(Digital Artificial Intelligent Sentient Entity)")
    print("")
    input("Press Enter to continue...")
    Chooser()

def Surveillance():
    cls()
    print("")
    print("Program 5: Surveillance")
    print("I see you and I am watching you!")
    print("")
    input("Press Enter to continue...")
    Chooser()

def KendyVerse():
    cls()
    print("")
    print("Program 6: KendyVerse")
    print("Welcome to the wonderful Universe of Kendy the Android!")
    print("Here you will enter the amazing adventure and gaming world - KendyVerse!")
    print("A Universe of many worlds, constructs, and entities, from earth, cyberspace, and the universe!")
    print("")
    input("Press Enter to continue...")
    Chooser()

def KendyInSpace():
    cls()
    print("")
    print("Program 7: Kendy in Space")
    print("")
    input("Press Enter to continue...")
    Chooser()

def KendyPast():
    cls()
    print("")
    print("Program 8: Kendy Past")
    print("")
    input("Press Enter to continue...")
    Chooser()

def Wendy():
    cls()
    print("")
    print("Program 9: Wendy")
    print("Hello, I am Wendy!")
    print("The Adventure begins in WendyVerse .....")
    print("")
    input("Press Enter to continue...")
    Chooser()

def KendyVerse2():
    cls()
    print("")
    print("Program 10: KendyVerse2 - Back to the Present")
    print("")
    input("Press Enter to continue...")
    Chooser()

def ToDoList():
    cls()
    print("")
    print("Program 11: ToDo List")
    print("""
    This is the To Do List!
    -----------------------
        
    1. Change #chooser items 6 and 9
    2. Add Intro and Copyright to kstart01.py through kstart20.py
    3. Start adding programs and files to Kstart2310.py.
    4. Add more stuff here.....
    """)
    input("Press Enter to continue...")
    cls()
    Chooser()

def End():
    print("Ending program...")
    sys.exit()

# Main Menu Programs
def StartMenu():
    cls()
    print("")
    print("StartMenu:")
    print("---------")
    print("")
    print("Program 1: Intro")
    print("Program 2: ChatBot")
    print("Program 3: Tank")
    print("Program 4: D.A.I.S.E")
    print("Program 5: Surveillance")
    print("Program 6: KendyVerse - Present (Start here Bunker!)")
    print("Program 7: Kendy in Space - Future")
    print("Program 8: Kendy - Past")
    print("Program 9: Wendy - Ship")
    print("Program 10: KendyVerse 2 - Back to the Present")
    print("Program 11: ToDoList")
    print("Program 12: End Program")

def Chooser():
    while True:
        StartMenu()
        choice = input("Please choose a program number from 1 - 12 and then press Enter: ")

        if choice == '1':
            Intro()
        elif choice == '2':
            ChatBot()
        elif choice == '3':
            Tank()
        elif choice == '4':
            AI()
        elif choice == '5':
            Surveillance()
        elif choice == '6':
            KendyVerse()
        elif choice == '7':
            KendyInSpace()
        elif choice == '8':
            KendyPast()
        elif choice == '9':
            Wendy()
        elif choice == '10':
            KendyVerse2()
        elif choice == '11':
            ToDoList()
        elif choice == '12':
            End()
        else:
            cls()
            print("")
            print("Invalid choice")
            sleep(2)

def Main():
    Chooser()

if __name__ == "__main__":
    Main()
