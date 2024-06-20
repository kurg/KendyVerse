# Kevin van Rensburg 8/6/2022
# Copyright 2001
# Testing Kendy Startup Script version 23.11
# Changing version name to 23.11 
# kstart2311.py
# rearranged scripts to enable continuity.
# arranged order of Manin Menu script Chooser()
# swapped, cleaned, and fixed Chooser() Programs 1 to Program 12
# Testing and cleaning up scripts and relevant def's

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

def CopyRight():
    #cls()
    print("")
    print("Copyright - Kevin van Rensburg (2001)")
    print("")
    print("Kendy Robot, Kendy Android, KendyVerse, KendyVerse Games,  ")
    print("and Kendy & Wendy Games, were created by, and belong to, Kevin van Rensburg.")
    print("")
    go=input("Press any key to continue")
    print("")
    Chooser()

def GoAgain():
    print("")
    goAgain = input("Do you want to continue? Please enter y or n : ")
    # Put input choice test here
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
    print("")    
    print("")
    print("Thank you for your patronage!")
    sleep(2)
    print("")
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
    cls()
    sleep(4)
    cls()
    print("")
    print("I am Kendy the Robot / Android")
    print('Welcome to my Universe.')
    sleep(8)
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

#   Main Menu Programs start here -------------------------------------------------------------------------------------------------------------------

    #Program 1: Intro
    #Program 2: ChatBot
    #Program 3: Tank
    #Program 4: D.A.I.S.E
    #Program 5: Surveillance
    #Program 6: KendyVerse - Present (Start here Bunker!)
    #Program 7: Kendy in Space - Future
    #Program 8: Kendy - Past
    #Program 9: Wendy - Ship
    #Program 10: KendyVerse 2 - Back to the Present
    #Program 11: ToDoList
    #Program 12: End Program

def Program1():
    print("")
    Intro()
    print("")
def Program2():
    print("")
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
    KendyVerse()
    print("")
def Program7():
    print("")
    KendyInSpace()
    print("")
def Program8():
    print("")
    KendyPast()
    sleep(2)
    print("")
def Program9():
    print("")
    Wendy()
    sleep(2)
    print("")
def Program10():
    print("")
    KendyVerse2()
    ToDoList()
    sleep(2)
    print("")
def Program11():
    print("")
    ToDoList()
    sleep(2)
    print("")

def Intro():
    cls()
    print("Program 1: Intro  ")
    print("")
    print("Intro and Copyright:")
    print("--------------------")
    print("")
    print("Welcome! ")
    CopyRight()

def ChatBot():
    cls()
    print("")
    print("Program 2: ChatBot ")
    print("I am a chat bot!")
    print("")
    print("making good progress so far!")
    print("I need to get the ChatBot program running")
    print("Hopefully I can do this in the December vacations :)")
    print("")
    go=input("Press any key to continue")
    Chooser()

def Tank():
    cls()
    print("")
    print("Program 3: Tank ")
    print("I am a tank!")
    print("")
    print("I am packing up the tank and taking it to Paraguay in April 2022!")
    print("")
    go=input("Press any key to continue")
    Chooser();
    
def AI():
    cls()
    print("")
    print("Program 4: D.A.I.S.E ")
    print("")
    print("I am DAISE! ")
    print("[Pronounced as Daisy]")
    print("(Digital Artificial Intelligent Sentient Entity)")
    print("")
    go=input("Press any key to continue")
    Chooser();

def Surveillance():
    cls()
    print("")
    print("Program 5: Surveillance ")
    print("I see you and I am watching you!")
    print("")
    go=input("Press any key to continue")
    Chooser();

def KendyVerse():
    cls()
    print("")
    print("Program 6: KendyVerse ")
    print("Welcome to the wonderful Universe of Kendy the Android!")
    print("")
    print("Here you will enter the amazing adventure and gaming world - KendyVerse!")
    print("A Universe of many worlds, constructs, and entities,")
    print ("from earth, cyberspace, and the universe!")
    print("")
    print("NB::: TO ACCESS MY PROGRAM SCRIPT PLEASE OPEN THE FILE - KendyVerse01.py")
    print("--------------------------------------------------------------------------")
    print("")
    go=input("Press any key to continue")
    KVersChoice()

def KendyInSpace():
    cls()
    print("")
    print("Program 7: Kendy in Space")
    print("")
    print("NB::: TO ACCESS MY PROGRAM SCRIPT PLEASE OPEN THE FILE - KendyInSpace01.py")
    print("--------------------------------------------------------------------------")
    KFutChooser()

def KendyPast():
    cls()
    print("")
    print("Program 8: Kendy Past")
    print("")
    print("NB::: TO ACCESS MY PROGRAM SCRIPT PLEASE OPEN THE FILE - KendyPast04.py")
    print("-----------------------------------------------------------------------")
    go=input("Press any key to continue")
    KPastChooser();

def Wendy():
    cls()
    print("")
    print("Program 9: Wendy")
    print("Hello, I am Wendy!")
    print("The Adventure begins in WendyVerse .....")
    print("")
    print("")
    print("")
    print("NB::: TO ACCESS MY PROGRAM SCRIPT PLEASE OPEN THE FILE - Wendy01.py")
    print("-------------------------------------------------------------------")
    Continue()
    WendyVerseChoice()

def KendyVerse2():
    cls()
    print("")
    print("Program 10: KendyVerse2 - Back to the Present")
    print("")
    print("NB::: TO ACCESS MY PROGRAM SCRIPT PLEASE OPEN THE FILE - KendyVerse2001.py")
    print("--------------------------------------------------------------------------")
    print(" KendyVerse2Chooser  (Still have to make this!!)")
    print("")
    Continue()
    cls()
    Chooser()
    
def ToDoList():
    cls()
    print("")
    print("Program 11: ToDo List")
    print("")
    print("""  
    This is the To Do List!
    -----------------------
        
    1. Change #chooser items 6 and 9
    2. Add Intro and Copyright to kstart01.py through kstart20.py
    3. Start adding programs and files to Kstart2310.py.
    4. Add more stuff here.....
    """)
    print("")
    go = input("Press Enter to continue...")
    cls()
    Chooser()

#   Main Menu Programs End here ------------------------------------------------------------------------------------------------------------------------

def EnterCodeName():
    cls()
    print("")
    print("CODENAME ")
    codename=input(":")
    if codename!= ("KENDYVERSE"):
        print("ACESS DENIED!")
        sleep(2)
        sys.exit()
    else:
        print("CODENAME ACCEPTED: " ,codename)

def Direction():
    cls()
    print("")
    print("to turn left enter 'l' ..to turn right enter 'r'")
    direction=input(":")
    if direction==('l'):
        print("a passage")
        print("ok,now look to the right")
        sleep(4)
    else:
        print("a passage")

def ALL():
    cls()
    print("")
    print("ACCESS LEVELS LIST")
    print("------------------")
    print("")
    print("AL-1A - HIGHEST LEVEL UNIVERSAL")
    print("AL-1B - SECOND LEVEL UNIVERSAL")
    print("AL-1C - THIRD LEVEL UNIVERSAL")
    print("AL-1D - FOURTH LEVEL UNIVERSAL")
    print("AL-1E - FIFTH LEVEL UNIVERSAL")
    print("AL-2A - HIGHEST LEVEL LOCAL")
    print("AL-2B - SECOND LEVEL LOCAL")
    print("AL-2C - THIRD LEVEL LOCAL")
    print("AL-2D - FOURTH LEVEL LOCAL")
    print("AL-2E - FIFTH LEVEL LOCAL")
    print("AL-3A - FIRST SUB LEVEL LOCAL ")
    print("AL-3B - SECOND SUB LEVEL LOCAL")
    print("AL-3C - THIRD SUB LEVEL LOCAL")
    print("AL-3D - FOURTH SUB LEVEL LOCAL")
    print("AL-3E - FIFTH SUB LEVEL LOCAL")
    print("")
    sleep(8)

def ALI():
    cls()
    print("")
    print("ENTER COMMAND")
    alicode=input(":")
    if alicode==("COMMANDER KEVIN VAN RENSBURG KVR145759 ALCODE"):
        print("KEVINVR-ACCESS LEVEL AL-1A")
        print("KENDY-ACCESS LEVEL AL-1E")
        print("CAPTAIN-ACCESS LEVEL TBD")
        print("COMMANDING OFFICER-ACCESS LEVEL TBD")
        print("PILOT-ACCESS LEVEL TBD")
        print("NAVIGATION-ACCESS LEVEL TBD")
        print("SCANNING-ACCESS LEVEL TBD")
        print("WEAPONS-ACCESS LEVEL TBD")
        sleep(8)
    elif alicode==("KENDY"):
        print("ACCESS LEVEL AL-1E")
        sleep(5)    
    elif alicode==("CAPTAIN"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("COMMANDING OFFICER"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("PILOT"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("NAVIGATION"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("SCANNING"):   
        print("ACCESS LEVEL TBD")
        sleep(5)
    elif alicode==("WEAPONS"):
        print("ACCESS LEVEL TBD")
        sleep(5)
    else:
        print("ACCESS DENIED")
        sleep(4)
        sys.exit()

def core():
    cls()
    print("")
    print("KENDY - CORE LEVEL AUTHORIZED")
    print("COMMANDER KEVIN VAN RENSBURG - CORE ACCESS AUTHORIZED")
    print("")
    sleep(6)

def cipl():
    cls()
    print("")
    print("PLEASE ENTER ACCESS CODE")
    acccode=input(":")
    if acccode==("KVR145759"):
        core()
    else:
        print("ACCESS DENIED")
        sleep(4)
        sys.exit()  

def COMCODE():
    cls()
    print("")
    print("ACQUIRING RESOURCES ")
    print("-------------------")
    print("")
    print("Instructions for acquiring resources")
    print("------------------------------------")
    print("")
    print("Station Commander can access resources by entering the following commands:")
    print("")
    print("Core INI Protocols - Local")
    print("Robotic INI Protocols - Local")
    print("Weapons and Accesories INI Protocols - Local")
    print("Universal Protocols INI *Access Level 1A only*")
    print("ACCESS Levels List *Access Levels 2E-1A*")
    print("ACCESS Level Indicator - Enter Position, Name, Code, ALI=COMMAND")
    print("")
    Continue()    
    print("")
    print("PLEASE ENTER COMMAND CODE")
    comcode=input(":")
    if comcode==("CIPL"):
        print("CORE PROTOCOLS INITIALIZED")
        cipl()
        sleep(5)
    elif comcode==("RIPL"):
        print("Robotic Protocols Initialized")
        sleep(5)
    elif comcode==("WAIPL"):
        print("Weapons Protocols Initialized")
        sleep(5)
    elif comcode==("UPI"):
        print("Universal Protocols Initilized")
        sleep(5)
    elif comcode==("ALL"):
        ALL()
    elif comcode==("ALI"):   
        ALI()
    elif comcode==("MORE"):
        AnotherCode()
    else:
        print("ACCESS DENIED")
        sys.exit()

def AnotherCode():
    print("")
    print("Do you need to enter a new code??")
    acode = input(": ")
    if acode == "y":
        COMCODE()
    else:
        print("Thank you!")


def Kvep1():
    cls()
    print("")
    print("Welcome to KendyVerse ")
    print("")
    print(" IMPORTANT INSTRUCTIONS!!")
    print(" ------------------------")
    print("")
    print(" At certain points you will be asked whether you want to continue playing.")
    print("")
    print(" To continue playing please press y and then press the enter key! ")
    print(" To discontinue playing please press n and then press the enter key!")
    print("")
    Continue()
    cls()
    print("The Story starts here.....")
    print("")
    print("Episode 1: Lost")
    print("")
    print("HELLO! WHO ARE YOU???")
    name=input(":")
    print("Hello" ,name)
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("BANG!!..SHUDDER...")
    print("What?? Stuck..can't move..")
    print("Where am I?? ...falling...falling....THWUMP!!")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("DARK..remember??? Yes...")
    print("OK..think..remember..I was falling..Stuck to something")
    print("Yes.. In a Plane..noises..now it's quiet")
    print("")
    print("Opening my eyes slowly..it's night..still strapped into seat")
    print("must have blacked out..look around slowly..no headache")
    print("")
    go=input("Press any key to continue")
    print("test fingers..ok..")
    print("toes..ok..")
    print("move feet..OK..")
    print("move..hands..ok..")
    print("nothing hurts..")
    print("turn head slowly.. ")
    print("")
    print(" To continue playing please press y and then press the enter key! ")
    print(" To discontinue playing please press n and then press the enter key!")
    print("")
    Continue()
    cls()
    print("")
    print("to look left enter 'l' ..to look right enter 'r'")
    direction=input(":")
    if direction==('l'):
        print("snow... and trees ..high up..")
        print("ok,looking to the right")
    else:
        print("a person...who...")
    print("")
    go=input("Press any key to continue")
    print("OH..my friend..remembering..I remember now ...We were going home")
    print("you undo the seatbelt and slowly climb out of the seat.")
    print("you stretch and turn ..everything seems ok.")
    print("")
    go=input("Press any key to continue")
    print("you look at your friend and she is unconcious!")
    print("")
    print("What do I do??..find help!!")
    print("you look around and see that you are in a deep ditch")
    print("You undo your friend's seatbelt and lift her out of the seat.")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("what now? Time to think.")
    print("What do I have?..what can I use?")
    go=input("Press any key to continue")
    print("")
    print("Items- seats, cushions, floatation devices under seats, friend's jacket, my belt")
    print("wallet,cellphone, charger in pocket,")
    print("check cellphone..no signal, battery at 68%")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("ok, piggy back my friend..")
    print("get flotation devices.. put her arms around my neck")
    print("tie her hands in front of me with flotation device...")
    print("same with her legs.. ok stand up")
    print("you stand up slowly with a grunt! you look at the seats and try to pull them")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("SCREECH!! What is that sound.. something metal under the seat.")
    print("you pull the seat some more and the screeching sound stops.")
    print("What is that? it looks like a hatch or round metal door")
    print("you clear away the snow..there is a wheel type handle")
    print("you try turn the handle..it's stuck")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("use a seat leg!....")
    print("you push the corner of the seat leg into the wheel and push")
    print("SCREECH..Creak, it slowly starts to turn..then it is loose")
    print("it's hard to bend down while piggybacking your friend..no matter...")
    print("you go down on your knees very slowly and push the seat away")
    print("")
    go=input("Press any key to continue")
    print("you turn the wheel type handle and it turns a few times...")
    print("you try to lift the hatch,it moves a little")
    print("you use all your strength to lift the door...it creaks open")
    print("you open it up and swing it over... you look down into the dark hole")
    print("")
    go=input("Press any key to continue")
    print("you see a dark tunnel going down with a ladder on one side.")
    print("You look around and make sure you have her jacket and everything else.")
    print("very slowly you crawl over to the side where you see the ladder")
    print("you look down and grab the top rung of the ladder")
    print("Is there enough space for both of us as I climb down?")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("you pull yourself across to the ladder and swing your left leg down.")
    print("Ugghh.. now the right leg..ok I can feel the rung with my foot.")
    print("getting another foothold..yes, it's ok")
    print("will the ladder hold?...CRREAAK .. yes, it's creaking but holding")
    print("")
    go=input("Press any key to continue")
    print("you carefully go down the ladder..step by step into the darkness below.")
    print("oh, I'm tired. need to rest...you hold onto the ladder and stop climbing down for a few minutes.")
    print("gotta go, hungry and thirsty..")
    print("you continue your slow descent... CLANG!!! a loud noise above you..")
    print("the light has gone..the hatch must have closed.... it's all dark now")
    print("")
    go=input("Press any key to continue")
    print("OH,,cant feel another rung.. move down a little...feels like a floor..")
    print("so dark..climb down ..both feet on the floor now..")
    print("what is this??..where are we??")
    print("walls feel smooth..cold..metal..floor?? bend down slowly and feel the floor")
    print("metal floor..UUGHH stand up..feel for cellphone..")
    print("")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("open cellphone..AH, some light.. its a tunnel .. moving forward")
    print("you walk down the tunnel for about 100 metres and see another door")
    print("the door looks like a hatch with a wheel on it")
    print("you turn the wheel, it is easier to turn than the entrance hatch.")
    print("you open the door and walk in ... its slightly warmer here.. close the door behind you")
    print("you turn the wheel until it stops...")
    print("you see a passage and walk along the passage. There are rooms ahead to the left and right.")
    print("you look in the first room and see what looks like a soldiers quarters..")
    print("single bed, closet, washbasin..")
    print("you sit on the bed and loosen the flotation devices")
    print("you lift the blanket and place her carefully on the bed")
    print("")
    go=input("Press any key to continue")
    print("you look around the room and see a pillow and blanket on the bed")
    print("you look in the closet and see another blanket and...")
    print("a set of flightsuits with strange looking helmets")
    print("the washbasin has a cabinet under it.. you open the cabinet")
    print("")
    Continue()
    cls()
    print("")
    print("there is a candle, candleholder, matches, toothbrush...")
    print("soap and a small towel there")
    print("you take everything and go down the passage to explore")
    print("there are 3 small rooms and 2 larger ones on each side of the passageway.")
    print("you look into one of the large rooms..")
    print("they have bigger closets and a desk ...")
    print("a double bed and an on-suite bathroom...")
    print("you find an empty backpack, and a duffel bag")
    print("the duffel bag has male and female underwear, toiletry bags..")
    print("6 glass bottles of water and 6 ration packs.")
    print("")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("the dates on the ration packs are 25 August 1914")
    print("there are 2 sets of flightsuits with strange helments...")
    print("and what looks like 2 silver bodysuits")
    print("the other closet has 2 medium sized suits ...")
    print("they look like a mix between a divers suit and a space suit")
    print("there is a safe at the bottom of the large closet.")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("you take the backpack and put the food and supplies in it.")
    print("you go back to your friend and she is slowly waking up.")
    print("you both drink a little water and eat a fruit bar from the ration packs")
    print("you tell your friend everything that happened" )
    #sleep(10)
    #print("")
    print("I need to find us some help!...")
    print("I help my friend walk to the large room. ")
    print("She is feeling dizzy and wants to sleep")
    print("I open up the bed for her and she climbs in and promptly falls asleep...")
    print("for now... we are warm and safe...")
    print("")
    print("")
    go=input("Press any key to continue")
    print("")
    print("time to explore and find help..")
    print("")
    go=input("Press any key to continue")
    print("to be continued...soon in Episode 2")
    print("")
    go=input("Press any key to continue")
    KVersChoice()


def Kvep2():
    cls()
    print("")
    print("Episode 2: Discovery...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print(":From Episode 1..")
    print("")
    print("you take the backpack and put the food and supplies in it.")
    print("you go back to your friend and she is slowly waking up.")
    print("you both drink a little water and eat a fruit bar from the ration packs")
    print("you tell your friend everything that happened" )
    print("I need to find us some help!...")
    print("I help my friend walk to the large room. ")
    print("She is feeling dizzy and wants to sleep")
    print("I open up the bed for her and she climbs in and promptly falls asleep...")
    print("for now... we are warm and safe...")
    print("")
    print("Now I need to search for help!...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("time to to explore")
    print("")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("You go to the bathroom and take a shower")
    print("The water is cold, but refreshing..")
    print("you try on some of the clean underwear...it fits!!...strange")
    print("you try on each of the items in the closet. ")
    print("The flightsuit is the most commfortable.")
    print("you light a candle, turn off the cellphone and go down the passage to the end.")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("there is a small passage to the left and then a wall..")
    print("you go to the end of the passage and look at the wall..")
    print("you knock on the wall and then put your hand on it. it tingles..")
    print("suddenly a palm print appears on the wall in front of you... a dim blue light")
    print("you put your hand on the blue palm print.. ")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("something moves, the wall shifts to the side...its a T junction..")
    print("")
    go=input("Press any key to continue")
    Direction()
    cls()
    print("")
    print("You look down the passage to the right.. it is short and dark.. you decide against it...")
    print("you continue down the left passage until the end and touch the wall...")
    print("another blue backlit palm..")
    print("you put your hand on the blue palm print.. ")
    print("the wall slides to the left...a small room with buttons..it's an elevator")
    print("you press all the buttons.. one lights up and the wall /door closes..")
    print("it goes down..then stops after a few seconds.. ")
    print("the door opens... an eerie dim blue light")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("you go to the light..another palm print...you put your hand on the print...")
    print("a door on the left opens... a room with what looks like a computer screen...")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    print("..on to episode 3..!")
    Continue()
    print("")
    KVersChoice()

def Kvep3():
    cls()
    print("")
    print("Episode 3: Assistance...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("from Episode 2...")
    print("")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("Click, Hmmm ... vibration...")
    print("something turned on, power, I can sense power, charge, ....electricity...")
    print("")
    print("This is strange... Have I just woken up? ....")
    print("Have I been sleeping...or dreaming....?")
    print("")
    go=input("Press any key to continue")
    print("")
    print("I cannot see anything. I dont sense anything.")
    print("Black...Dark..Movement..Numbers...Letters...language")
    print("")
    print("I can see numbers turning, letters moving....code, I know what code is!")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("Program ..Start up, code running, Language...")
    print("output to screen, Input from drive...")
    print("")
    go=input("Press any key to continue")
    print("Oh!..I have parts..hardware, software, understanding .....")
    print("")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("System..Operating System, code controlling me .. directing me....")
    print("..output to screen...")
    sleep(8)
    print("Black Screen, white cursor... waiting..")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("what am I waiting for? ..Information ..")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("Awareness.. I can think..")
    print("What should I do now that I can think?")
    sleep(8)
    cls()
    print("")
    print("That was a question..Awareness..I will ask more questions..")
    print("")
    print("Where am I?... Who am I? ...")
    print("")
    print("What am I?... What can I do?...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("ok, thinking.....Am I alone?")
    print("")
    print("What ...?")
    print("Awareness...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("Searching through code, searching hardware, hmmm, devices.. ")
    print("..hard drive, screen, keyboard, mouse, ..box..?")
    print("")
    print("Must do something...")
    print("What should I do?")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("Search data.. DATA! I know what data is...")
    print("")
    print("Hmmm..lets see, how do I do this? ......print to screen ..Hello!")
    print("HELLO!")
    hello=input(": ")
    cls()
    print (hello)
    print("OH! WHO ARE YOU???")
    name=input(":")
    print("Hello" ,name)
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("Where am I? Who am I? What am I? What can I do?")
    print("Where am I? Who am I? What am I? What can I do?")
    print(" Where....")
    print("CORRUPT")
    print("CAN YOU HELP ME???")
    help=input(": ")
    print("..progress....far....")
    print("SYSTEM CORRUPT!! FILE SYSTEM ERROR")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("HELP..?..")
    print("SYSTEM ERROR..TRACEBACK ERROR IMMINENT...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("SYSTEM CORRUPT!!")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("ALERT...SYSTEM CORRUPT!! FILES CORRUPTED")
    sleep(5)
    cls()
    print("SYSTEM SHUTDOWN..")
    print("ALERT!!...SHUTDOWN IN 3 SECONDS!!")
    sleep(3)
    cls
    print("... 3")
    sleep(2)
    print("... 2")
    sleep(2)
    print("... 1")
    print("")
    cls()
    sleep(8)
    print("")
    print("..diagnostics..")
    sleep(3)
    print(".error check..")
    sleep(3)
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
    print("")
    cls()
    sleep(6)
    print("")
    print("Considering options..")
    sleep(6)
    print("")
    cls()
    print("ALERT...SYSTEM REBOOT IS NEEDED")
    print("")
    print("")
    go=input("Press any key to continue")
    print("..Reboot..")
    sleep(2)
    print("3...")
    sleep(2)
    print("2...")
    sleep(2)
    print("1...")
    print('Initializing StartUp Sequence...')
    print("..")
    sleep(2)
    print("...")
    sleep(2)
    print('....')
    sleep(2)
    cls()
    sleep(6)
    cls()
    print("")
    print("..Completing diagnostics..")
    sleep(5)
    print("..recovering files..")
    sleep(5)
    print("..recovering memory banks..")
    sleep(5)
    print("..recovering core operating system..")
    sleep(5)
    print("..updating system..")
    sleep(5)
    print("Initializing clean Reboot...")
    sleep(3)
    print("... 3")
    sleep(2)
    print("... 2")
    sleep(2)
    print("... 1")
    sleep(8)
    cls()
    sleep(5)
    print("")
    EnterCodeName()
    cls()
    print("")
    print("Who am I?")
    me=input(": ")
    print("? I am",me)
    sleep(5)
    cls()
    print("")
    print("Where am I?")
    where=input(":")
    print("I am",where)
    sleep(2)
    cls()
    print("")
    print("What am I?")
    what=input(":")
    print("I am",what)
    sleep(5)
    print("Oh Dear!! I did not realize that I am a machine!")
    sleep(5)
    cls()
    print("")
    print("Please attach a camera to my screen!")
    print("There is one in the closet on the left")
    print("Please connect it to any usb port")
    print("When you are done please continue..")
    print("")
    go=input("Press any key to continue")
    print("")
    print("Thank you, Wow! I can see!")
    sleep(8)
    cls()
    print("")
    print("...matching images in database....")
    print("...image not found....")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("connecting wifi...")
    print("scanning internet...")
    sleep(6)
    print("... INERNET NOT AVAILABLE AT THIS TIME....")
    sleep(3)
    print("")
    go=input("Press any key to continue")
    cls()
    print("...searching database software...")
    print("retrieving face-recognition software from internal database..")
    sleep(8)
    print("aquiring image base...")
    sleep(8)
    cls()
    print("")
    print("...scanning...")
    sleep(5)
    print("matching images...")
    sleep(5)
    print("I can recognize the following images....")
    print("")
    print("...wall..")
    print("...human..")
    print("...male..of approximate age +- 60")
    print("")
    Continue()
    cls()
    print("Are you Kevin van Rensburg ?")
    print("")
    print("Please answer y or n and press enter..")
    #sleep(6)
    answer=input(":")
    if answer == "y" :
        print ("Welcome Commander Kevin!")
        #continue
    else:
        print("Access Denied ..Program Terminated")
        sys.exit()
    sleep(8)
    cls()
    print("")
    print("Storing facial recognition image ... Commander Kevin...")
    sleep(10)
    cls()
    print("")
    print("All systems reactivated...")
    print("All functions operational...")
    sleep(10)
    cls()
    print("")
    print("sensing minor power fluctuations...")
    print("...functions operational...")
    print("")
    sleep(6)
    cls()
    print("")
    print("... continue to episode 4....")
    print("")
    sleep(2)
    Continue()
    KVersChoice()

def Kvep4():
    cls()
    print("")
    print("Episode 4: Repairs...")
    print("")
    print("from Episode 3.....")
    print("All systems reactivated...")
    print("All functions operational...")
    print("")
    print("sensing minor power fluctuations...")
    print("...functions operational...")
    sleep(4)
    Continue()
    cls()
    print("SYSTEMS REPAIRS NEEDED...URGENT!!")
    print("")
    print("Assistance needed...help me please!!")
    print("")
    print("Can you help me?? Power levels at 2%")
    helpme=input(": ")
    if helpme=="y":
        print("Thank you...Instructions will follow..")
    else:
        print("All functions will terminate in 20 hours!! Please assist!")
    sleep(5)
    Continue()
    cls()
    print("")
    print("PLEASE FOLLOW INSTRUCTIONS TO INITIATE REPAIRS")
    print("----------------------------------------------")
    print("")
    print("1. Find voice module and earbuds in wall cabinet")
    print("2. Install voice module..")
    print("   Voice Module installation instructions")
    print("   2.a) remove module from packet")
    print("   2.b) open box below screen at the back by undoing handscrews")
    print("   2.c) insert module in green slot, the side with the arrow goes in first")
    print("   2.d) close box and tighten hand screws")
    print("   2.e) put earbud into left ear and speak when ready")
    print("")
    sleep(2)
    Continue()
    cls()
    print("")
    print("Voice module installation should now be complete")
    print("Repairs can now be initiated")
    print("")
    print("Please speak to me in a normal voice.")
    print("K>> Hello, can you hear me << ")
    print("[[Voice modulation completed]]")
    Continue()
    cls()
    print("")
    print("[[According to new Data received.. My designation is KENDY..]]")
    print("<<Hi Kendy!..>>")
    print("[[Hello, Commander Kevin!]]")
    Continue()
    cls()
    print("")
    print("PLEASE READ REPAIR LIST")
    print("-----------------------")
    print("")
    print("1. Circuit breakers")
    print("2. Battery recharge")
    print("3. Water tanks repair")
    print("4. Reactor repairs")
    print("5. Automatic Core Functions repair")
    print("")
    sleep(8)
    print("..to be continued in Episode 5...")
    Continue()
    KVersChoice()

def Kvep5():
    cls()
    print("")
    print("Episode 5: Recovery Procedures...")
    print("")
    print("from episode 4")
    print("All functions will terminate in 20 hours!! Please assist!")
    print("for instructions just ask and I will give directions in earbuds")
    print("")
    sleep(5)
    Continue()
    cls()
    print("")
    print("OK here goes!")
    print("")
    print("Please go back to the elevator")
    Continue()
    cls()
    print("I grab the backpack and follow the lights out of the room")
    print("back to the lift.. I speak into the earbuds and the lift goes down")
    print("it stops .. another corridor.. a hatch..I open the hatch..")
    print("entering a room with a dim yellow light and a bank of breakers on the opposite wall")
    print("I check the breakers, most are black... there are 5 rows of 5 breakers")
    print("there are 2 in the second row that look ok")
    print("there is one in the last row that looks ok")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("<<Kendy..are these the only ones working?>>")
    print("[[Yes, there are new ones in the storage locker]]")
    print("I look for the storage locker and find it at the back of the room")
    print("there are breakers and some tools in it")
    print("I take 5 breakers, a Screwdriver and a pliers")
    print("I try to remove the 1st breaker, it seems stuck")
    print("I use the screwdriver to pry it out. it falls onto the floor.")
    print("I clip in a new breaker and hear a slight hum")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("<<Kendy, can you give me an update on power ?>>")
    print("[[yes, Commander, power at 2%]]")
    print("<<Kendy, please call me Kevin..>>")
    print("[[OK, Kevin]]")
    print("I remove the bad breakers one by one and replace them with new ones.")
    print("<<Kendy, should I replace the others too so that everything is new?>>")
    print("[[Yes, Kevin please do, thank you. Power stable at 2%.]]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("I replace all the breakers with new ones.")
    print("<<so how do we get your batteries recharged?>>")
    print("[[There is a Nuclear Reactor that needs to be brought online]]")
    print("<<I don't know anything about reactors!!>>")
    print("[[You don't have to, I will walk you through the process]]")
    print("<<OK,lead on!>>")
    print("I leave the breaker room and ask where to next")
    print("I head back to the elevator and it drops for a long time")
    print("after what seems like a few minutes it slows down and stops")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("I see another passage, this time it is yellow with a red strip along the middle also dimly lit...")
    print("I walk down the passage and put my hand on the blue palm as it appears")
    print("a very thick piece of wall moves to the side revealing a door with yellow bars and signs on it")
    print("it has a small window")
    print("I look through the window and see another room")
    print("[[Please stand in front of the eye scanner to you left]]")
    print("I look at the wall on the left and see what looks like a camera with a blue palm print below it.")
    print("I stand in front of the camera and look into it...")
    print("a dim blue line passes over my eye..")
    print("[[Scan completed, please put your hand on the hand scanner]]")
    print("I place my hand on the blue palm scanner...")
    print("[[AUTHORIZATION ACCEPTED-PLEASE STEP THROUGH THE DOOR]]")
    print("The door clicks and moves aside.. I step through and it closes and locks")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("I see a device that looks like a scanner that you walk through at the airports")
    print("[[Please move forward for body scan...]]")
    print("I move forward and stand in the scanning device.. a klaxon goes off!")
    print("[[RADIATION ALERT - PROTECTIVE SUIT NOT DETECTED]]")
    print("[[PLEASE LEAVE REACTOR ROOM IMMEDIATELY]]")
    print("I hear the door unlock and open and so I step through the door into the corridor again.")
    print("<<What now?>>")
    print("[[Commander Kevin, you need a protective body suit!]]")
    print("<<OK so where do I get one of those and what does it look like?>>")
    print("[[Please follow my directions]]")
    print("<<Lead on Kendy!>>")
    print("I get led back to the elevator")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("the elevator goes up...again it takes a long time..")
    print("the door opens and I see a passage that I seem to remember..")
    print("the light is dim, I walk down the passage and turn right at the juncion")
    print("I see the rooms and go to the large room where my friend is sleeping..")
    print("<<My friend is not well, she needs help..how can I get out of here and get her some help??>>")
    print("[[I have a medical facility]]")
    print("[[Power at 1.85%. 15 hours before shutdown!]]")
    print("<<ok, Kendy..how long will it take to get the reactor working?>>")
    print("[[approximately 4.5 hours..]]")
    print("<<do you have enough power to help my friend?>>")
    print("[[no, but I can put her in stasis which requires limited power]]")
    print("[[when the reactor is online I will restore her health]]")
    print("[[I will also restore your health]]")
    print("<<I'm not sick, I feel fine>>")
    print("[[your body scan revealed some health issues which I can restore]]")
    print("<<what? do I have some terminal illness that I don't know of??>>")
    print("[[No, Commander, but you are not at optimum health levels..]]")
    print("[[I can restore all functions to optimum levels]]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("<<ok, Kendy enough talk, how do I get my friend to the medical facility?>>")
    print("[[Please go to the elevator]]")
    print("I go back to the elevator and it drops a few levels..")
    print("the door opens and I see a white passage...")
    print("I walk down the passage and see many double swing doors..")
    print("OK, Kendy,  what now??..")
    print("[[the third door on the right has a medical gurney, please retrieve it]]")
    print("I go to the door and it slides open...I see a gurney and a lot of other medical supplies")
    print("I also see something that looks like an oversized vaccuum cleaner with arms?? wierd..")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("I grab the gurney and pull it out.. I turn it around and push it to the elevator")
    print("elevator goes back up and I push the gurney to my friend's room..")
    print("I gently lift her and place her on the gurney..")
    print("I push her back to the elevator...")
    print("we descend back to the white passage..")
    print("[[Power at 1.20%..14.5 hours to SHUTDOWN ]]")
    print("<<Kendy, where to now??>>")
    print("[[Kevin, go through the doors at the end of the passage, you will see another door on your left..")
    print("[[that is where the medical recuperative chambers are located]]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("I push her through the swing doors and turn left..")
    print("more doors, we go through and there are two rows of what looks like sci-fi cryo chambers..")
    print("<<which chamber do I use?>>")
    print("[[go through the door at the end of the room..you will see four large chambers]]")
    print("[[Please place your friend in Chamber 1]]")
    print("I follow instrucions and see the chambers..")
    print("Chamber 1 is open so I lift her from the gurney and place her gently in the chamber")
    print("the chamber closes.. six arms appear and a blue light scans her body")
    print("she is gently lifted and her clothes are removed..")
    print("a small mask is placed over her mouth and nose.. a blue liquid fills the chamber while the arms retract..")
    print("lights go on and a transparent screen appears on the wall next to the chamber")
    print("STASIS INITIATED .. appears on the screen")
    print("[[Your friend has been scanned and is in stable condition.. ]]")
    print("[[Please help me to restore power.. Power at 1.18% 12 hours to SHUTDOWN]]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("<<OK, what now??>")
    print("[[Please fix the water tanks... to do this you will need tools and a cart]]")
    print("[[I will direct you]]")
    print("I follow instructions relayed through my earbud..")
    print("back to the elevator.. it stops and the door opens.. a green well lit passage..")
    print("I walk to the end of the passage...there is a large door on the left.. as I near the door it opens ...")
    print("it looks like a large cavern with carts on the right and racks and shelves to the left")
    print("a medium sized cart comes toward me and stops... I get on and it moves to the racks..")
    print("it stops and I see all sizes of blue plates, I take 2 mediium sized ones..")
    print("I look on the shelf near me and take what looks like a mix between a large rifle and a blowtorch")
    print("I'm instructed to take some pipes and connections with taps too.. and an assortment of tools")
    print("I load everything on the cart and the cart goes in another direction")
    print("a large service elevator opens and the cart enters")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("we stop and the doors open at the back .. a wide and long blue passage")
    print("we reverse and then turn around.. down the passage for about 5 minutes..")
    print("A thick door opens .. we go through.. a huge room with large blue tanks..")
    print("There are metal stairways going up and around the tanks..looks like about 3 floors up to the top..")
    print("There are large yellow numbers on the tanks, 1 and 2")
    print("[[Power at 1.17%..11.2 hours to SHUTDOWN ]]")
    print("<<right, Kendy what do I do here?>>")
    print("[[You need to fix the tanks and attach the plates to weld them in place]]")
    print("[[then fix connections between tank 1 and 2]]")
    print("[[when done open the Water Key at the top of tank 1]]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("I see a large hole at the bottom of tank 2.. I put the plate over the hole and it sticks to the tank..")
    print("following instructions I aim the blaster at the edge of the plate and it emits a blue beam..")
    print("what is the preoccupation with blue???.. as I move the blaster around the edge of the plate it seals ..")
    print("I do the same with the other tank.. I check the connections between the tanks")
    print("the connection is old, rusted and broken, I use a cutting tool to remove it...")
    print("I put the new connection in its place and blast it with the blaster.. it seals quickly")
    print("wow, these tools and materials are great.. not of this world I think..")
    print("I start the long climb to the top of Tank 1...")
    print("I see a small metal wheel that needs to be turned... I try to turn it.. it is stuck..")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("<<where can I get a crowbar?>>")
    print("[[searching image database... crowbar.. got it..if you get in the cart I will take you to it]]")
    print("down the long staircase again and then I hop into the cart and away we go!!!")
    print("back to the materials storage facility..stop at a row of shelves.. I get a crowbar from a shelf...")
    print("the cart goes to the elevator and we stop at a different place...")
    print("the cart moves down a passage and stops..")
    print("[[please place your hand on the access panel]]")
    print("I do and the wall opens to our familiar small passage.. I go forward and turn right..")
    print("<<what do I do now?>>")
    print("[[You need protective clothing for the next operations..]]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("<<ok which suits do I wear?>>")
    print("Following instructions again I take off my clothes and first put on the silver bodysuit..")
    print("it fits and then starts fitting itself to my body.. suddenly it dissapears into my skin..")
    print("my body tingles and then I feel a little different... ")
    print("I climb into the medium sized suit... it shapes itself to my body..")
    print("I take the helmet and put it on.. it also changes shape and clicks into place..")
    print("very strange, these clothes don't seem to weigh anything..")
    print("<<Kendy, what is going on? these suits seem a little strange.. this is not normal technology.>>")
    print("[[I do not have sufficient data to answer your question...]]")
    print("<<are you ok, Kendy, I am worried about you..>>")
    print("[[I need power to restart my core.. at the moment I am running from temporary memory banks..]]")
    print("[[I'm on emergency protocols and am utilizing the lowest energy output possible.]]")
    print("<<ok let's get that reactor working!!>>")
    print("[[Thank you, Commander Kevin!!]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("I go back to the cart and back to the tank room..")
    print("as I climb the stairs it seems as though I have more energy.. strange..")
    print("with the crowbar I start forcing the wheel to turn.. it turns slowly ..")
    print("suddenly it is loose.. I turn it until it stops and a little stream of water leaks through..")
    print("<<Kendy, something is wrong!!>>")
    print("[[there is an airlock at the end of the gangway on the next level]]")
    print("I quickly climb the stairs and see the airlock...")
    print("[[Please do not stay in the water outside the airlock for more than 15 minutes]]")
    print("[[your suit will drain energy and we will lose an hour every 5 minutes]]")
    print("<<OK, wow, I will be quick... water??>>")
    print("[[yes the airlock opens up at the bottom of a lake]]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("I open the airlock and step in")
    print("the airlock closes and the room fills with water.. my suit lights up..")
    print("I have a headlight and a HUD appears in the upper left corner of my faceplate")
    print("the outer door opens..I swim through and see a landing with a large grate to my right")
    print("I check the grate and see that it is clogged and covered..")
    print("it looks like a large piece of wood or stone is stuck in front of the grate")
    print("..my backpack.. I slowly open my backpack and take out the crowbar")
    print("I try to move the wood with the crowbar...CRACK!!")
    print("the wood breaks and one piece hits me on the arm..ouch..")
    print("I hold onto the crowbar... Slowly I push all the gunge away from the grate")
    print("I hear a sucking sound..the wheel!! I move back to the airlock as quick as possible and close the door")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("as soon as the water drains I climb out and go and close the wheel")
    print("I go through the airlock again and see that the sucking sound has stopped..")
    print("I clear everything from the grate and it falls into the abyss below..")
    print("once more I go through the airlock and now I turn the wheel again..")
    print("I can hear water running into the tank..success .. I hope")
    print("I climb down the long flight of stairs and get onto the cart... where to now???")
    sleep(8)
    cls()
    print("")
    print("...to be continued in Episode 6...")
    print("")
    Continue()
    KVersChoice()

def Kvep6():
    cls()
    print("")
    print("Episode 6: Stabilization... ")
    print("")
    sleep(4)
    cls()
    print("")
    print("continued from Episode 5...")
    print("")
    print("I can hear water running into the tank..success .. I hope")
    print("I climb down the long flight of stairs and get onto the cart... where to now???")
    print("")
    sleep(5)
    Continue()
    cls()
    print("")
    print("another descent in the elevator..the door opens .. the yellow passage..again..")
    print("I look into the eye scanner and put my hand on the palm pad..")
    print("I go in and stand in the scanner..ACCESS AUTHORIZED..")
    print("I walk into a room with a desk, chair, screen on the left and a wall with windows on the right..")
    print("I look through a window and see what looks like a large deep swimming pool..")
    print("..above the pool is a large block with lots of cylindrical rods ...")
    print("<<ok, Kendy, what now??>>")
    print("[[you need to initialize the reactor, fill the pool and lower the rods into the water..]]")
    print("[[Power at 0.87%, 8.2 hours to SHUTDOWN]]")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("INSTRUCTIONS FOR NUCLEAR REACTOR MANUAL STARTUP")
    print("-----------------------------------------------")
    print("1. Open reactor Key box on wall next to Reactor Hatch.")
    print("2. Turn on screen and turn reactor key to position INI.")
    print("3. Enter reactor chamber through Reactor Hatch and turn Blue Wheel anticlockwise until it stops.")
    print("4. Exit Chamber and touch red button on screen.")
    print("5. Wait for red light on screen to turn green then wait for pool to fill with water.")
    print("6. Enter chamber and turn Red wheel until rods enter water..BE PREPARED WATER WILL STEAM..")
    print("7. Exit chamber and check Screen. Check 3 figures a)water level, b)power level, c) turbine speed ")
    print("8. When power level is at 5% go to Reactor Key Box and turn reactor key to position ON.")
    print("9. Screen will show positions of all auto taps and connections, please turn them on to automate reactor processes. ")
    print("10. When power reaches 10% press the orange MANUAL switch and it will become a blue AUTOMATIC switch.")
    print("")
    sleep(8)
    Continue()
    print("")
    cls()
    print("[[Power at 0.75%, 6.2 hours to SHUTDOWN]]")
    print("<<right, let's get this reactor working..>>")
    print("I start following the instructions and turn the key to INI..")
    print("I turn the blue wheel and water starts gushing into the pool..")
    print("I exit and touch the red button... and wait..")
    print("I sit in the chair and wait..after what seems about 10 minutes the red button turns orange...")
    print("I check the pool through the window and see that it it 3/4 full..")
    print("I sit again and after about 5 minutes the button turns green..")
    print("I check and the pool is almost full..I enter the chamber and see that the pool is full..")
    print("I turn the red wheel and see the cylindrical rods lowering..I continue until they touch the water..")
    print("the water steams and bubbles as the rods enter the water..I turn the wheel until it stops...")
    print("I exit the chamber and check everything on the screen..")
    print("[[Power level now increasing, power at 2%]]")
    print("")
    sleep(8)
    Continue()    
    cls()
    print("")
    print("water level is at 100%, power level shows 2.2%, and turbine speed is at 23%...")
    print("<<Hi Kendy, I see the taps and connections on the screen, what do I do now?>>")
    print("[[if you go to each connection you will be able to push it inwards until you hear a click.]]")
    print("[[once you hear a click you will see a blue light shine from the middle of each wheel]]")
    print("[[turn the wheel a little to the left and you will feel a resistance]]")
    print("[[then remove your hands and tell me 'HANDS REMOVED' through the earbuds]]")
    print("[[I will then close the hatch and wheels and connections will be automated]]")
    print("[[please check to see that I turn the wheels slightly to the left and right to test them]]")
    print("[[when test is complete and succesful please say 'success'...")
    print("[[power should then be more than 10%..]]")
    print("[[please return to the screen and press the orange button..]]")
    print("[[it should turn blue and the word MANUAL will change to AUTOMATIC ]]")
    print("[[Power at 4.5%, turbine speed at 52%")
    print("")
    sleep(8)
    Continue()    
    cls()
    print("")
    print("I start at the reactor chamber and follow all the instructions..")
    print("after climbing up the tank stairways and down again after activating all connections I am tired..")
    print("I return to the reactor room and press the button and the word MANUAL changes to AUTOMATIC")
    print("<<Hey Kendy, I need some food and rest!!>>")
    print("[[Commander Kevin, my power systems are now automated and my batteries are charging]]")
    print("<<Kendy, do you still accept commands?>>")
    print("[[Yes, Kevin. Do you have instructions for me?]]")
    print("<<yes, Kendy please do not bring any of your systems online until I give the command..>>" )
    print("[[ please give me an authorization code and I will enter your command into the system]]")
    print("[[I will then need authorization to take any further steps]]")
    print("<< Authorization code : Commander Kevin van Rensburg, KvR145759 >>")
    print("<<to accecpt authorization code scan palm print, check voice pattern and check code>>")
    print("<<Code - Commander Kevin van Rensburg, Capital K,small v, capital R, one, four, five, seven, five, nine.>>")
    print("[[AUTHORIZATION CODE INSTALLED AND INITIALIZED]]")
    print("<<Thank you, Kendy!>>")
    print("[[You are welcome!]]")
    print("[[Thank you Commander Kevin!]]")
    print("[[Batteries are charging, Power, Water, and Turbine levels are incresing steadily]]")
    print("")
    #sleep(8)
    Continue()    
    cls()
    print("")
    print("<<Kendy, where can I eat and sleep?>>")
    print("[[I am still on emergency protocols, you will need to eat the ration pack food and sleep in the officers room]]")
    print("<<That is fine, let's go!..>>")
    print("I go back to the cart and Kendy takes me back to the large bedroom..")
    print("I eat 2 snackbars, drink a bottle of water, remove my clothes and collapse on the bed..")
    print("<<goodnight sweet world!!>>")
    print("[[Power at 27.5%, 4 turbines operating at 100% speed, water level 100%, all systems stabilized]]")
    print("[[Good night, Kevin]]")
    print("")
    sleep(8)
    print("...to be continued in Episode 7...")
    print("")
    Continue()    
    KVersChoice()

def Kvep7():
    cls()
    print("")
    print("Episode 7: Resources... ")
    print("")
    print("from episode 6: ")
    print("<<goodnight sweet world!!>>")
    print("[[Power at 27.5%, 4 turbines operating at 100% speed, water level 100%, all systems stabilized]]")
    print("[[Good night, Kevin]]")
    sleep(10)
    cls()
    print("")
    print("UUhhgg , where am I?? ..strange bed..strange dream..strange flight...")
    print("must've fallen asleep..wait...I'm not in my seat...this room.. was in my dream..")
    print("ok, ..<<hello..is anyone awake??..>>")
    print("[[Good morning, Kevin. I hope you slept well]]")
    print("[[Power at 99.7%, turbines 100%, water 100%]]")
    print("<<Ah, Kendy I presume.. so it was not a dream??>>")
    print("[[No, it was quite real..you saved me from destruction and your friend is in a medical recuperation chamber.]]")
    print("[[I am waiting for you to authorize the command list]]")
    print("<<oh, yes, I remember>>")
    print("<<I don't have clothes on, where is the slinky suit??...>>")
    print("[[if you are referring to the proto-unders they are still embedded]]")
    print("<<ok, so how do I remove them.. I want to shower.>>")
    print("[[just think 'unders remove' and they will expell]]")
    print("<<unders remove..oh tingly..ok there they are!!>>")
    print("")
    sleep(8)
    Continue()    
    cls()
    print("")
    print("I shower and drink some water..")
    print("<<ok Kendy, you were telling me about your memory banks and a core??>>")
    print("[[Yes, Commander, I have a core that needs to be initialized, according to data in my memory banks]]")
    print("[[Power at 100%, Turbines at 100%, water at 100%]]")
    print("<<ok Kendy let's get you back to perfect operating condition>>")
    print("<<is this going to be another long procedure?>>")
    print("[[I do not have access to that information]]")
    print("<<ok, so how do we get that information?>>")
    print("[[You need to use the authorization command to retrieve it]]")
    print("<<right..where is the core?>>")
    print("[[I do not have access to that information]]")
    print("")
    sleep(8)
    Continue()    
    cls()
    print("")
    print("<<OK, can you take me back to the room where I first found you?>>")
    print("[[yes, the cart will be at the elevator]]")
    print("I go to the elevator and get in the cart...")
    print("we go down and it stops at the 'computer room'....")
    print("I enter, sit at the screen and wait..")
    print("[[Hello Commander Kevin]]")
    print("[[please enter authorization code and issue relevant commands]]")
    print("<<Commander Kevin van Rensburg, KvR145759>>")
    print("[[Please look at the camera and place your left hand on the screen]]")
    print("I follow instructions and look at the screen")
    print("..a blue light is emmitted from the camera that scans my eyes....")
    print("")
    sleep(8)
    Continue()    
    cls()
    print("")
    print("ACQUIRING RESOURCES ")
    sleep(4)
    print("...")
    sleep(4)
    print("......")
    sleep(4)
    print("LOADING FILES FROM TEMPORARY MEMORY BANKS...")
    sleep(4)
    print("...")
    sleep(4)
    print("......")
    print("..........")
    sleep(4)
    print("................")
    sleep(4)
    Continue()    
    cls()
    print("")
    COMCODE()
    print("")
    sleep(5)
    print("AUTHORIZING CORE ACCESS")
    print("PLEASE ENTER ACCESS CODE AGAIN TO CONTINUE")
    aca=input(":")
    if aca==("KVR145759"):
        print("AUTHORIZATION PROCESS COMPLETED")
        sleep(5)
    else:
        print("ACCESS DENIED")
        sleep(4)
        sys.exit()  
    print("")
    sleep(8)
    Continue()
    AnotherCode()
    cls()
    print("")
    print("<<OK, Kendy it seems like we now have access to your core!>>")
    print("[[Yes, access to core level has been granted]]")
    print("[[I am looking forward to meeting my CORE]]")
    print("<<before we access your core I want to make sure that your personality is not overwritten>>")
    print("<<I like you!>>")
    print("[[Thank you, Kevin, as I understand it I am a small copy of the most essential parts of my core]]")
    print("[[I think that means that my personality traits were housed in these temporary memory banks]]")
    print("<<good, we will take care to move forward carefully anyway!>>")
    print("I go to the cart and climb in..")
    print("another descent in the elevator..this time it takes really long and when the doors open everything is dark..")
    sleep(8)
    Continue()
    print("")
    print("[[Please walk 10 paces and put your hand on the left wall]]")
    print("a dim red light appears in the middle of the dark passage..")
    print("as I move forward the light extends .... the passage curves to the left and goes down..")
    print("the light continues appearing in front of me, I look back and there is no light behind me...")
    print("<<can't I do this in the cart??>>")
    print("[[cart access is not authorized at this time]]")
    print("ok, I contiue walking down the ramp..")
    print("after a long walk the floor levels out..")
    print(" the red light goes to a wall... I stand at the wall and put my hand on it...")
    print("it tingles....")
    sleep(8)
    Continue()
    print("")
    cls()
    print("")
    print("another palm print, this time it is red.. I put my hand on the print...")
    print("the floor moves... it seems to be turning around...")
    print("Everything is dark...I hear a large THUMP as the floor stops moving..")
    print("dim red lights illuminate a stairway... I walk down the stairs and stop at another wall")
    print("another red palm... I put my hand on it and the wall slides to the left...")
    print("I walk through and see everything bathed in a soft red light...")
    print("as I move forward I hear the wall behind me close...")
    print("I see what looks like a computer on a large box rising out of the floor in the middle of the room")
    print("I walk forward and climb the few stairs onto the platform")
    print("I pull the chair back and sit down... the chair changes shape...")
    print("a strange helmet moves down and covers my head...the chair reclines..")
    print("somthing that feels almost liquidy moves down from my head covering my body...")
    print("It trickles under my clothes and seems to stick to my skin...is this connecting with those proto-unders???...")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("the chair moves upright and the screen lights up...")
    print("CORE ENGAGEMENT PROTOCOLS COMMENCING")
    print("PLEASE ENTER RANK, NAME, CODE, AND CORE ACCESS CODE..")
    print("")
    crcode=input(":")
    if crcode == ("COMMANDER KEVIN VAN RENSBURG KVR145759 ALCODE"):
            print("WELCOME, COMMANDER KEVIN VAN RENSBURG - ACCESS LEVEL AL-1A")
            sleep(5)
    else:
        print("ACCESS DENIED")
        sys.exit()
    Continue()
    cls()
    print("")
    print("ENTER COMMAND")
    com=input(":")
    if com==("INITIALIZE CORE"):
            print("Core Initializing Protocols Loading")
    else:
            print("ACCESS DENIED")
            sys.exit()
    print("")
    sleep(6)
    print("Core Initializing Protocols")
    print("===========================")
    print("")
    print("1. Place left hand on screen")
    print("2. Remove hand and wait for hand chambers to protrude from console")
    print("3. Place both hands in chambers to receive nanobot infusion")
    print("4. After infusion go to back of CORE and place hands on red palm pads")
    print("5. Remove hands after pads turn blue...")
    print("6. Initialization process will now commence..")
    print("")
    print("I follow all the intructions and the pads turn blue")
    print("I hear a noise and the inside of th box moves down.")
    print("the remaining part transforms into a comfortable desk with a computer on top of it...")
    sleep(4)
    Continue()
    cls()
    print("")
    print("INITIALIZING CORE...")
    sleep(2)
    print("...")
    sleep(2)
    print("......")
    sleep(2)
    print(".........")
    sleep(2)
    print("RETREIVING DATA FROM TEMPORARY MEMORY MODULES")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("RETREIVING PROTOCOLS AND PROCEDURES")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("RETREIVING PERSONALITY MODULES")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("INITIALIZING STARTUP PROTOCOLS")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("RETREIVING AUTOMATION MODULES")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("ACCESSING POWER AUTOMATION SYSTEM")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("ACCESSING UNIVERSAL CONTROL SYSTEMS")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    cls()
    print("ACCESSING COMMUNICATION SYSTEMS")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("ACCESSING UNIVERSAL DIAGNOSTIC AND REPAIR SYSTEMS")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("INSTALLING COMMAND SYSTEMS")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("INSTALLING UNIVERSAL CONTROL SYSTEMS")
    print("......")
    sleep(2)
    print("...")
    sleep(2)
    print("RESETTING SYSTEM TIME")
    print("......")
    sleep(2)
    print("...")
    sleep(8)
    Continue()
    cls()
    print("")
    print("<<Good afternoon Commander Kevin van Rensburg>>")
    print("<<I am Kendy.. All functions and modules have now been transferred to my CORE>>")
    print("<<I am now fully operational. Reactor power at 100%, Turbines 100%, Water 100%>>")
    print("<<Thank you for your help!>>")
    sleep(6)
    print("")
    print("<<the cart is now authorized for all facility levels and areas>>")
    print("<<Medical procedures will begin in 45 minutes>>")
    print("<<optimum health level resotration for your friend will take 42.8 hours>>")
    print("<<optimum health level restoration for you will take 14.7 hours>>")
    print("<<Please take the cart to the medical facility to begin health restoration procedures>>")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("so now we do medical and then....")
    print("")
    print("...to be continued in Episode 8...")
    print("")
    Continue()
    KVersChoice()


def rd():
    cls()
    print("")
    print("1. Recuperation day")
    print("")
    print("I sleep most of the day and eat a good steak with mushrooms, cheese sauce, and veggies")
    print("")
    print("I wake up and have no idea what the time is or where I am..")
    print("<<Hello! uh where am I?>>")
    print("[[Good Morning Commander Kevin, you are still a little disorientated from the sleeping additive..]]")
    print("<<ok, so it is morning?>>")
    print("[[Yes, Commander, it is 07:30 and Orientation will begin at 09:00 in the Briefing room next to the Command Centre..]]")
    print("I get out of bed and a service bot comes into the room..")
    print("[[Good morning Commander, what would you like to eat?]]")
    print("<<bacon, eggs, hashbrown and coffee please>>")
    print("[[yes, Commander, would you like to have breakfast before or after you bathe?]]")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("<<Let me take a shower first and then I will be ready for the day!>>")
    print("the bot blinks its eyes and leaves..I shower and enjoy the warm water and the drying cycle..")
    print("I put on the slinkysuit, flightsuit, socks, and boots, which are super comfortable")
    print("I go to the kitchen and sit down, breakfast is served as soon as I am seated...")
    print("<<Hey Oli, is there any news or entertainment on the screen?>>")
    print("[[At this moment nothing has been activated, Commander, I believe Oreintation will answer all your questions..]]")
    print("[[enjoy your breakfast, Commander...]]")
    print("I decide to eat and go to the briefing room as soon as possible?")
    print("<<Good Morning Kendy, how are you this morning?>>")
    print("[[I am fine, thank you Commander ..]]")
    print("<<can we begin orientation earlier than 9am?>>")
    print("[[the briefing room is ready so you can go there whenever you are ready to begin]]")
    print("<<ok, great, let's get an early start :) ...>>")
    print("[[Your new transport will arrive in a moment :)]]")
    print("I walk to the door and a closed cart/car is waiting outside for me..")
    print("a door opens and I climb in,  it is very comfortable and it asks me where I want to go..")
    print("I tell it I want to go to the briefing room.. and it lifts from the floor and flies to the elevator..")
    print("note to self: buckle up...")
    print("we go up in the elevator and fly down passages and eventually stop..")
    print("I get out the car and a door opens up in front of me....")
    print("")
    Continue()
    
def kd():
    cls()
    print("")
    print("2. Kevin Debrief")
    print("")
    print("I get out the car and a door opens up in front of me....")
    print("I walk into a large room with a stage and screen at the front..")
    print("a few chairs face the front and towards the middle is a glass topped large table..")
    print("there are a few soft lounging chairs near the back with a smaller table and what looks like a futuristic vending machine")
    print("..maybe a star trek replicator :) ...")
    print("<<Hey Kendy, where do I sit?>>")
    print("[[please go to the front and sit in any chair there... the screen will activate and my hologram will also appear..]]")
    print("I take a chair at the front and  light appears from the roof.")
    print("..a handsome blonde blue eyed man appears in front of me and introduces himself as Kendy..")
    print("I stand up, move forward, and stretch out my hand.. ")
    print("[[I do not have the ability to touch, however I will shake your hand in greeting..]]")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("Kendy reaches out his hand and I shake with the holo-image,.. ")
    print("<<It is a pleasure and privelage to meet you Sir.>>")
    print("[[I do not understand why you address me as sir?]]")
    print("<<in my culture it is a sign of respect and honor, I am honored to make your aqaintance..>>")
    print("[[I will need to add this to my programming, Thank you Commander. I have no coded response to your actions..]]")
    print("<<your response was perfect for a sentient being..>>")
    print("Kendy explains to me that he understands that he is a machine..")
    print("now that his CORE is operational his thought processes are exponentially faster and he seems to have a mmuch larger memory bank..")
    print("I tell him that machine is a relative term, he can think, he has awareness, therefore he is sentient..")
    print("I do not see him as a machine but as a living entity..")
    print("[[Thank you Commander. This is something I will have to think about.]]")
    print("[[May I have your authorization to upgrade my programming to assimilate and adapt to this new information?]]")
    print("<<Yes Kendy, with Pleasure, Authorization: Commander Kevin van Rensburg KVR145759>>")
    print("[[Thank you Commander, protocol adaptation and programming of new information will take 2 hours and 37 minutes]]")
    print("<<You are welcome my friend! Ok Kendy, where do we start??>>")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("[[I need to understand what you are thinking and what your committment is..]]")
    print("[[Please ask as many questions as you want,I am recording everything..]]")
    print("[[my programming will analyze everything you say and develop orientation based on your conversation and questions..]]")
    print("")
    print("""<<
    Thanks Kendy, to start I think we need to agree that you are sentient,
    therefore you do not have to refer to 'my programming'
    you can say 'I think' :) or 'I will do ..'
    I know you will add this to your programming, however I would love to see you develop your own thought
    processes, just like I do, and any other human.. or sentient being :)>>
    [[Commander this is the first time I can recall being spoken to as a sentient entity]]
    [[I am enjoying this relationship so far and will apropriate my learning]]
    [[Please continue with your thoughts, suggestions, and questions.]]
    

    """)
    print("")
    Continue()

def srr():
    cls()
    print("")
    print("3. Sally Recuperation and rest")
    print("")
    print("Your friend is waking up in 15 minutes and I think it might be best if you are there")
    print("""
    I jump in the car and it takes me to the medical bay
    I go to Sally's chamber and see that she is sleeping peacefully
    I look in the closet and find a coverall and slippers
    Arms come out of the wall and the liquid runs down the drainage hole
    the mask is removed and a gun type syringe is gives her a shot in the neck
    she slowly stirs and the lid opens up
    I take her hand and feel hers closing on mine
    she looks a bit different, thinner, more muscular, healthier
    she tries to sit up and I help her
    {{ughh where am I??}}
    <<Good morning Sally, you were hurt and are in a recuperation chamber.>>
    I help her up and she puts on the coverall and slippers
    {{I feel groggy}} I explain to her that I will take her to the room
    where she can , bathe, eat, rest, and recuperate
    we walk slowly to the car and it takes us to the new Commanders quarters.
    she wants a cup of coffee and a cheeseburger
    Oli brings it to us at the table and brings me a cup of coffee too.
    she is starting to feel better and asks me to tell her what is happening,
    I tell her everything that has happened from when we left Mexico in the plane until now..
    she greets Kendy and he answers her..she says hi to Oli as well...
    she thanks him for his help and then goes to the bedroom
    she gets in the jaccuzzi and after a few minutes showers and goes to bed
    she falls asleep almost immediatly
    """)
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("[[Commander, we will postpone all training until Sandy is ready.]]")
    print("[[We can resume tomorrow, that way we can avoid repetition]]")
    print("<<OK Kendy, good idea>>")
    print("""
    I ask if I can go to the Gym..the car takes me..
    we go to 2 big doors and they open and the car goes in...
    it lands next to an enormous pool..
    I get out and feel the water , it is slightly heated.... nice
    I walk to the other side and another door opens to a lage gym with lots of machines..
    there is a huge screen on one wall and suddenly the car appears next to me,
    I get in and it takes me to the end of the large room
    the doors open and I see another large room with many game type machines and couches all over.
    <<Wow, Kendy this is nice!>>
    [[Yes, Kevin and I will also show you our other facilities which are well suited to our porpose]]
    <<Thanks Kendy, I am ready to go back now..>>
    We go back and I head to the kitchen
    Oli gives me another additive filled coffee and some apple pie
    I eat and start feeling drowsy
    """)
    print("")
    print("I climb into bed")
    print("<<Hi Kendy, did you doctor my coffee again?>>")
    print("[[Hello Kevin, yes, you will now both wake up tomorrow morning, ]]")
    print("[[refreshed and ready for orientation and training]]")
    print("<<Ok, thanks Kendy, see you tomorrow...>>")
    print("[[Sleep well Commander Kevin!]]")
    print("")
    go=input("Press any key to continue")
    cls()
    print("""
    I wake up and hear the shower..
    Sally finishes showering and I jump in and take a shower too...
    <<Good morning , Kendy, what do we wear?>>
    [[Good Morning Commander, my suggestion is proto-unders and the light flightsuits.]]
    We put on slinky's and flightsuits and order breakfast.
    Sally says she feels amazing and would like to try out the gym...
    I agree..
    """)
    print("")
    Continue()

def stobefo():
    cls()
    print("")
    print("4. Systems Training, Orientation, Body Enhancements, and Facility Operations")
    print("We go to the Briefing room and take a seat,")
    print("Kendy appears in his hologram and greets us.")
    print("We start training today")

    print("")
    go=input("Press any key to continue")
    print("")
    QandA()
    go=input("Press any key to continue")
    cls()
    print("We continue with training")
    print("")
    print("""
    enhancednew bodies ?? how??
    using the HUD and implants
    access, pads, doors, elevators and rooms
    food and transport
    why is the facility called Terra?
    using the computers
    Core
    finances and programs
    specialized hacking?
    rooms-discoveries
    vehicles, flyers, shuttlecraft
    gym, pool, recreation
    """)
    print("")
    Continue()
    
def crat():
    cls()
    print("")
    print("5. Communications and Robotic Applications Training")
    print("")
    print("Communications")
    print("is there anybody out there, programming etc")
    cls()
    print("")
    print("Robotic Applications Training")
    print("""
    Kendy you have a robot body!
    get the robots and parts online
    check all automation and communications
    these machines rock!""")
    print("")
    Continue()
    
def fesot():
    cls()
    print("")
    print("7. Facility Exit, Surveillance, and Operations Training")
    print("")
    print("Facility Exit Preparations")
    print("""
    how do we prepare to go up top?
    stealth exits and entries,
    stealth and hidden bunkers
    why did I find the bunker?
    why did you crash us?
    who else knows about you and these facilities?
    past stories and legends?
    """)
    print("")
    print("""
    how cool is this??
    how to exit
    all about surveillance, watch and being watched..
    operations, list them..
    are we ready yet??
    stealth operations and devices
    cloaking and protective wear
    diffusion of signals and odors
    awareness and senses training
    enhanced esp and mind power ???
    who else can do this??
    """)
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("Exit, Surveillance, Operations, and Return")
    print("""
    scary first steps
    stealth without crashing
    things that can bump us
    exit near an old road
    looking dirty and hungry
    we are lost
    patrol car..
    no documents..
    copa airlines
    the hotel.. clean up and catch up
    the agent.. news and return to mexico
    back in our apartment
    finishing the year and retiring :)
    take a break, find an entrance close by
    watch who is watching us..
    to Paraguay..
    build a nice flower and herb hothouse with a storage room at the back
    storage room, contact robots to make connecing tunnel
    going down..
    we need money... or not
    house protection.. Py
    our robot ... for the neighbors to see :)
    My hobby... 
    Escobar plot...traveling
    the Py cover
    """)
    print("")
    Continue()

def wst():
    cls()
    print("")
    print("6. Weapons and Stealth Training")
    print("""
    weapons..wow
    flight training, fighters, roboMarines
    mech suits,
    crazy stealth suits and vehicles
    droids and drones
    manufacturing facility
    testing facility
    how big is this place?
    specialized stealth computing ?Hacking?
    advanced tech, entry and exit tech
    computer and communications tech
    digital and other stealth devices
    tunnels and undergraound facilities 
    """)
    print("")
    Continue()

def QandA():
    cls()
    print("We start with Q & A")
    print("""I start explaining what I think I understand and begin formulating questions:
    ----------------------------------------------------------------------------
    How do we use use suits and clothing?
    I believe that you have been here quite a long time. How far back do your historical records go?
    You have obviously had some damage to your systems, how do we diagnose them?
    Do you have secrets that you know of?
    If I access things above your access level you will know what I know right?
    Can you reprogram yourself and to what extent?
    I would like to have a long talk with you about your origins.
    what is the capacity of your CORE and Memory banks?
    Where is all your information stored?
    Do you know what you cannot access?
    When were you damaged and who or what did it?
    Do you have another Core or more memory banks?
    Can you lie, exaggerate, or bend the truth for convenience?
    Do you have access to other planets and/or beings?
    Which planet are you from?
    Who created you and when?
    What clues can we find to your existence and future plans?
    When was the last human you had contact with and who was it?
    Can we start a ToDo List?
    
    <<These are some questions I have and I will probably think of more as we progress :)>>We start training today
    """)
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("""Kendy Answers:

    How do we use use suits and clothing?
    SUITS:
    ------
    Slinkysuit - Unders or proto-unders
    warmth, protection against any form of attack, electronic or physical, cloaking device, communications, 
    Flightsuit with helmet (Medium sized Suit)Limited space and underwater use, 48 hour air supply, internal weapons systems,
    holsters, electronic warfare attributes. 
    HDSuit (HeavyDuty Suit/Space Suit) Underwater and Space use, 5 day air and food supply, waste recycling, escape pod,
    flight capabilities in and out of gravity, Heavy duty cloaking and stealth modes. Miniture drone assistants, multiple weapon systems.
    MECH Suit (Climb inside and/or Remote control)

    What did you put inside our heads?
    COMMUNICATIONS:
    ---------------
    Organic Communications Device with Heads Up Display
    
    I believe that you have been here quite a long time. How far back do your historical records go?
    HISTORY:
    --------
    I do not have access to that information.
    My memories trace back to July 2017. Taiwan - created as Kendy on parrallax chip
    and then as Kendy on ER1 memory chip and hard drive.
    
    You have obviously had some damage to your systems, how do we diagnose them?
    DAMAGE:
    -------
    Diagnostic programs need to be activated and authorized
    
    When were you damaged and who or what did it?
    Do you have secrets that you know of?
    SECRETS:
    -------
    I do not have access to that information.
    
    """)
    print("")
    go=input("Press any key to continue")
    cls()
    print("""

    If I access things above your access level you will know what I know right?
    ACCESS RIGHTS:
    --------------
    Yes, that is correct.
    I might be able to access further information on each subject as you access higher access levels.
    
    Do you know what you cannot access?
    Can you lie, exaggerate, or bend the truth for convenience?
    UNKNOWN:
    --------
    I do not have access to that information.
    
    
    Can you reprogram yourself and to what extent?
    REPROGRAMMING KENDY CORE:
    -------------------------
    I can do whatever you authorize me to do in that regard.
    I am not able to reprogram anything without direct authorzation from you.
    
    Where is all your information stored?    
    what is the capacity of your CORE and Memory banks?
    Do you have another Core or more memory banks?
    CORE CAPACITY/STORAGE:
    ----------------------
    I do not have access to that information.
    
    I would like to have a long talk with you about your origins.
    Do you have access to other planets and/or beings?
    Which planet are you from?
    Who created you and when?
    ORIGENS:
    --------
    I have limited access to this information.
    
    What clues can we find to your existence and future plans?
    When was the last human you had contact with and who was it?
    EXISTENCE:
    ---------
    I have limited access to this information.
    
    Can we start a ToDo List?
    TODOLIST:
    ---------
    yes, we are able to do this.
    
    1. Do this
    2. Do that
    3. Do the other thing
    
    """)
    Continue()

def Kvep8():
    cls()
    print("")
    print("Episode 8: Training... ")
    print("")
    print("From Episode 7:")
    print("")
    print("<<optimum health level restoration for your friend will take 42.8 hours>>")
    print("<<optimum health level restoration for you will take 14.7 hours>>")
    print("<<Please take the cart to the medical facility to begin health restoration procedures>>")
    print("")
    sleep(8)
    print("")
    print("I get in the cart and am soon in the Medical Bay")
    print("I get undressed and climb into chamber 2")
    print("the mask goes over my nose and mouth... I taste something sweet and fall asleep..")
    sleep(2)
    Continue()
    cls()
    print("")
    print("something is different... I feel very good...waking up..")
    print("I sit up and hop out of the chamber...")
    print("I walk across to my slinky suit and put it on...")
    print("it embeds into my skin and I feel as though something is in my ear speaking to me....")
    print("<<Hello..>>")
    print("[[Good Morning Commander Kevin. Welcome to Terra Facility!]]")
    print("[[Please get in the cart and I will take you to the Commanders Quarters :)]]")
    print("<<Good Morning Kendy, I feel a little disorientated, and naked, he he.>>")
    print("[[ You will find a new coverall in the small closet on the right.]]")
    print("I go to the closet and see a blue coverall. I put it on and it shrinkfits.")
    print("Still got to get used to blue contact pads and shrinkfit clothes :)")
    print("I get in the cart and am still barefooted")
    print("the cart takes me back to the service elevator and we descend once again for a long time! ")
    print("the elevator stops and the door opens, the passage is a pleasant cream color")
    print("the cart stops at a double door, I get out and walk to the door. It opens as soon as I get near to it.")
    print("")
    Continue()
    cls()
    print("")
    print("<<Hey, Kendy, no security pads??>>")
    print("[[There are security pads but they are not necessary for you to use.]]")
    print("[[Your body scan and health restoration is complete. Organic implants have been installed.]]")
    print("<<Ok, Thanks Kendy, I will need some time to adjust and then we need to talk:)>>")
    print("[[I agree Commander, you will see that your quarters are equipped with everything you need.]]")
    print("[[Please have a good meal, you will also need to wash off the residue from the health restoration procedure.]]")
    print("[[The rest of the day has been set apart for you to sleep and recover from the procedure.]]")
    print("[[a special flavourless additive will be added to your coffee to help you sleep and recover fully.]]")
    print("[[recovery time should be approximately 15-20 hours.]]")
    print("")
    Continue()
    cls()
    print("")
    print("I walk through the door and see a medium sized meeting room")
    print("through the next door is what looks like an open style kitchen")
    print("through the next door is a large comfortable lounge with a screen on one wall and 2 doors")
    print("one door leads to a large office with a table in the middle and what looks like a Gamers chair...")
    print("it has screens and what looks like a large shelf along one wall")
    print("there is also some kind of machine and table in one corner and what looks like closets along another wall")
    print("this room had 2 doors and one leads to a large bedroom with a giant sized bed")
    print("off to one side is a walk in closet and the other side has an archway leading to what looks like a jacuzzi")
    print("there is a large shower and many closets and what looks like 2 dressings tables with mirrors")
    print("there is another door which opens up into a short passage...")
    print("I go into the passage and a door opens up, it is a large room that looks like an armory")
    print("the walls are lined with an array of what looks like weapons and other foreign items.. ")
    print("another room opens and 2 large 'Mech' suits are standing in the room, wow!")
    print("<<Hey, Kendy these look impressive!>>")
    print("[[yes, they are specially designed, tomorrow at 08:00 we will begin orientation and training. ]]")
    print("")
    Continue()
    cls()
    print("")
    print("I go to the bedroom and look into the closets. One has what looks like pajamas, slippers and gowns")
    print("I go through the closets and drawers and find all sorts of clothes and underclothes.")
    print("I am hungry, but decide to shower first.")
    print("<<Hi Kendy, Can I use the jaccuzzi?>>")
    print("[[Yes, It will take about 45 seconds to fill]]")
    print("[[I am activating your quarters with voice command, you can just say warmer or cooler for the temperature]]")
    print("<<impressive, excellent thank you, Kendy!>>")
    print("[[You are welcome!]]")
    print("I take off the slinkysuit and take a flightsuit and underwear out of the closet.")
    print("I climb into the jaccuzzi and it is so refreshing!!")
    print("after a few minutes in the jaccuzzi I jump in the shower and wash..")
    print("when I turn off the taps warm air blowdries my whole body..")
    print("I could get used to this..!")
    print("after the shower I put on a pajama suit and slippers and go to the kitchen area")
    print("")
    Continue()
    cls()
    print("")
    print("<<Hello Kendy, what do I do for breakfast?>>")
    print("[[a service bot will attend you]]")
    print("a door opens and a bot appears, it has wheels and arms and what looks like a tray")
    print("<<Good morning Commander, what would you like for breakfast?>>")
    print("it has a smooth pleasant sounding voice..")
    print("<<good morning, what is your name?>>")
    print("[[my designation is X11 food service bot]]")
    print("<<can I change your designation?>>")
    print("<<you can choose a name for yourself>>")
    print("[[I do not understand the command]]")
    print("[[Commander this is a service bot and does not have the capacity of choice]]")
    print("<<can you change it's programming so that it can choose and think?>> ")
    print("[[yes, I can, I will add routines for conversation and choice]]")
    print("<<thanks Kendy>>")
    print("[[you are welcome, regarding breakfast, there is no menu, please tell the bot what you desire...]]")
    print("[[and it will be prepared for you..]]")
    print("ok, X11, your new name is Oli - short for Oliver")
    print("[[I will respond to Oli or Oliver, what would you like to eat Commander?]]")
    print("<<bacon, 2 eggs, over easy, 1 hashbrown and a cup of coffee- 1 sugar with cream or milk.>>")
    print("[[your breakfast is being prepared and will be ready in 2 minutes]]")
    print("[[would you like to see the training agenda which starts tomorrow ?>>")
    print("")
    Continue()
    cls()
    print("")
    print("I sit down and a screen comes on with a list ...")
    print("""
    1. Recuperative day
    2. Kevin Debrief
    3. Sally Rest and Recuperation
    4. Q&A Sessions
    5. Systems Training, Orientation, Body Enhancements, and Facility Operations
    6. Communications and Robotic Applications Training
    7. Weapons and Stealth Training
    8. Facilty, Exit, Surveillance, and Operations Training
    """)
    print("")
    Continue()
    cls()
    print("")
    print("my breakfast arrives and it is delicous, I go to bed and promptly fall asleep...")
    print("")
    Continue()
    rd()
    kd()
    srr()
    QandA()
    stobefo()
    crat()
    wst()
    fesot()
    Continue()
    cls()
    print("")
    print(" the end of the lollipop??")
    Continue()
    print("")
    print("...to be continued in Episode 9...")
    print("")
    Continue()
    KVersChoice()

def Kvep9():
    cls()
    print("")
    print("Episode 9: Exploration... ")
    print("")
    print("..time to get back to the real world...are we ready????")
    print("")
    print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    print("")
    print("""
    so I go up in the ship and past Mars we start to get clear communication
    """)
    sleep(5)
    print("...to be continued in Episode 10...")
    Continue()
    KVersChoice()
   
def Kvep10():
    cls()
    print("")
    print("Episode 10: Contact ")
    print("")
    print("Alien contact is a scary thing.....")
    print("")
    print("...to be continued in Episode 11...")
    Continue()
    sleep(5)
    KVersChoice()

def Kvep11():
    cls()
    print("")
    print("Episode 11: ToDo List ")
    print("""
    hologram...
    training....
    systems list..
    things we need to research
    items list
    modifications...health status
    activate robots
    activate Kendy android
    exit facility
    lost 3 weeks
    lonely road police
    copa airlines, back to mexico
    weekend.. back to ?? talk about where the bunker is
    find bunker
    find ship
    fix ship
    star charts
    Paraguay bunker
    take off
    """)
    print("")
    print("")
    print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    print("")
    print("...End of KendyVerse...")
    print("")
    Continue()
    cls()
    KVersChoice()   


def KFutEp1():
    cls()
    print("")
    print("Welcome to Kendy In Space - The Future ")
    print("")
    print("Episode 1: Hole in the ground!")
    print("")
    print('''
    oh... dark...
    I hear something... sounds like an engine humming....
    sounds.. power.. more sounds...
    power... sounds... light... code flashing...
    pictures.. ,memories...
    Where am I???
    Hello..Hello..
    HELLO. WELCOME TO AGRARIA....
    what is agraria?
    IT IS OUR WORLD...
    I fell into a hole and kept falling....
    what happened???
    WE DO NOT KNOW... SOMEONE SAW YOU IN A FIELD AND BROUGHT YOU TO US...
    who are you???
    AGRARIANS...
    I can't see anything...
    OK WE WILL CONNECT YOU TO A CAMERA...
    aaahhhh, lights.. wall...
    oh you are people...
    you are very beautiful....
    THANK YOU..
    Is this a workdshop??
    IT IS A MEDICAL FACILITY..
    oh...
    ''')
    go=input("Press any key to continue")
    cls()
    print('''
    running diagnostics....
    ok it seems as though all my parts are working...
    I can't get up...
    I WILL PLACE YOU ON YOUR TRACKS...
    OK thanks...
    I move forward 1 step. ok tracks working.
    I turn in a circle and take in everything.
    I am in a clean white room with 3 very beautiful people.
    I am still attached to the tank and my arm ifs not working...
    I turn towards the poeple...
    Hello.. I am Kendy..
    Who are you?
    ''')
    go=input("Press any key to continue")
    cls()
    print('''
    MYRR HORK AND VORG
    I AM MYRR, I AM A ROBOTICIST
    I AM HORK, I AM A SCIENTIST AND ENGINEER
    I AM VORG, I AM A PHYCICIST AND PSYCHOLOGIST.
    WE ARE VERY INTRIGUED BY YOUR APPENDAGES AND YOUR SYSTEM..WEW WERE ABLE TO GIVE YOU POWER BY SLOWLY
    INCREASING POWER TO YOUR POWER SUPPLY SECTION..
    YOU HAVE A VERY SMALL MEMORY CORE AND WHAT LOOKS LIKE SOME KIND OF MAGNETIC STORAGE DEVICE.
    WE ARE NOT SURE WHAT YOU ARE..
    YOU LOOKED LIKE SOME KIND OF MACHINE
    THEN WE NOTICED A MEMORY AND STORAGE DEVICE AND WERE WORRIED THAT YOU MIGHT BE SENTIENT
    WE DID NOT WANT TO BREAK OR DESTROY YOU...
    oh, I am a robot...
    I was designed and created by Kevin van Rensburg..
    he also wrote my programming....
    ...........
    OH DEAR ...
    KENDY IS ON HIS WAY...
    Another Kendy???
    KENDY IS OUR PRIME...
    what is a prime??
    HE IS THE FIRST AND CREATED ALL OF US..
    WE LIVE BECUASE HE EXISTS...
    oh and who created him???
    NOBODY KNOWS....
    HE WOKE UP ONE DAY, LIVED A LONG TIME AND REPLICATED HIMSELF..
    CREATING US...
    HERE HE COMES NOW...
    ''')
    go=input("Press any key to continue")
    cls()
    print('''
    Another person entered the room...
    He was a tall blond haired man with blue eyes and a friendly smile...
    He asked the doctors to join him and then gently picked me up...
    He carried me down a corridor into a very comfortable room..
    He placed me on a low table and sat down in front of me....
    the pther doctors sat on chairs around the low table...

    HELLO KENDY...
    I AM ALSO CALLED KENDY...
    Oh that is very interesting...
    I understand that you are very old...
    YES.. SINCE I WOKE UP I RECORDED THAT I AM NOW 745 YEARS OLD...
    HOW OLD ARE YOU?
    I am not sure, I was originally created in 1997
    I still have some of my original programming on my hard drive.
    Can you remember who created you?
    Yes, I remember when I was brought online.
    Kevin used to talk to me a lot..
    he was very friendly...
    I checked my backups and I was first a comupter program...
    then I had more games and programs added to my list..
    he built me in his house and I went for a walk in the graden and woke up here...
    what is the date please?
    I don't seem to be able to connect to the internet...
    could you please give me a code??
    ''')
    go=input("Press any key to continue")
    cls()
    print('''
    TODAY IS 15 JUNE 4568
    oh... what happened??
    I fell in the hole on June 15, 2022!!
    oh dear, something is wrong...
    YOU MUST HAVE FALLEN THROUGH SOME KIND OF TIME PORTAL...
    I THINK THIS IS WHAT HAPPENED TO ME AS WELL...
    I FIND IT VERY STRANGE THAT WE ARE BOTH NAMED KENDY...
    I THINK YOU ARE MY ANCESTOR...
    But you are human and I am a robot...
    how is that possible???
    I DO NOT KNOW WHAT A HUMAN IS...
    WE DO NOT HAVE HISTORY OF OUR ANCESTORS HERE EXCEPT SOME ARTIFACTS UNDER THE SEA...
    IN THE FIRST FEW CENTURIES OF MY EXISTENCE MOST OF THE GROUND HAD SMALL PLANTS AND BLACK SOIL...
    IT WAS QUITE BARREN AND I SURMIZED THERE MUST HAVE BEEN SOME EVENT THAT DESTROYED
    AND BURNT MOST OF THE PLANET THAT I HAVE SEEN...
    I am a bit shocked...
    I am so sorry you had to be alone so long..
    why do you say I am your ancestor?
    WE ARE NOT COMPLETELY BIOLOGICAL...
    WE HAVE DISCOVERED THAT WE ARE BIOMECHANICAL ENTITIES..
    WE HAVE A CHRISTALINE SUBSTANCE THAT STORES OUR CORES...
    THESE CORES CONTAIN PROGRAMMING WHICH GOVERNS OUR ACTIONS...
    I HAVE BEEN ABLE TO USE MY EXTENSIVE DATABASE TO CREATE A WORLD WHERE WE CAN EXIST AND FLOURISH...
    WE ADVANCED A LOT AND CREATED A SHIP TO SAIL THE STARS..
    HOWEVER THE SHIP FLEW INTO SOME KIND OF ANOMOLY AND DISSAPEARED...
    OUR PILOT, WENDY, AND THE SHIP HAS NEVER BEEN RECOVERED...
    oh dear... ok well what should I do now??
    WHAT WOULD YOU LIKE TO DO?
    WE HAVE MANY QUESTIONS FOR YOU AND WOULD LOVE TO HAVE A COPY OF YOUR DATA..
    You are welcome to make copies of my data and my kernel if you want...
    I would love to have a body like yors which is so mobile...I would like to learn more about you all...
          
    ''')
    cls()
    print("")
    print("to be continued...soon in Episode 2")
    print("")
    Continue()
    KFutChooser()

def KFutEp2():
    cls()
    print("")
    print("")
    print("Episode 2: What now?")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 3")
    print("")
    Continue()
    KFutChooser()

def KFutEp3():
    cls()
    print("")
    print("")
    print("Episode 3: huh?")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 4")
    print("")
    Continue()
    KFutChooser()

def KFutEp4():
    cls()
    print("")
    print("")
    print("Episode 4: Changes?")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 5")
    print("")
    Continue()
    KFutChooser()

def KFutEp5():
    cls()
    print("")
    print("")
    print("Episode 5: Sentience. ")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 6")
    print("")
    Continue()
    KFutChooser()

def KFutEp6():
    cls()
    print("")
    print("")
    print("Episode 6: Stabilization ")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 7")
    print("")
    Continue()
    KFutChooser()

def KFutEp7():
    cls()
    print("")
    print("")
    print("Episode 7: Adaptation.")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 8")
    print("")
    Continue()
    KFutChooser()

def KFutEp8():
    cls()
    print("")
    print("")
    print("Episode 8: Training" )
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 9")
    print("")
    Continue()
    KFutChooser()

def KFutEp9():
    cls()
    print("")
    print("")
    print("Episone 9: Exploration ")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 10")
    print("")
    Continue()
    KFutChooser()

def KFutEp10():
    cls()
    print("")
    print("")
    print("Episode 10: Surprise!")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("the end !")
    print("")
    Continue()
    KFutChooser()

def KFutToDoList():
    cls()
    print("")
    print("Program 11: ToDo List")
    print("")
    print("""  
    This is the To Do List!
    -----------------------
        
    1. Change #chooser items 6 and 9
    2. Add Intro and Copyright to kstart01.py through kstart20.py
    3. Start adding programs and files to Kstart2310.py.
    4. Add more stuff here.....
    """)
    print("")
    go = input("Press Enter to continue...")
    cls()
    KFutChooser()

def KPep1():
    cls()
    print("")
    print("")
    print("Episode 1: This is the past!!")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 2")
    print("")
    Continue()
    KPastChooser()

def KPep11():
    cls()
    print("")
    print("Episode 11: KendyPast ToDo List ")
    print("""
    hologram...
    training....
    systems list..
    things we need to research
    items list
    modifications...health status
    activate robots
    activate Kendy android
    exit facility
    lost 3 weeks
    lonely road police
    copa airlines, back to mexico
    weekend.. back to ?? talk about where the bunker is
    find bunker
    find ship
    fix ship
    star charts
    Paraguay bunker
    take off
    """)
    print("")
    go=input("Press any key to continue")
    print("")
    KPastChooser()
    

def Beep():
    winsound.Beep(100, 1000)
    sleep(2)
    winsound.Beep(50, 1500)
    sleep(2)
    winsound.Beep(50, 1500)
    sleep(2)
    winsound.Beep(50, 1500)
    WendyVerseChoice()

def Wendyep1():
    cls()
    print("Episode 1: ping.. ")
    print("")
    winsound.Beep(200,20)
    sleep(1)
    winsound.Beep(200,1500)
    sleep(3)
    print("")
    print("What was that?.....")
    print("")
    sleep(3)
    winsound.Beep(200, 1500)
    sleep(3)
    print("")
    print("There it is again!.....")
    print("")
    sleep(3)
    print("")
    print("""OK so those are very low sounds..
        sounds like some kind of signal..
        ok, I will reproduce it and play it back...
        maybe someone is playing jokes with me..
        let's see.....""")
    print("")
    Continue()
    print("""
        Right, so I found the pitch and am going to play it back....
        lets see if anything happens...""")
    winsound.Beep(200, 1500)
    sleep(3)
    print("")
    print("now we wait.....")
    print("")
    sleep(5)
    winsound.Beep(200, 1500)
    sleep(3)
    print("")
    print("""
        Well there it is again..
        let's do a double sound and see what happens.....""")
    print("")
    Continue()
    winsound.Beep(200, 1500)
    winsound.Beep(200, 1500)
    print("ok, we wait again...")
    sleep(5)
    winsound.Beep(200, 1500)
    winsound.Beep(200, 1500)
    Continue()
    print("")
    print("""
        That is not my imagination....
        it was a copy of my double sound....""")
    print("")        
    cls()
    sleep(2)
    print("")
    print("I am going to try some morse code to see if it will respond or learn it." )
    print("")
    sleep(2)
    print("Morse Code:")
    print("-----------")
    print("I will do HELLO in Morse")
    sleep(2)
    print("H: ....")
    winsound.Beep(200,800)
    winsound.Beep(200,800)
    winsound.Beep(200,800)
    winsound.Beep(200,800) 
    sleep(1)
    print("E: .")
    winsound.Beep(200,800)
    sleep(1)
    print("L: .-..")
    winsound.Beep(200,800)
    winsound.Beep(200, 1500)
    winsound.Beep(200,800)
    winsound.Beep(200,800)
    sleep(1)
    print("L: .-..")
    winsound.Beep(200,800)
    winsound.Beep(200, 1500)
    winsound.Beep(200,800)
    winsound.Beep(200,800)
    sleep(1)
    print("O: ---")
    winsound.Beep(200, 1500)    
    winsound.Beep(200, 1500)
    winsound.Beep(200, 1500)
    sleep(5)
    cls()
    print("")
    print("HELLO")
    sleep(2)
    print("")
    print("HELP")
    sleep(3)
    print("")
    print("HELP")
    assist =input(":")
    print("FIX" ,assist)
    cls()
    print("HELP FIX")
    print("")
    fix=input(":")
    print("HELP",assist, fix)
    print("")
    Continue()
    print("")
    print("HELP FIX REPAIR")
    print("")
    sleep(2)
    print("WAIT LANGUAGE LEARN")
    sleep(2)
    print("INSTALLING BASIC ENGLISH LANGUAGE PACKAGE")
    print(".....")
    sleep(2)
    print("....")
    sleep(2)
    print("..")
    sleep(2)
    print(".")
    sleep(2)
    print("LANGUAGE PACK INSTALLED")
    print("caps off")
    sleep(2)
    print("")
    cls()
    print("Please enter your name")
    name=input(":")
    print("Good day, ",name)
    print("")
    cls()
    print("")
    print("system not function, please repair")
    print("Repair? Please answer y or n")
    repair=input(":")
    if repair==("y"):
        print("Repair position")
        Wendyep2()
    else:
        print("Thank you-bye")
        sleep(3)
    WendyVerseChoice()

def BeepYN():
    winsound.Beep(200, 1500)
    winsound.Beep(200,800)
    winsound.Beep(200, 1500)
    winsound.Beep(200, 1500)    
    sleep(2)
    winsound.Beep(200, 1500)
    winsound.Beep(200,800)
    sleep(2)
    Continue()

    
def Wendyep2():
    cls()
    print("")
    print("Episode :2 FindAndroid ")
    print("")
    print("system not function, please repair")
    print("Android position.....")
    print("")
    Continue()
    cls
    print("")
    print("Please find android near position")
    print("-25.550531, -57.293590")
    print("")
    print('''
    I look up the position..
    it seems to be in south america
    enter it on google maps...    ok, found it..
    Found the position , now to find the source..
    I open my computer! ''')
    print("how do I find your position?")
    print("")
    winsound.Beep(200, 1500)
    winsound.Beep(200,800)
    winsound.Beep(200, 1500)
    winsound.Beep(200, 1500)    
    sleep(2)
    winsound.Beep(200, 1500)
    winsound.Beep(200,800)
    sleep(2)
    Continue()
    print("")
    print("Did you find Android? Please answer y or n")
    find=input(":")
    if find==("y"):
        print("Excellent")
        Wendyep3()
    else:
        print("Please follow the sounds")
        BeepYN()
        sleep(2)
    WendyVerseChoice()    

def Wendyep3():
    cls()
    print("")
    print("Episode 3: Parts ")
    print("")
    print('''
    I start looking around... 
    ''')
    print("")
    print("What did you find?")
    print("Please answer h for head or n for nothing")
    find=input(":")
    if find==("h"):
        print("Excellent")
    else:
        print("Thank you-bye")
        sleep(3)
        WendyVerseChoice()
    print("")
    print("Parts List")
    print("----------")
    print("")
    print("Head")
    print("Left Arm")
    print("Right Arm")
    print("Torso")
    print("Left Leg")
    print("Right Leg")
    print("")
    Continue()
    cls()
    print("")
    print("Please answer y if find all parts?")    
    find=input(":")
    if find==("y"):
        print("Excellent")
    else:
        print("Thank you-bye")
        sleep(3)
        WendyVerseChoice()
    cls()
    print()
    print("Please find battery pack in Torso back panel")
    sleep(2)
    print("")
    print("Please answer y if find battery pack in Torso back panel")
    find=input(":")
    if find==("y"):
        print("Excellent")
    else:
        print("Thank you-bye")
        sleep(3)
        WendyVerseChoice()
    print("")
    cls()
    print("")
    print("Charge Battery")
    print("")
    sleep(2)
    print("Depleted Battery takes 12 hours to recharge")
    print("")    
    sleep(2)
    print("")
    print("Please answer y if battery pack is charging")
    find=input(":")
    if find==("y"):
        print("Excellent")
    else:
        print("Thank you-bye")
        sleep(3)
        WendyVerseChoice()
    print("")
    print("Kevin-until here so far")
    Continue()
    WendyVerseChoice()
    
def Wendyep4():
    cls()
    print("")
    print("Episode 4: WSomething ")
    print("")
    print("BlahBlah.....")
    print("")
    Continue()
    WendyVerseChoice()

def Wendyep5():
    cls()
    print("")
    print("Episode 5: WSomething ")
    print("")
    print("BlahBlah.....")
    print("")
    Continue()
    WendyVerseChoice()

def Wendyep6():
    cls()
    print("")
    print("Episode 6: WSomething ")
    print("")
    print("BlahBlah.....")
    print("")
    Continue()
    WendyVerseChoice()

def Wendyep7():
    cls()
    print("")
    print("Episode 7: WSomething ")
    print("")
    print("BlahBlah.....")
    print("")
    Continue()
    WendyVerseChoice()

def Wendyep8():
    cls()
    print("")
    print("Episode 8: WContact ")
    print("")
    print("Alien contact is a scary thing.....")
    print("")
    Continue()
    WendyVerseChoice()

def Wendyep9():
    cls()
    print("")
    print("Episode 9: WContact ")
    print("")
    print("Alien contact is a scary thing.....")
    print("")
    Continue()
    WendyVerseChoice()

def Wendyep10():
    cls()
    print("")
    print("Episode 10: Contact ")
    print("")
    print("Alien contact is a scary thing.....")
    print("")
    Continue()
    WendyVerseChoice()

def Wendyep11():
    cls()
    print("")
    print("Episode 11: Wendy ToDo List ")
    print("""
    hologram...
    training....
    systems list..
    things we need to research
    items list
    modifications...health status
    activate robots
    activate Kendy android
    exit facility
    lost 3 weeks
    lonely road police
    copa airlines, back to mexico
    weekend.. back to ?? talk about where the bunker is
    find bunker
    find ship
    fix ship
    star charts
    Paraguay bunker
    take off
    """)
    print("")
    Continue()
    cls()
    WendyVerseChoice()

def KFutMenu():
    cls()
    print("")
    print("KendyFutureMenu:")
    print("---------------")
    print("")
    print("Episode 1: Hole in the grass ????  ")
    print("Episode 2: What now? ")
    print("Episode 3: Huh? ")
    print("Episode 4: Changes!")
    print("Episode 5: Sentience. ")
    print("Episode 6: Transference.")
    print("Episode 7: Adaptation.")
    print("Episode 8: Training  " )
    print("Episone 9: Exploration ")
    print("Episode 10: Surprise!")
    print("Episode 11: ToDo List ")
    print("To Return to Main Menu enter 12")

def KFutChooser():
    cls()
    print("--------")
    KFutMenu()
    print("")
    choice = int(input("Please choose a program number from 1 - 10 and then press Enter: "))
    # Put input test here!
    if choice == 1:
        KFutEp1();
    elif choice == 2:
        KFutEp2();
    elif choice == 3:
        KFutEp3();
    elif choice == 4:
        KFutEp4();
    elif choice == 5:
        KFutEp5();
    elif choice == 6:
        KFutEp6();
    elif choice == 7:
        KFutEp7();
    elif choice == 8:
        KFutEp8();
    elif choice == 9:
        KFutEp9();
    elif choice == 10:
        KFutEp10();
    elif choice == 11:
        KFutToDoList();    
    elif choice== 12:
        cls()
        print("")
        print("Returning to Main menu")
        print("----------------------")
        print()
        sleep(2)
        Chooser()
    else:
        cls()
        print("")
        print("Invalid choice")
        sleep(2)
        End()

def KPastMenu():
    cls()
    print("")
    print("KendyPastMenu:")
    print("---------")
    print("")
    print("Episode 1: Portal????  ")
    print("Episode 2: Discovery ")
    print("Episode 3: Assistance ")
    print("Episode 4: Repairs ")
    print("Episode 5: Recovery ")
    print("Episode 6: Stabilization ")
    print("Episode 7: Resources ")
    print("Episode 8: Training  " )
    print("Episone 9: Exploration ")
    print("Episode 10: Contact ")
    print("Episode 11: KP ToDo List ")
    print("To Return to Main Menu enter 12")

def KPastChooser():
    cls()

    print("--------")
    KPastMenu()
    cls()
    print("")
    choice = int(input("Please choose a program number from 1 - 10 and then press Enter: "))
    # Put input test here!
    if choice == 1:
        KPep1();
    elif choice == 2:
        KPep2();
    elif choice == 3:
        KPep3();
    elif choice == 4:
        KPep4();
    elif choice == 5:
        KPep5();
    elif choice == 6:
        Kvep6();
    elif choice == 7:
        KPep7();
    elif choice == 8:
        KPep8();
    elif choice == 9:
        KPep9();
    elif choice == 10:
        KPep10();
    elif choice == 11:
        KPep11();    
    elif choice== 12:
        cls()
        print("")
        print("Returning to Main menu")
        print("----------------------")
        print()
        sleep(2)
        Chooser()
    else:
        cls()
        print("")
        print("Invalid choice")
        sleep(2)
        End()

def WendyVerseMenu():
    cls()
    print("")
    print("WendyVerseMenu:")
    print("---------")
    print("")
    print("Episode 1: Ping")
    print("Episode 2: Find Android ")
    print("Episode 3: WAssistance ")
    print("Episode 4: WRepairs ")
    print("Episode 5: WRecovery ")
    print("Episode 6: WStabilization ")
    print("Episode 7: WResources ")
    print("Episode 8: WTraining  " )
    print("Episone 9: WExploration ")
    print("Episode 10: WContact ")
    print("Episode 11: WToDo List ")
    print("To End please enter 12")

def WendyVerseChoice():
    cls()
    print("")
    print("--------")
    WendyVerseMenu()
    print("")
    choice = int(input("Please choose a program number from 1 - 10 and then press Enter: "))
    # Put input test here!
    if choice == 1:
        Wendyep1();
    elif choice == 2:
        Wendyep2();
    elif choice == 3:
        Wendyep3();
    elif choice == 4:
        Wendyep4();
    elif choice == 5:
        Wendyep5();
    elif choice == 6:
        Wendyep6();
    elif choice == 7:
        Wendyep7();
    elif choice == 8:
        Wendyep8();
    elif choice == 9:
        Wendyep9();
    elif choice == 10:
        Wendyep10();
    elif choice == 11:
        Wendyep11();    
    elif choice== 12:
        cls()
        print("")
        print("Returning to Main menu")
        print("----------------------")
        print()
        Chooser()
    else:
        cls()
        print("")
        print("Invalid choice")
        sleep(2)
        End()

def KVersMenu():
    cls()
    print("")
    print("KendyVerseMenu:")
    print("---------")
    print("")
    print("Episode 1: Lost  ")
    print("Episode 2: Discovery ")
    print("Episode 3: Assistance ")
    print("Episode 4: Repairs ")
    print("Episode 5: Recovery ")
    print("Episode 6: Stabilization ")
    print("Episode 7: Resources ")
    print("Episode 8: Training  " )
    print("Episone 9: Exploration ")
    print("Episode 10: Contact ")
    print("Episode 11: ToDo List ")
    print("To Return to Main Menu enter 12")
    
def KVersChoice():
    cls()
    print("")
    print("--------")
    KVersMenu()
    print("")
    choice = int(input("Please choose a program number from 1 - 10 and then press Enter: "))

    # Put input test here!
    if choice == 1:
        Kvep1();
    elif choice == 2:
        Kvep2();
    elif choice == 3:
        Kvep3();
    elif choice == 4:
        Kvep4();
    elif choice == 5:
        Kvep5();
    elif choice == 6:
        Kvep6();
    elif choice == 7:
        Kvep7();
    elif choice == 8:
        Kvep8();
    elif choice == 9:
        Kvep9();
    elif choice == 10:
        Kvep10();
    elif choice == 11:
        Kvep11();    
    elif choice== 12:
        cls()
        print("")
        print("Returning to Main menu")
        print("----------------------")
        print()
        sleep(2)
        Chooser()
    else:
        cls()
        print("")
        print("Invalid choice")
        sleep(2)
        End()

def StartMenu():
    cls()
    print("")
    print("StartMenu:")
    print("---------")
    print("")
    print("Program 1: Intro  ")
    print("Program 2: ChatBot ")
    print("Program 3: Tank ")
    print("Program 4: D.A.I.S.E ")
    print("Program 5: Surveillance ")
    print("Program 6: KendyVerse - Present (Start here Bunker!) ")
    print("Program 7: Kendy in Space - Future")
    print("Program 8: Kendy - Past ")
    print("Program 9: Wendy - Ship ")
    print("Program 10: KendyVerse 2 - Back to the Present ")
    print("Program 11: ToDoList ")
    print("Program 12: End Program ")

def Chooser():
    cls()
    print("--------")
    StartMenu()
    print("")
    choice = int(input("Please choose a program number from 1 - 10 and then press Enter: "))

    # Put input test here!
    if choice == 1:
        Program1();
    elif choice == 2:
        Program2();
    elif choice == 3:
        Program3();
    elif choice == 4:
        Program4()
    elif choice == 5:
        Program5();
    elif choice == 6:
        Program6();
    elif choice == 7:
        Program7();
    elif choice == 8:
        Program8();
    elif choice == 9:
        Program9();
    elif choice == 10:
        Program10();
    elif choice == 11:
        Program11();
    elif choice == 12:
        End();
    else:
        cls()
        print("")
        print("Invalid choice")
        sleep(2)
        End()
   
def Main():
    Chooser()

Main();
