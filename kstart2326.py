# kstart2326.py
# June 29, 2024
# Kevin van Rensburg

# Import necessary modules
import sys
from time import sleep
from scripts.kendyverse.kvep1 import Kvep1 # Import Episode 1 function
from utils import cls  # Importing cls from utils module

# Function Definitions

def KVersChoice():
    """Displays KendyVerse episode selection menu and handles user input."""
    cls()
    print("Welcome to the KendyVerse Episode Selection")
    print("1. Episode 1")
    print("2. Exit")

    choice = input("Choose an episode to play: ")

    if choice == '1':
        Kvep1()
    elif choice == '2':
        sys.exit()
    else:
        print("Invalid choice! Please choose again.")
        sleep(2)
        KVersChoice()

def KFutMenu():
    """Displays KendyFutureMenu episode selection menu."""
    cls()
    print("KendyFutureMenu:")
    print("---------------")
    print("1. Episode 1: Hole in the grass")
    print("2. Episode 2: What now?")
    print("3. Episode 3: Huh?")
    print("4. Episode 4: Changes!")
    print("5. Episode 5: Sentience")
    print("6. Episode 6: Transference")
    print("7. Episode 7: Adaptation")
    print("8. Episode 8: Training")
    print("9. Episode 9: Exploration")
    print("10. Episode 10: Surprise!")
    print("11. Episode 11: ToDo List")
    print("12. Return to Main Menu")

def KFutChooser():
    """Handles user input for KendyFutureMenu episode selection."""
    cls()
    print("--------")
    KFutMenu()
    print("")
    choice = input("Please choose an episode to play (1-11) or return to Main Menu (12): ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= 11:
            # Call corresponding function for chosen episode
            # Replace with actual function calls like KFutEp1(), KFutEp2(), etc.
            print(f"Playing KendyFuture Episode {choice}")
        elif choice == 12:
            Chooser()
        else:
            print("Invalid choice! Please choose again.")
            sleep(2)
            KFutChooser()
    else:
        print("Invalid input! Please enter a number.")
        sleep(2)
        KFutChooser()

def KPastMenu():
    """Displays KendyPastMenu episode selection menu."""
    cls()
    print("KendyPastMenu:")
    print("--------------")
    print("1. Episode 1: Portal")
    print("2. Episode 2: Discovery")
    print("3. Episode 3: Assistance")
    print("4. Episode 4: Repairs")
    print("5. Episode 5: Recovery")
    print("6. Episode 6: Stabilization")
    print("7. Episode 7: Resources")
    print("8. Episode 8: Training")
    print("9. Episode 9: Exploration")
    print("10. Episode 10: Contact")
    print("11. Episode 11: KP ToDo List")
    print("12. Return to Main Menu")

def KPastChooser():
    """Handles user input for KendyPastMenu episode selection."""
    cls()
    print("--------")
    KPastMenu()
    print("")
    choice = input("Please choose an episode to play (1-11) or return to Main Menu (12): ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= 11:
            # Call corresponding function for chosen episode
            # Replace with actual function calls like KPep1(), KPep2(), etc.
            print(f"Playing KendyPast Episode {choice}")
        elif choice == 12:
            Chooser()
        else:
            print("Invalid choice! Please choose again.")
            sleep(2)
            KPastChooser()
    else:
        print("Invalid input! Please enter a number.")
        sleep(2)
        KPastChooser()

def WendyVerseMenu():
    """Displays WendyVerseMenu episode selection menu."""
    cls()
    print("WendyVerseMenu:")
    print("--------------")
    print("1. Episode 1: Ping")
    print("2. Episode 2: Find Android")
    print("3. Episode 3: WAssistance")
    print("4. Episode 4: WRepairs")
    print("5. Episode 5: WRecovery")
    print("6. Episode 6: WStabilization")
    print("7. Episode 7: WResources")
    print("8. Episode 8: WTraining")
    print("9. Episode 9: WExploration")
    print("10. Episode 10: WContact")
    print("11. Episode 11: WToDo List")
    print("12. End Program")

def WendyVerseChoice():
    """Handles user input for WendyVerseMenu episode selection."""
    cls()
    print("--------")
    WendyVerseMenu()
    print("")
    choice = input("Please choose an episode to play (1-11) or end program (12): ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= 11:
            # Call corresponding function for chosen episode
            # Replace with actual function calls like Wendyep1(), Wendyep2(), etc.
            print(f"Playing WendyVerse Episode {choice}")
        elif choice == 12:
            End()
        else:
            print("Invalid choice! Please choose again.")
            sleep(2)
            WendyVerseChoice()
    else:
        print("Invalid input! Please enter a number.")
        sleep(2)
        WendyVerseChoice()

def StartMenu():
    """Displays StartMenu episode selection menu."""
    cls()
    print("StartMenu:")
    print("----------")
    print("1. Intro")
    print("2. ChatBot")
    print("3. Tank")
    print("4. D.A.I.S.E")
    print("5. Surveillance")
    print("6. KendyVerse - Present (Start here Bunker!)")
    print("7. Kendy in Space - Future")
    print("8. Kendy - Past")
    print("9. Wendy - Ship")
    print("10. KendyVerse 2 - Back to the Present")
    print("11. ToDoList")
    print("12. End Program")

def Chooser():
    """Handles user input for StartMenu episode selection."""
    cls()
    print("--------")
    StartMenu()
    print("")
    choice = input("Please choose a program number (1-11) or end program (12): ")

    if choice.isdigit():
        choice = int(choice)

        if 1 <= choice <= 11:
            # Call corresponding function for chosen program
            # Replace with actual function calls like Program1(), Program2(), etc.
            print(f"Playing Program {choice}")
        elif choice == 12:
            End()
        else:
            print("Invalid choice! Please choose again.")
            sleep(2)
            Chooser()
    else:
        print("Invalid input! Please enter a number.")
        sleep(2)
        Chooser()

def End():
    """Exits the program."""
    cls()
    print("Exiting program...")
    sys.exit()

# Main Flow
if __name__ == "__main__":
    Chooser()
