# Kevin van Rensburg 2/21/2020
# Testing Startup Script version 0.001
# kstart.py

#import os
from time import sleep

def Intro():
    print("\033c")
    print("Welcome to Program 1: ")
    print("Program 1: Intro  ")
    print("")
    print("Intro:")
    print("------")
    print("")
    print("Welcome to my universe!")
    print("I am KyBot the sibling of Kendy.")
    print("My purpose is to serve and to please.")
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
    KyBot()
    sleep(2)
    #KendyVerse()
    #KyVerse()
    print("")
    
def Program8():
    KendyVerse()
    sleep(2)
    print("")
    
def Program9():
    KyBotVerse()
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
    
def KyBot():
    print("\033c")
    print("Program 7: KyBot")
    print("I am KyBot!")
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

def KyBotVerse():
    print("\033c")
    print("Program 9: KyBotVerse ")
    print("Welcome to the wonderful KyBotUniverse!")
    print("")
    go=raw_input("Press any key to continue")
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
    print("Program 7: KyBot ")
    #print("")
    print("Program 8: KendyVerse ")
    #print("")
    print("Program 9: KyVerse ")
    #print("")
    #print("Please choose a program")


def Chooser():
    print("\033c")
    print("Chooser:")
    print("--------")
    StartMenu()
    print("")
    #choice = 0;
    #terminator = "n";
    choice = int(input("Please choose a program number from 1 - 7 and then press Enter: "))
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
    else:
        print("\033c")
        print("Invalid choice")
        GoAgain()
	#go =  raw_input("Press Enter to continue...")
    #Menu();
    #GoAgain()
    #Chooser()
        
def End():
    print("\033c")
    print("End:")
    print("----")
    print("")    
    print("\033c")
    print("")
    print("Thank you for your patronage!");
    print("");
    raw_input("Press Enter twice to end program : ")
    print("")
    print("\033c")    
    print("End of Program.");
    print("---------------")
    #return
    #print("")
    
   
def GoAgain():
    print("\033c")
    print("This is the menu we all return to!")
    goAgain = raw_input("Do you want to go again? : ")
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
        
def Main():
    
    #Test()
    #Intro()
    #StartMenu()
    #MainEx()
    Chooser()
    #GoAgain()
    End()


Main();
