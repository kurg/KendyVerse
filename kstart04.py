# Kevin van Rensburg 2/21/2020
# Testing Startup Script version 0.04
# kstart04.py
# fixed def 9 Kendy Robot and cleaned up related def's

#import os
from time import sleep

def Intro():
    print("\033c")
    #print("Welcome to Program 1: ")
    #print("Program 1: Intro  ")
    #print("")
    print("Intro:")
    print("------")
    print("")
    print("Welcome to my universe!")
    print("I am Kendy.")
    print("My purpose is to serve and to obey.")
    print("")
    go=raw_input("Press any key to continue")
    Chooser();

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
    Chooser();
    
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
    print("Program 4: A.I. ")
    print("I am AI!")
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
    print("Program 6: Kendy")
    print("I am Kendy!")
    print("")
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
    print("Program 8: KendyVerse ")
    print("Welcome to the wonderful Kendy Universe!")
    print("")
    go=raw_input("Press any key to continue")
    #Chooser();
    #sleep(3)
    GoAgain()

def KendyRobot():
    print("\033c")
    print("Program 9: Kendy Robot")
    print("")
    print("Welcome, I am Kendy Robot!")
    print("Activating Startup Sequence.")
    print("----------------------------")
    print("")
    go=raw_input("Press any key to continue")
    # run program Kendy11.py
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
    print("Program 4: A.I. ")
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
    #print("Please choose a program")


def Chooser():
    print("\033c")
    print("Chooser:")
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
        print("You chose program ,",+choice)
        Program7();
    elif choice == 8:
        print("You chose program ,",+choice)
        Program8();
    elif choice == 9:
        print("You chose program ,",+choice)
        Program9();
    elif choice == 10:
        print("You chose program ,",+choice)
        Program10();
    else:
        print("\033c")
        print("Invalid choice")
        GoAgain()
	#go =  raw_input("Press Enter to continue...")
    #Menu();
    #GoAgain()
    #Chooser()
        
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
    It looks like this:
    
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
    11. Add more stuff here.....
    """)
    print("")
    go = raw_input("    Press Enter to continue...")
    print("\033c")
    #sleep(2)
    #print("")
    GoAgain()
        
def Main():
    
    #Test()
    #Intro()
    #ToDoList()
    #StartMenu()
    #MainEx()
    Chooser()
    #GoAgain()
    #End()


Main();
