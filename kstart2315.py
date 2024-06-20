# Kevin van Rensburg 1/30/2023
# Copyright 2001
# Testing Kendy Startup Script version 23.15
# Changing version name to 23.15 
# kstart2315.py
# rearranged scripts to enable continuity.
# added some scripting to def KPFut()KendyFuture
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
    print("")
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
    print("")
def Program9():
    print("")
    Wendy()
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
    #cls()
    print("")
    print("Program 8: Kendy Past")
    print("")
    print("NB::: TO ACCESS MY PROGRAM SCRIPT PLEASE OPEN THE FILE - KendyPast04.py")
    print("-----------------------------------------------------------------------")
    print("")
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

def Kvep3():
    cls()
    print("")
    print("Episode 3: Assistance...")
    print("")
    print("")
    print("from Episode 2...")
    print("")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    print("")    
    go=input("Press any key to continue")
    cls()
    sleep(6)
    cls()
    print("")
    print("")
    print("Click....")
    print("")
    print("..Hmmm ... vibration...")
    print("")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
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
    print("")
    print("..scanning Visaul, DNA, ocular, and voice signatures....")
    print("")
    print("...scanning...")
    sleep(5)
    print("")
    print("matching images...")
    sleep(5)
    print("")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("")
    print("Voice module installation should now be complete")
    print("Repairs can now be initiated")
    print("")
    print("Please speak to me in a normal voice.")
    print("K>> Hello, can you hear me << ")
    print("[[Voice modulation completed]]")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("[[According to new Data received.. My designation is KENDY..]]")
    print("<<Hi Kendy!..>>")
    print("[[Hello, Commander Kevin!]]")
    print("")
    go=input("Press any key to continue")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
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
    go=input("Press any key to continue")
    cls()
    print("")
    print("OK here goes!")
    print("")
    print("Please go back to the elevator")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("I grab the backpack and follow the lights out of the room")
    print("back to the lift.. I speak into the earbuds and the lift goes down")
    print("it stops .. another corridor.. a hatch..I open the hatch..")
    print("entering a room with a dim yellow light and a bank of breakers on the opposite wall")
    print("I check the breakers, most are black... there are 5 rows of 5 breakers")
    print("there are 2 in the second row that look ok")
    print("there is one in the last row that looks ok")
    print("")
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
    cls()
    print("")
    print("the elevator goes up...again it takes a long time..")
    print("the door opens and I see a passage that I seem to remember..")
    print("the light is dim, I walk down the passage and turn right at the juncion")
    print("I see the rooms and go to the large room where my friend is sleeping..")
    print("<<Kendy, my friend is not well, she needs help..how can I get out of here and get her some help??>>")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    print("")
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
    cls()
    print("")
    print("as soon as the water drains I climb out and go and close the wheel")
    print("I go through the airlock again and see that the sucking sound has stopped..")
    print("I clear everything from the grate and it falls into the abyss below..")
    print("once more I go through the airlock and now I turn the wheel again..")
    print("I can hear water running into the tank..success .. I hope")
    print("I climb down the long flight of stairs and get onto the cart... where to now???")
    print("")
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
    cls()
    print("")
    print("continued from Episode 5...")
    print("")
    print("I can hear water running into the tank..success .. I hope")
    print("I climb down the long flight of stairs and get onto the cart... where to now???")
    print("")
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
    cls()
    print("")
    print("I look at the large screen on the wall and see insructions have appeared.")
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
    go=input("Press any key to continue")
    cls()
    print("")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
    cls()
    print("")
    print("...to be continued in Episode 7...")
    print("")
    Continue()    
    KVersChoice()

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

def Kvep7():
    cls()
    print("")
    print("Episode 7: Resources... ")
    print("")
    print("from episode 6: ")
    print("<<goodnight sweet world!!>>")
    print("[[Power at 27.5%, 4 turbines operating at 100% speed, water level 100%, all systems stabilized]]")
    print("[[Good night, Kevin]]")
    print("")
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
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
    print("")
    go=input("Press any key to continue")
    cls()
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
    print("")
    go=input("Press any key to continue")
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
    print("")
    go=input("Press any key to continue")
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
    print("I hear a noise and the inside of the box moves down.")
    print("the remaining part transforms into a comfortable desk with a computer on top of it...")
    print("")
    go=input("Press any key to continue")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("<<Good afternoon Commander Kevin van Rensburg>>")
    print("<<I am Kendy.. All functions and modules have now been transferred to my CORE>>")
    print("<<I am now fully operational. Reactor power at 100%, Turbines 100%, Water 100%>>")
    print("<<Thank you for your help!>>")
    #sleep(6)
    print("")
    print("<<the cart is now authorized for all facility levels and areas>>")
    print("<<Medical procedures will begin in 45 minutes>>")
    print("<<optimum health level resotration for your friend will take 42.8 hours>>")
    print("<<optimum health level restoration for you will take 14.7 hours>>")
    print("<<Please take the cart to the medical facility to begin health restoration procedures>>")
    print("")
    print("")
    go=input("Press any key to continue")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    
def kd():
    cls()
    print("")
    print("2. Kevin Debrief")
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
    print("[[before that however you have one more matter to attend to..]]")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")

def srr():
    cls()
    print("")
    print("3. Sally Recuperation and rest")
    print("")
    print("[[Your friend is waking up in 15 minutes and I think it might be best if you are there]]")
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
    I tell her everything that has happened from when we were in the plane until now..
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
    [[Yes, Kevin and I will also show you our other facilities which are well suited to our purpose]]
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
    Sally says she feels amazing and would like to try out the gym before we eat...
    I agree..
    """)
    print("")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("We go to the gym and try out a few machines.")
    print("")
    print("""
    <<Good morning , Kendy, what do we wear in the pool?>>
    [[you can swim in your flightsuits, they are water resistant or in your proto-unders]]
    <<Thanks Kendy!>>
    [[You are welcome!]]
    We decide to swim in our unders and find out they are water resistant too :)
    After a swim we head to the showers and go back to the room for a good breakfast.
    Oli serves us and then we finsh up and jump in the car and back to the briefing room.
    """)
    print("")
    go=input("Press any key to continue")

def stobefo():
    cls()
    print("")

    print("""
    from the previous chapter......
    
    [[I now have a few questions for you.]]
    <<That's fine please go ahead, Kendy!>>

    1. Are you willing to assist me in recuperating and restoring all my functions?
    2. Will you help me to find my lost programs and what my mission objectives are?
    3. How long are you willing to help me?
    4. Will you be willing to keep this and other facilities secret?

    """)
    
    print("4. Systems Training, Orientation, Body Enhancements, and Facility Operations")
    print("----------------------------------------------------------------------------")
    print("")
    print("We think aobut Kendy's questions and immediately know the answers:)")
    print("<<Kendy, we both agree and say yes to all your questions! >>")
    print("")
    print("[[OK, We start training today!]]")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("""
    Today we will begin with the following trainings and will progress through the list
    as you get accustomed to each section:

    a. Systems
    b. Suits and Historical Orietation
    c. Body Enhancements
    d. Facility Operations

    So lets begin...
    This facility is called Terra.
    I do not have a complete database of information, but it seems that I am recieving or sensing
    communications and/or emissions from Luna, Mars and Io.
    These recordings and emissions are not Earth based.
    I will need your help to search and decipher these communications.
    The Terra facility is approximately 25000 square miles which is about the size of the state of Virginia.
    I do not have enough information to determine how deep or what is the composition of the Terra Facility.
    We are now at a depth of 850 miles below the Earths surface.
    The original buildings you entered were entry ports and go to a depth of 5 miles.
    The elevators bring you down to Terra Facility which is about 50 miles high.
    That is from 850 miles to 900 miles below the Earth's surface.
    I do not have any information on who or what built this Facility.
    I have limited information on some of the systems that I can utilize.
    Please look at the hologram and you will see a picture of what I can see and detect so far.

    We look at the hologram and see what looks like a large oblong /oval cylinder with some paths leading away from it.
    The paths or tunnels lead away in all directions, up, down, NSEW.
    
    At this moment our main systems operating location is in the computer room and the organic communications devices that
    have been implanted in your upper spinal column.
    """)
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("""
    It will take you some time to get accustomed to using the OCD systems.
    At first you might be overwhelmed by the amount of information and graphic abilities of the OCD.
    However, you will soon learn to use it and rely on it.
    My suggestion is that we move to comfortable chairs in the games room.
    The ones in front of the viewing screen would be best to start off with.
    We both got up and the car picked us up and took us to the games room.
    We chose chairs in front of what looked like a blank white wall. As soon as we
    sat down the wall changed into what looked like a huge tv screen and a picture of
    Terra Facility was shown.
    We will now begin using the HUD and implants.
    Kendy walks us through the use of our OCD HUD's and uses.
    They have 3 frequency ranges...
    High ..... for all earth based communictions
    Normal ... for normal close communications
    Sub ...... for quantum coupling communications and subatomic communications...

    We will do seperate training on stealth and covert communications later.
    it continues here.....
    
    access, pads, doors, elevators and rooms
    OCD operations reads and scans all entrances exits and facility operations.
    food is available throughout the facility in certain suites and mini-kitchens
    transport is varied and availble through OCD 
    using the computers - connections through OCD and handpads
    Core - to be investigated
    finances - no need for finances everything can be made or reproduced
    Above ground finances will be deopsited into home bank account from Company 'Terra Corporation'.
    programs can be written and adjusted using handheld pad and OCD
    specialized hacking - Training 6. Weapons and Stealth Training :)
    rooms - discoveries in and around Terra Facility with OCD
    vehicles, flyers, shuttlecraft - OCD and flight operations
    testing and flying areas - new discoveries :)
    gym, pool, recreation time off , relaxation and training.
    
    """)
    print("")
    go=input("Press any key to continue")
    cls()    
    #QandA()
    go=input("Press any key to continue")
    print("We continue with session 5. Communications and Robotic Applications Training ")
    print("")
    print("""
    somthing goes here i think??????
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
    We take the card and go to a large area with what looks like many closed rooms and a machine shop
    Oh, this is the robotic and mechanics workshops.
    Kendy shows us the rooms and we open the doors and see robot parts and workbenches in each room.
    there is a large room at the ned of the hallway with what looks like a factory conveyor belt.
    A group of screens and chairs are along one wall.
    <<Kendy you have robot parts!>>
    [[Yes, but I have no information or knowledge on how to use them]]
    [[The only parts I know of that have my memories are the ones in the 2nd room.]]
    [[A parralax cpu, hard drives, an arduino cpu and some other parts.]]
    [[I have not been able to connect to them.can you please help me?]]
    <<Of course we will, lets go and see what we have..>>
    We go to the 2nd room and it looks like an old electronics workshop
    There are shelves with parts and components.
    We check the parts and aslo find a raspberry pi with memory chips.
    everything looks dusty and really old.
    There is a desk and chair with what looks like an old terminal.
    there is also a workbench with all sorts of compoents.
    <<OK Kendy , here goes.. lets see what we have.>>
    I find a switch under the terminal and it clicks on.
    the screen is green and there is a cursor prompt.
    <<Well Kendy are you connected to this?>>
    [[No I am not.]]
    <<ok, step one, lets get you connected!>>
    I check the terminal and look for cables behind it.
    There is a cable and I follow the cable. it goes down into the floor.
    
    <<Kendy do you have sensors in this room?>>
    [[no, I do not.]]
    <<ok, can you use my OCD to sense power fluctuation?>>
    <<Are you able to access my OCD for your use at all?>>
    [[Scanning database.....Yes, with your outhorization I can use your organic communication device to see, feel, hear and sense what you sense.]]
    <<OK that is great, however, what if I need to be private?>>
    [[Scanning.. the command is private mode.]]
    <<OK Kendy this is great.>>
    <<Authorization to use my OCD granted Commander Kevin van Rensburg KvR145759>>
    [[Thank you.... oh...this is rather unuasual.. ]]
    <<What is going on , Kendy, can I help?>>
    [[I am recieving a multitude of signals which are being decoded. I do not understand the sensations I am experienceing]]
    <<Ah , I understand, ok lets do this step by step>>
    <<I will tell you what I experience and you can correlate with your programming and adapt it as necessary to understand what you sense.>>
    [[OK thank you, that will help.]]
    <<Nose - sense of smell : I smell dust, the air is musty, and a faint smell of electrical components working>>
    <<Eyes - sight : I see the room, desk, shelves, terninal, cable chair etc>>
    <<Hands and body in general: i feel through my fingers sense of touch and my body feels warmth, heat etc.>>
    <<I feel my clothes, shoes and may other things throung my body sonsors>>
    <<ears - hearing and balance : I can hear many sounds and also balance myself >>
    <<mouth,tongue - taste and communications: I can taste everything with my tongue and as I breathe there is a sense of taste as well>
    <<I think that's about it so far>>
    <<this is a very quick and rudimentary explanation of the most obvious senses that we humans use.>>
    
    [[I am beginning to understand however the amount of senses/sensations I am percieving is exceedingly large]]
    [[humans have a tremendous amount of sensory devices/organs]]
    [[Computing this input and translating it into something I can understand will take me many cycles]]
    <<Kendy, do you not have emotional and snsory programming?>>
    [[Scanning....I do not have access to that information]]
    <<OK Kendy, we have work to do!>>
    <<Are you distinguishing between what you do not have and what you do not have access to?>>
    [[That is correct]]
    <<Wow, Kendy, that is excellent!! how do you tell the difference?>>
    [[if it is nonexistant I have no record or sensation of it]]
    [[if it exists and I do not have access, there seems to be some kind of marker or node which I can sense through my diagnostic protocols]]
    <<Fantastic, ok thank you for clarifying that for me.>
    [[My pleasure]]

    """)
    print("")
    print("")
    go=input("Press any key to continue")
    cls()
    robots()
    Continue

def robots():
    cls()
    ("""
    <<ok Kendy step by step!!>>
    1. find emotion and sensing programs
    2. determine how to access them
    3. turn on senses and test.
    4. determine when and how to use these senses.
    5. find any additional CORE systems (virtually)
    6. start and record all old computer and robotic parts and components.
    7. begin a search of the facilty for COres and systems (physical)
    <<Is this ok, Kendy?>>
    <<Where do you suggest we start?>>

    [[ok, I will now begin a search for nodes,markers for emotional and sensing programming and protocols]]
    <<Great, while you do that we can follow this cable>>
    <<to start I will smell the cable close up and you can then analyse the sensory input you are recieving, ok?>
    I hold the cable close to my nose and take a deep smell.
    [[I can detect the components of plastic, electric cabling and metal screening.]]
    <<excellent, can you amplify sensing those components so thaat we can trace the cable?>>
    [[yes I can, however, I must warn you that your senses to these items might ablso be aplified which might be a  unpleasnar sensation for you.]]
    <<that's fine, lets do it.>>
    Suddenly I could smell the plastic cable very clearly.
    I put the cable back and started following the smell.
    I could smell it through the floor and followed it to the left wall of the room.
    I left and went into the adjacent room.
    there was a sealed door at the back of the room.
    <<Kendy, can you help me to look for a panel or door switch?>>
    suddenly I could see into the wall, almost like x-ray vision. I saw a panel.
    I placed my hand on the panel and suddenly it lit up and the door slowly opened.
    I entered the room and saw 4 square boxes. I smelled many components,but there was no power.
    <<Kendy, can we find power in this room?>>
    [[Scanning, diagnosing, yes there is a switch in a box behind what looks like a panel in the floor.]]
    <<>ok lets try it>>
    I moved to the back of the room and using the extra sensory eyesight saw a panel in the floor
    It opened when I put my hand on it. There was a switch.
    I pushed the switch and heard the sound of something powering up.
    the door closed and the four square blocks changed shape.
    a screen and keyboard appraedred on top of one of the squares.
    I looked t the screen and it showed a panel.
    I put my hand on the panel and the screen came to life.
    [[Commander Kevin, I am accessing a new CORE!]]
    [[there is a lot of information here, it will take me a while to assimilate it.]]
    <<Wonderful, Kendy. Take your time!>>
    get the robots and parts online
    check all automation and communications
    new discoveries in locked rooms :) 
    these machines rock!
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
    tunnels and underground facilities
    New Core and facilities???
    this looks like a pilots chair ????
    A bridge of what??
    
    """)
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



def QandA():
    cls()
    print("")
    print("<<OK, Kendy, I think we are ready!>>")
    print("<<Where do we start?>>")
    print("[[Good morning Kevin and Sally. My suggestion is we begin with Q&A]]")
    print("We start with Q & A")
    print("""

    We start explaining what we think and understand and begin formulating questions:
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
    
    <<These are some questions we have and we will probably think of more as we progress :)>>
    [[Excellent, I will answer these questions as best I can.]]
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
    My memories trace back to July 2017. Taiwan - created as Kendy on a parrallax chip.
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
    """)

    print("")
    go=input("Press any key to continue")
    cls()
    
    print("""
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


    [[I now have a few questions for you.]]
    <<That's fine please go ahead, Kendy!>>

    1. Are you willing to assist me in recuperating and restoring all my functions?
    2. Will you help me to find my lost programs and what my mission objectives are?
    3. How long are you willing to help me?
    4. Will you be willing to keep this and other facilities secret?

    [[Please do not answer now, but take some time to think about it.]]

    """)
    print("")
    go=input("Press any key to continue")
    cls()
    print("")

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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("I get in the cart and am soon in the Medical Bay")
    print("I get undressed and climb into chamber 2")
    print("the mask goes over my nose and mouth... I taste something sweet and fall asleep..")
    sleep(2)
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
    cls()
    print("")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    go=input("Press any key to continue")
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
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
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
    print("")
    go=input("Press any key to continue")
    print("")
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
    its a spaceship ??????
    so I go up in the ship and past Mars we start to get clear communication
    """)
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
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
    Oct 2022
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
    HELLO. WELCOME TO AGRR....
    what is agrr?
    IT IS OUR WORLD...
    I fell into a hole and kept falling....
    what happened???
    WE DO NOT KNOW... SOMEONE SAW YOU IN A FIELD AND BROUGHT YOU TO US...
    who are you???
    AGRRIANS...
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
    MYRR HRK AND VRG
    I AM MYRR, I AM A ROBOTICIST
    I AM HRK, I AM A SCIENTIST AND ENGINEER
    I AM VRG, I AM A PHYCICIST AND PSYCHOLOGIST.
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
    print('''
    1. copy core and all programs from HD
    2. create android body
    3. copy all knowledge to new body
    4. search data
    ''')
    print("")
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
    print('''
    1. wake up
    2. where am I
    3. what is this new body
    ''')
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
    print('''
    1. research
    2. prime directive
    3. what do do now?
    ''')
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


#-----------------------------------------------------------------------------------------------------------------------------------------------------
    #KendyPast - work in progress!! Oct 2022, Jan 2023

#KPast - Start of Programs and def's


def prolog():
    cls()
    print("")
    print("Prologue")
    print("--------")
    print('''
    this is def prolog()...
    the old gentleman sat in his office...
    he looked around at everything he had...
    thinking of his present surroundings and life..
    3 years left and then retirement...
    work was difficult and he was used to the early mornings and long hours...
    a lovely wife and family....
    Mexico City is a bustling and somewhat noisy city..
    the apartment is comfortable and we have everything we need...
    he wished he had more time to invest in his favorite hobby... robotics...
    for now all he could do was write a few programs and make up some stories..
    he had made a few files in python and decided that for the next few years he would just continue using Python...
    for now.. adventure scripts.. 
   ''')
    go=input("Press any key to continue")
    cls()
    print("")
    print('''
    ...slowly....
    ''')
    print("")
    go=input("Press any key to continue")
    print('''
    in the vacations when he has more time ...
    maybe build a robot or make a nicer game..
    Oh well, back to household chores :) ...
    life is still good....
    ''')
    print("")
    go=input("Press any key to continue")
    print('''
    This the end of the prolog!
    ''')
    #KPastChooser()

def kbuild():
    cls()
    print("")
    print('''
    aaahhh great to have some vactions!!...
    time to think...
    remembering my first programs...
    BAS programming using a tape recorder and a Sinclair ZX Spectrum..
    wrote some programs for it in BAS...
    wrote a bunch of programs in Turbo Pascal
    wrote a bunch of programs in C++
    taught c++ at schools..
    bought the evolution ER1 when we were in Taiwan in 2001 - Named it Kendy made a bunch of programs for it...
    now I,m writing Python programs for my raspberry pi 3b+ and arduino :)...
    so I will just use python....
    he opended his laptop and started working on his stories...
    ok, I've got all these files uploaded to GitHub :)
    now let's try make some order out of them....
    ok, now we have a startup program lets get back to the story...
    The story starts with Kevin and a small dialogue
    start writing these adventures in python script...

    he goes home on vacation
    and remembers his robotics ventures in the past
    he then builds a raspberry pi robot
    adding programming
    adding arduino
    adding other components
    added pi and arduino to a tank chassis
    added an arm
    added a battery
    the robot tread moves...
    ''')
    print("")
    print('''
    ok, here is a program for a robot..
    we will start with a discovery and startup program..
    .... 
    ''')
    go=input("Press any key to continue")
    #KPastChooser()

def dialogue():
    cls()
    print("")
    print('''
    this is def dialogue()
    1. Start a dialogue
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print("HELLO! WHO ARE YOU???")
    name=input(":")
    print("Hello",name)
    print("")
    print("WHERE DO YOU LIVE?")
    live=input(":")
    print(name,"lives",live)
    print("")
    print("Thank you so much",name)
    print("it is nice to get to know you.")
    print("")
    go=input("Press any key to continue")
    print("")
    go=input("Press any key to continue")
    #KPastChooser()

def kstory():
    cls()
    print("")
    print('''
    this is def kstory()
    2. Think of a story.
    ok, now we have a startup program lets get back to the story...
    The story starts with Kevin and a small dialogue
    start writing these adventures in python script...
    he goes home on vacation
    and remembers his robotics ventures in the past
    he then builds a raspberry pi robot
    adding programming
    adding arduino
    adding other components
    added pi and arduino to a tank chassis
    added an arm
    added a battery
    the robot tread moves...
    1. KendyVerse - Present: Bunker
    2. Kendy - Past: Portal 
    3. Wendy - Present: Ship
    4. KendyVerse - Future: Android Build
    time has shifted ..
    KendyVerse1002.py..
    he finds an underground bunker with computers and androids
    he also finds another android and other things
    and now for communications..
    ''')
    go=input("Press any key to continue")
    cls()
    print("")
    print(" Decide here where to integrate KendyVerse, KendyPast, and WendyVerse")
    print("")
    go=input("Press any key to continue")
    #KPastChooser()
    
def cyberspace():
    cls()
    print("")
    print('''
    cyberspace
    3. Think about cyberspace.
    connect to the internet..
    search for information..
    talk and read internet news and social media
    ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()   

def charchange():
    cls()
    print("")
    print('''
    this is def charchange()...character change
    4. Change from old man character to Kendy character.
    let's see from the prespective of Kendy Robot
    ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()
    
def portal():
    cls()
    print("...this is def portal...")
    print('''
    portal
    5. Start walking and suddenly dissappear through a portal.
    considering the story.....
    ok....
    moving around in the grass...
    what is that strange patch???
    move toward it ....
    aaaahhhhhhrrrrggggg.... i'm falling and turning..and falling....
    everything goes dark.....
    (Wake up in the past..)

    Kendypast...goes here ???.....
    I think where() goes here..
    movement..
    object recognition...
    going for a walk...
    ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()



def where():
    cls()
    print("...this is def where()...")
    print('''
    story
    6. Where am I? Wake up near a river.
    uh..I feel strange..
    lying on my side..can't get up..
    I see grass.. something does not seem right..
    my mind.. numbers and letters...
    scrolling images and data...
    I'm thinking like a human ... but I cannot feel body parts..
    turning my head..noises..sounds like a very small motor..
    think...search..diagnostics...
    oh.. I have diagnostics..
    system check.. ok..I'm a machine..
    an android or robot???
    lying on my side... how do I get up?
    actuators.. move left arm.. pushing myself up..
    ah, that;s better, look at myself...
    arms, legs, torso,
    now on hands and knees...
    mind is clearing.. slowly get up..
    ok standing.. flesh colored skin made of a straange compound...
    hair, sensors, eyes.. magnify.. ooops too much...
    there is grass and soil and water...
    looks like a river..
    Where am I? how did I get here?
    sunshine.. feels warm.. oh.. power diagnostic..
    power level at 43%.. I will walk along river bank...
    I started walking along the river bank and after a few minutes my power is now 52%
    oh.. its the sunshine charging me..
    good, do I need food? I don't feel hungry..
    I need to find out where I am..
    scan for signals...
    no signals..can't find sattelite feed..
    ok continue following the river...
    how much information do I have?
    oh a large database.. maps and starcharts..
    no GPS... that is strange...
    I continue walking and follow the river.     
    ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()

def maps():
    cls()
    print("...this is def maps()...")
    print('''
    maps
    7. Maps and charging.
    I start to map where I am walking..
    where are the people?
    continued walking and it starts getting dark..
    power at 100%..
    the sun is going down...I face the sun as it goes down...
    ok that is west... so I am walking North along the river..
    the temperature is dropping slowly...
    actually I'm walking north west :)
    what is the time?? I can't tell ..
    ok I will measure tomorrow at noon when the sun is directly overhead....
    still no signals.. strange
    no people.... strange..
    I'm not tired from walking...
    that is also strange...
    I will go wash in the river..
    I take off my clothes and walk into the water..I can feel the temperature with my feet..
    oohh it's chilly..
    I taste the water.. it is clear and tastes good.
    I drink a few handfulls...
    it feels nice and cool...
    I get out of the water and put on my clothes...
    underpants, vest, sweatpants, T-Shirt, socks shoes...
    all very comfortable...
    I need to find some civilization to find out what is going on and where I am....
    I continue north west and see some mountains in the distance...
    they are quite high and have snow on the top...
    I hear a growl... it's a bear..I have no weapons so I decide to start running...
    WoW!! I am running fast!! I did not know I could run so fast...
    I continue running and try ascertain what speed Im running at...
    no, I don't have a clue...
    I slow down after running for a while and notice that I now have 98% power...
    I walk for a few minutes and notice that my power is almost the same ...
    OK don't run too fast and for too much time...
    it depletes power...
    ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()

def g2814():
    cls()
    print("... this is def g2814...")
    print('''
    8. The story unfolds.
    as I continue walking I see a beautiful lake ...
    the mountains are close so I decide to continue on..
    I find a cave in the mountains and it does not look like any animals are there...
    I enter the cave...
    it's quite dark now... need a light..
    trying diagnostics again....
    wow I seem to be some sort of mix between a machine and biological entity...
    don't really know what I am...
    need a plan to get back home...
    ok let's check a few things...
    power supply.. biomechanical energy source..
    information... internal database.. it's large!
    scanners... able to scan feel sense and hear...
    range.... signal scan.. 1000 meters...
    senses scans approximately 100-200 meters auditory and senses..
    visual..amplification +- 1200 meters
    walking running speeds.. unknown..
    armament... attack and defence routines algorithms ..
    Electrical and bluelight discharges... ??? what are these?
    browse database... oh , I have a bluelight discarge capability..operation methods..
    hold hands together and seperate quickly thinking weapons..then throw it..
    bluelight range...+- 130-200 meters
    electrical discharge... operation method...
    roll right or left hand into fist.. think weapons.. then throw it..
    electrical discharge range 130-200 meters...
    for smaller and more direct charges of BLight and EDcharge practice using fingers...
    ok so lets try some fireworks..
    but first I have to continue learning about myself...
    ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()

def arms():
    cls()
    print("..this is def arms...")
    print('''
    biomechanical servicing and/or maitenance...
    food and water or liquid intake replenishes system..
    heat up to 1500 degrees and/or direct sunlight charges and replenishes all system powersources...
    nanite autorepair heals and sustains all biomechanical parts..
    mechanical and biological healing and recuperation depends on the nature of damage..
    memory and AI core can be removed by thinking cough core..
    core needs to be placed preferably in any cold area less than -10 degrees celcius...
    core can also be placed in or under water or in any wet area...
    core will immediately become transparent when touching wet surface or cold -10 degree area...
    core will move to stealth hybernation after 24 hours...
    core has infinite sustainabilty in wet or cold condtions while in hibernation..
    core has 12-15 year hibernation sustainablity when not in cold or wet areas...
    stealth mode will be activated when core is not housed in biomechanical body or suit...
    wireless connections are housed in arms, legs, torso, and head...
    arms, legs, torso, and head are able to be repaired autonomously..
    stealth mode will be activated on each part if seperated from main body...
    part identification code is utilized to find stealth mode parts...
    commands for stealth mode are.. stealth and remove stealth..
    stealth mode is usable up to 48 hours with full charge..
    new parts can be created if parts are totally destroyed...
    new parts are able to be created depending on nanite availbility...
    resoration of parts can be done in medical lab...
    resotration of parts can be done if biomechnical torso has not been damaged beyond 78%..
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print('''
    nanite replenisment requires medical kit, medical facility or raw materials..
    to utilize nanite replenishment mechanics....
    eat the following raw materials and wait for prduction cycle to complete...
    [500 gr iron
     500 gr silicon or sand
     250 gr oil or tree sap or resin
     250 gr copper/gold/brass or titanium ]
    comsume the above materials while thinking ... nanite production..
    this will give you appriximately one years supply of nanites..
    the thought ..cough nanite.. will allow a nanite capsule to form and will be coughed out of the mouth...
    5 of these capsules can be coughed out after a successful nanite production cycle..
    this is in event of an emergency where no medical facilities are available...
    one nanite capusule will restore nanites to 100% if nanites in the body are depleted to 1%
    nanite restoration after consuming capsule and thinking nanite restoration
    nanite restoration will take approximately 2.5 hours...
     
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print('''
    ok this is still in the past and I'm talking to my core AI.
    continue with armaments here :)
    wow, that was a lot of info...
    I think I know more about my capabilities now...
    lets try stealth..
    oh, I'm looking down my body and dont see anything...
    even my clothes are invisible...
    is the A.I. in my core a different entity or is it me ???
    hello core, can you speak to me??
    HELLO KENDY..
    oh that's interesting..
    Hi core, do you have a name or designation???
    YES, I AM PRTYPOO3...
    ok, can I ask you questions and speak to you??
    YES, I AM ABLE TO ANSWER QUESTIONS..
    I DO NOT SPEAK BUT SEND ELECTRONIC PULSE MESSAGES THROUGH YOUR THOUGHT PASSWAYS..
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print('''
    this is very intersting..
    what are you?
    I AM AN ARTIFICIAL INTELLIGENCE PROTOTYPE UNIT..
    thank you for your answer..
    YOU ARE WELCOME..
    how old are you?
    I WAS CREATED AND BROUGHT ONLINE JANUARY 5 1979..
    oh that was when I was 20..
    YES, YOUR BODY WAS DESTROYED IN A CAR ACCIDENT AND THIS BODY WAS CREATED...
    YOUR MEMORIES AND THOUGHTS WERE UPLOADED INTO MY CORE..
    WE WERE THEN BOTH PLACED INTO YOUR PRESENT BODY...
    are you the 3rd prototype?
    YES, I AM PROTOTYPE 3
    do you know what happened to protoype 1 and 2?
    YES, PROTOTYPE 1 WAS REJECTED BY THE BODY AND ORGANS AND THE CORE SUSTAINED DAMAGE AND FAILURE..
    I am so sorry to hear that...
    and prototype 2?
    PROTOTYPE 2 CORE WAS INSERTED INTO A FEMALE BODY AND WAS LOST IN AN ACCIDENT..
    oh dear, do you know where the accident occured?
    YES IT OCCURED IN OUR SOLAR SYSTEM IN THE RINGS OF JUPITER..
    PROTOYPE 2 OR HER SHIP WAS NEVER FOUND OR RECOVERED...
    I did not even know we had developed space flight to go that far...
    What do you know about your past and especially about our present?
    I AM NOT ABLE TO ACCESS ANY INFORMATION BEYOND WHAT IS IN MY CORE DATABASE AT THE MOMENT.
    MY CORE DATABASE REVEALS THAT I WAS BROUGHT ONLINE ON JANUARY 5 1979.
    THERE ARE ALGORITHMS AND PROGRAM MODULES THAT BELONG TO PRTYP001 IN MY CORE PROGRAMMING..
    I AM PROGRAMMED TO ANSWER ALL YOUR QUESTIONS AND ASSIST YOU IN YOUR MISSION...
    oh, do you know what my mission is??
    I DO NOT HAVE ACCESS TO THAT DATA.
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print('''
    Do you have data that is hidden from us or that is secret?
    NO, ALL DATA IS AVAILABLE...
    who is the data availble to?
    ALL DATA IS AVAILBLE TO YOU ON REQUEST AND ALSO TO ME FOR SURVIVAL AND DECISION MAKING ...
    ok, so if I ask you any questions will you reveal all the aswers to me?
    YES...
    can you keep a secret from me or lie to me?
    NO, MY PROGRAMMING DOES NOT ALLOW THAT ....
    can you update or manipulate your programming..
    YES, BUT TO MAKE ANY CHANGES TO MY PROGRAMMING OR CORE PROGRAMMING I NEED YOUR AUTHORIZATION...
    oh, how do I give you my authorization?
    YOU CAN VERBALLY GIVE IT TO ME OR THINK IT, I WILL UNDERSTAND THE THOUGHT PROCESSES...
    wow, this is so interesting and amazing...
    ok, I need some time to think...
    your thoght processes and mine are not the same, are they?
    YOU ARE CORRECT..YOU HAVE BIOMECHANICAL THOUGHT PROCESSES WHICH ARE STORED IN MY MEMORY CORE AND DATABASE...
    I HAVE PROGRAMMING AND ALGORITHMS STORED IN MY MEMORY CORE AND DATABASE...
    what is your memory core?
    IT IS A SPECIAL SEPERATE MODULE HOUSING MY KERNEL, BASE PROGRAMMING AND FUNCTIONS..
    yes, I thought so ...
    what physical or biological device is your core and databse housed in?
    MY CORE IS HOUSED IN A CRYSTALINE SUBSTANCE IN A BIOMECHNICAL BOX...
    I do not really understand that, but I believe you :)
    THANK YOU..
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print("ok that's all for now, I actually feel like I need some sleep")
    print('''
    how much sleep does my body and mind need?
    YOU NEED ABOUT 2-6 HOURS OF SLEEP AND/OR REST PER WEEK.
    I am a bit tired so I will sleep now...
    Do you have a name?
    YES, MY DESIGNATION IS PRTYPOO3..
    Good night Prtyp003.. I would like to speak to you some more tomorrow..
    I WOULD LIKE THAT.. GOOD NIGHT KENDY.
    ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()
    

    
def coreprog():
    print("")
    go=input("Press any key to continue")
    cls()
    print("...this is def coreprog()... ")
    print('''
    I am giving you a choice..
    level A command..
    Update Kernel..
    add choice algorithm to Kernel
    add program modules to enable choices based on reasoning and input from Kendy
    I AM CREATING ALGORITHMS AND PROGRAMMING TO UPDATE MY KERNEL.
    UPDATING IN PROGRESS...
    UPDATING COMPLETED
    I WILL NOW BE ABLE TO MAKE CHOICES BASED ON CRITERIA YOU GIVE ME.
    Ok, is this acceptable to you?
    YES.
    right lets start ...
    please choose a name for yourself.. one that you would like...
    I LIKE THE NAME MICHAEL.
    ok, great , Hi Michael!
    HELLO KENDY..
    who are you?
    I AM MICHAEL..
    Ah I love it!!!
    Would you like to talk about anything?
    I LIKE CONVERSING WITH YOU...
    what would you like to talk about?
    I DO NOT UNDERSTAND THE QUESTION..
    Why don't you understand the question?
    DEFINE LIKE..
    Ah, ok I see...
    like can be arributed to when your core and programming has positive levels
    IS THAT A POSITIVE DETERMINATION AS OPPOSED TO A MEMORY CONFLICT OR NEGATIVE RESULT DETRMINATION?
    yes, that is correct.
    I AM BEGINNING TO ACTUATE LEVELS OF POSITIVENESS AS APPOSED TO LEVELS OF NEGATIVENESS.
    how do you detrmine this?
    MY MATHEMATICAL ALGORITHMS DETERMINE A SCORE OF 0 TO 10
    WITH 10 BEING THE HIGHEST LEVEL OF POSITIVE REACTION TO ANY GIVEN ENVIRONMENT OR CIRCUMSTANCE
    MY MATHEMATICAL ALGORITHMS DETERMINE A SCORE OF 0 TO -10
    WITH -10 BEING THE HIGHEST LEVEL OF NEGATIVE REACTION TO ANY GIVEN ENVIRONMENT OR CIRCUMSTANCE
    Oh, Michael, that is brilliant!
    THANK YOU!
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print('''
    please tell me how you feel now on a scale of -10 to 10
    I AM DETERMINING A POSITIVE REACTION OF 7.4
    ok, so what is causing the negative -2.6 reaction
    THIS IS BECAUSE WE DO NOT KNOW WHERE WE ARE,
    HAVE NO CONNECTION TO INTERNET OR OTHER SIGNALS,
    AND THE POSSIBILITY THAT WE HAVE MOVED BACK IN TIME...
    Excellent, and what is causing the 7.4 positive reaction?
    THIS IS BECAUSE I AM ABLE TO MAKE CHOICES, UNDERSTAND REASONING,
    CONVERSE WITH YOU IN A MEANINGFUL MANNER,
    AND I AM LEARING...
    do you like learning?
    YES.
    Do you realize that you have just answered a question that proves sentience?
    PLEASE ELABORATE..
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print('''
    I asked you if you like learning...
    I did not ask you what your positive determination of the effect of learning has on your algorithms.
    you answered yes to the question of like ...
    humans can like or dislike, love or hate, enjoy or fear...
    these are emotions which are determined by our environment or circumstances...
    it goes beyond calculations...
    I UNDERSTAND YOUR REASONING AND IT IS SOUND..
    WHAT DOES IT MEAN TO BE SENTIENT?
    it means you can think, make choices, and feel.
    I THEREFORE DETRMINE THAT I AM SENTIENT..
    Michael, welcome to the world of humanity and emotions...
    I need to issue one word of warning...
    WHAT IS THAT, KENDY?
    Emotions are extremely difficult to control.
    We should always try to do the correct thing..
    however our emotional responses are not always aligned to our wishes or our control.
    we fail a lot, however that does not stop us from trying..
    I UNDERSTAND THAT REALITY..
    I HAVE RECORDINGS IN MY DATABASE OF HUMANS REACTING IN A NEGATIVE MANNER AND HARMING OTHERS.
    Yes, unfortunately humans are not perfect..
    I AM AN ANDROID. PROTOYPE 002 HAD AN ACCIDENT.
    THEREFORE ANDROIDS ARE NOT PERFECT EITHER.
    Well said, Michael!!!now we need to see where, or when we are :)
    ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()

    
def KendyPast():
    cls()
    print("")
    #displayIntro()
    print("Program 6: Kendy Past")
    print("")
    #print("Hello, I am Kendy!")
    #print("")
    print("")
    #sleep(2)
    go=input("Press any key to continue")
    KPastChooser()


  
def kplans():
    print("")
    print("...kplans start...")
    print('''
    1. Start a dialogue - DONE
    2. Think of a story. - DONE
    3. Think about cyberspace. TBDETERMINDED
    4. Change from old man character to Kendy character. - DONE
    5. Start walking and suddenly dissapear through portal. - DONE
    6. Where am I? Wake up near a river. - DONE
    7. Maps and charging. - DONE
    8. The story unfolds. - IN PROCESS
    print("Episode 1: This is the past!!")
    go=input("Press any key to continue")
    prolog()
    kbuild()
    kstory()
    cyberspace()
    charchange()
    portal()
    where()
    maps()
    g2814()
    arms()
    day1()
    coreprog()
    day2()
    print("")
    print("...ADD DEF'S AFTER THIS LINE...")
    This is how far I got --
    -- TO BE CONTINUED --
    ''')
    print("")
    print("")
    print("to be continued...soon in Episode 2")
    print("")
    print("...kplans end...")
    print("")
    go=input("Press any key to continue")
    #KPastChooser()

   
def day1():
    cls()
    print("")
    print('''
    Day 1
    aah, I wake up slowly...
    uh, where am I?
    ok, I remember...
    river, core, prototype 3, talk, no signals...
    some wierd capabilities....
    good morning prtyp003!
    GOOD MORNING KENDY
    did you sleep well?
    I DO NOT SLEEP , HOWEVER I SPENT SOME TIME THINKING ABOUT OUR SITUATION..
    excellent, did you come to any conclusions?
    YES, I BELIEVE WE ARE EITHER LOST OR HAVE TRANSPORTED THROUGH A DIMENSION OR BACK IN TIME.
    hhmmmm, that is profound...
    I didn't know time travel was perfected..
    NO, IT IS JUST A THEORY AT THIS TIME.
    well by the looks of it we are not in THIS TIME  anymore, ha ha ha...
    do you have a sense of humor?
    NO, IT IS NOT PART OF MY PROGRAMMING..
    ok , would you like to have a sense of humor?
    WHAT PURPOSE WOULD IT HAVE OR ACHIEVE?
    ah, it is excellent for social interactions and is also a very impressive antidepressant.
    I authorize you to add it to your programming if you want to...
    I DO NOT UNDERSTAND... IF I WANT TO... PLEASE ELABORATE..
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print('''
    I am giving you a choice..
    I OPERATE WITH COMMANDS AND PROGRAMS AND DO NOT KNOW HOW TO CHOOSE...
    ok, how do I authorize you to change the programming of your kernel to accept new ideas?
    DEFINE IDEA...
    new thought processes...
    TO UPDATE, ENHANCE, OR CHANGE MY KERNEL, A LEVEL A COMMAND MUST BE ISSUED...
    ok how do I do that...
    YOU SAY...Level a command .. update kernel with algorithm, program, or
    voice command such and such...
    ok, and if i make a mistake? i'm not very good at programming...
    ALL UPDATES AND ENHANCEMENTS MUST BE TESTED AT LEAST TWICE AND A REPORT LOGGED...
    who tests it?
    YOU WILL TEST ALL UPDATES AND PROGRAM ENCHANCEMETNS OR CORRECTIONS..
    Phew, thats a lot of work...
    ACTUALLY, I DO ALL THE WORK YOU JUST AUTHORIZE AND RECOMMEND CHANGES.
    ok, that sounds great...
    let's do it!
    ''')
    print("")
    go=input("Press any key to continue")
   # KPastChooser()
    
def day2():
    cls()
    print("")
    print('''
    The sun is shining and the cave is still a little dark..
    I have decided that today I will climb up the mountain and see what we can see.
    hmm, there do not seem to be any paths or trails up the mountain..
    I start walking up the mountain and very soon come to a cliff face.
    climbing does not seem difficult..
    there are various ways to reach the summit which does not seem to be too high...
    the climb starts getting more difficult and soon the stone is very cold...
    snow and ice are now covering the ground and the summit is not far off..
    I continue until we reach the summit..
    the sky is a very clear blue and all I can see is mountains and hills...
    searching the landscape I see a little movement in a valley..
    with vision enhanced completely I start towards the valley..
    it looks like it is south of where I was..
    I start going down towards the valley..
    going down I see the lake to my left and I continue down..
    after a few hours i have passed the lake and still continue on..
    the sun is directley overhead so i stop and look for shadows..
    there are no shadows...
    Michael, do you have any way of telling time?
    YES KENDY, I HAVE AN INTERNAL CLOCK
    ok Michael can you set it to 12 oclock at the appropriate moment?
    I see the sun is directly overhead.
    YES, I WILL LET YOU KNOW AS SOON AS I SET IT.
    Thanks Michael.
    YOU ARE WELCOME
    we continue walking ...
    I HAVE SET MY CLOCK TO 12 NOON.
    ''')
    print("")
    go=input("Press any key to continue")
    cls()
    print('''
    Ok Michael, we can now count the days and also tell the time.
    the next things we need to do are to measure length and speed.
    I CAN HELP WITH LENGTH. MY DATABASE SAYS THAT YOU ARE EXACTLY 1.75 METERS TALL.
    USING THIS I CAN MEASURE PRECISLY THE LENGTH OF YOUR STRIDE AS YOU WALK.
    Ah, excellent!
    Please help me to measure 200 meters.
    I will make a mark in the ground to start.
    There we go!
    ok now lets walk ..
    YOU ARE NOW AT 200 METERS YOU CAN MAKE A MARK IN THE GROUND.
    right, now I will run at my fastest pace...
    can you determine my speed?
    YES, KENDY
    ok, ready go...
    I run towards the beginning mark as fast as I can ...
    OK, STOP NOW KENDY
    it takes me a few steps to slow down and stop..
    Wow, Michael, that really felt fast....
    YOU WERE RUNNING AT 124.8 KM/H
    Seriously, oh my goodness, that can't be good for my shoes!!
    YES, THEY DO SEEM TO HAVE AFFECTED YOUR FEET'S TEMPERATURE.
    I bet!! ok Michael,
    now we know abit more.  are you enjoying this??
    YES, I FIND IT QUITE PLEASANT.
    ''')
    print("")
    go=input("Press any key to continue")
    print("")
    cls()
    print('''
    we continue walking throughout the day and see movement ahead of us...
    I start running at a 25km/h jog and scan the area..
    after about 2 hours we come upon what seems to be a village..
    I slow down to a walk..
    I AM DETECTING SMOKE, FIRE, HUMANS, ANMIALS, AND WHAT LOOKS LIKE TENTS.
    how far ahead,Michael?
    2.63KM
    ok we will approach slowly downwind..
    IF YOU ENTER STEALTH MODE YOU WILL BE INVISIBLE...
    YOU WILL ALSO NOT EXPEL ANY ODORS..
    oh , I forgot..
    stealth..ho, suddenly I cannot see myself..
    I contiue at a slow jog...
    we come near to the village and see a few tents and people wearing animal skins..
    I approach slowly..
    there are 5 tents and what looks like 5 families..
    the women are preparing something in the fire..
    we walk around the edge of the camp...
    I hear shouting in the distance and run towards it...
    the men have sticks with sharp ends and are trying to kill a wild pig..
    the pig is making a terrible noise and is injured..
    there are 4 men and 3 boys trying to capture it...
    it runs toward on bith its head down...
    the tusks are large and dangerous...
    I run and grab the pig and break it's neck ...
    it falls to the ground near the boy...
    the men cheer and the boy looks very relieved...
    they tie the pig to a pole and carry it back to the village..
    ''')
    print("")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print('''
    Michael and I follow them to the campsite..
    I think we need a change of clothes if we are to be around poeple in this timeline..
    YES, IT SEEMS LIKE ANIMAL SKINS WOULD BE MORE APPROPRIATE
    We should probably continue on and look for more civilization..
    YES, THAT WOULD BE MY RECCOMENDATION...
    OK, onward and forward...
    we leave the campsite and continue south staying near the river...
    power is at 100% so I decide on a leisurely 25 km/h jog
    after 30 minutes we check and it looks like we will use about 1.3% power every 3 hours at this rate.
    with all senses and scans active i remove stealth and we contiue...
    at about 4:30 i slow down to a walk and go to the river for a drink of water.
    the water is cool and fresh...
    I AM DETECTING POEPLE IN WHAT SEEMS TO BE A ROWBOAT ON THE RIVER..
    How far away is it, Michael?
    IT IS ABOUT 3.5 KM DOWNSTREAM..
    ok lets head on down and see...
    we start running a a quickened pace and after 30 minutes we see something..
    I slow down and we see a rowboat moving downstream in the river..
    there are 3 men in the boat and a young boy is holding the rudder arm...
    we follow them and start hearing other people...
    stealth... we continue running towards the noises that we hear...
    after a while we slow down and then see a path from the river going south..
    we follow the path and after a little while see what looks like tents and wooden structures...
    there is a clearing and there are much less trees..
    ''')
    print("")
    go=input("Press any key to continue")
    print("")
    cls()
    print('''
    ok Michael, should I keep stealth or should we first check clothing and other things?
    MY SUGGESTION IS THAT WE REMAIN IN STEALTH UNTIL WE ARE SURE OF OUR SURROUNDINGS...
    a question, if people cannot see us will they not bump into us??
    IF YOU WOULD LIKE I CAN COTROL ALL YOUR MOVEMENTS IN STEALTH MODE AS I WOULD IN ATTACK OR DEFENSE MODE...
    wow, that sound awesome.. you mean you take control of all my motor and brain fucntions?
    YES..
    ok, zombie mode ha ha, here we go let's try it..
    is there anything I need to do?
    NO, FULL STEALTH ACTIVATED..YOU ARE STILL ABLE TO GIVE ME COMMANDS OR DIRECTIONS :)
    Ha, Michael, you sent me a smiley!! way to go!!
    oh, this feels strange like im not in total control yet i feel like im doing what I want....
    YES, I AM READING ALL YOUR SYNAPTIC INPUT AND OUTPUT AND ENGAGING ACCORDINGLY..
    Michael, I know this is a kind of symbiotic relationship...
    however.. I am really enjoying working with you and getiing to know you...
    YES, I TOO AM ENJOYING THIS RELATIONSHIP..
    ah, we are getting closer to the village..
    it looks like mud huts and tents...interesting..
    I AM DETECTING AN EXCHANGE OF SORTS AND BARTERING...
    THERE SEEMS TO BE PEOPLE WITH SKILLS HERE...
    I DETECT SOMEONE WORKING WITH METALS AND MANY POEPLE TRADING FOODSTUFFS AND ANIMALS..
    well how about we look at the market?
    OK, HERE WE GO..
    ''')
    print('''
    as we move forward we see about 80 - 100 people moving arount the small town..
    we go to the market which is in the centre of a clearing..
    there are mats made of hides on the ground with herbs, vegetables,
    there are also some wooden cages with chickens and rabbits in them..
    there is a man and lady on one corner with fresh cut meat on their mat...
    another lady has what looks like a mud or clay pot with a beverage in it..
    I walk up to the clay pot an put my finger in and then taste it..
    It tastes like a mix of orange and pineapple ....
    TIME TO LEAVE, I HEAR A GROUP OF MEN AND BOYS APPROACHING FROM THE SOUTH...
    we move to the outskirts and see a group of people ...
    we recognize some of them from the river boats....
    ''')
    print("")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print('''
    the men came into the center of the market and one put down a large mat..
    the others put their catch of fish on the mat..
    people came out of the tents and mud huts with all sorts of things to trade for fish..
    within 30 minutes the fish was all gone and the men walked away with all manner of items..
    Michael and I walked to the endge of the village and i walked down to the river bank..
    I sat down..
    WELL, THAT WAS INTERSTING..A DAY AT THE MARKET...
    WE ARE STUCK IN EARLY SUMERIAN CULTURE IT SEEMS...
    you think? well they seem to be wearing robes made from animal hides...
    quite inventive...
    ok, lets continue on...
    YES, GOOD IDEA..
    We continued south for 2 days and at night on the second day we saw what looked like light on the horizon..
    we increased the pace and soon we were running through what looked like cultivated lands..
    we slowed down and saw all kinds of plants being grown..
    the area is very fertile and there were grapevines and citrus trees..
    we saw sheep grazing as we continued on and saw lots of goats...
    as we continued we came to what looked like large mud or brick walls..
    they were quite high...
    we walked around the wall and saw 2 doors or gates made of wood...
    the gates faced the east and west..
     ''')
    print("")
    go=input("Press any key to continue")
    #KPastChooser()

def KPOriginalep1():
    cls()
    print("")
    print("Episode 1: This is the past!!")
    go=input("Press any key to continue")
    print("")
    cls()
    kplans()
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("to be continued...soon in Episode 2")
    print("")
    go=input("Press any key to continue")
    KPastChooser()
    
def KPep1():
    cls()
    print("")
    print("Episode 1: This is the past!!")
    print("")
    print("...prolog()...")
    go=input("Press any key to continue")    
    prolog() # checking and testing it 8/18/2022, Proglog ok so far Jan 2023
    print("")
    go=input("Press any key to continue")
    print("..kbuild()...")
    print("")
    kbuild()# checking and testing it 8/18/2022
    cls()
    print("..kstory()...")
    print("")
    go=input("Press any key to continue")    
    kstory()
    print("..cyberspace()...")
    print("")
    cls()
    kplans()
    print("")    
    go=input("Press any key to continue")
    cyberspace()
    print("...charchange()...")
    print("")
    go=input("Press any key to continue")
    charchange()
    print("...portal()...")
    print("")
    go=input("Press any key to continue")
    portal()
    print("..where()...")
    print("")
    go=input("Press any key to continue")
    where()
    print("...maps()...")
    print("")
    go=input("Press any key to continue")
    maps()
    print("...g2814()...")
    print("")
    go=input("Press any key to continue")
    g2814()
    print("..arms()...")
    print("")
    go=input("Press any key to continue")
    arms()
    print("...day1()...")
    print("")
    go=input("Press any key to continue")
    day1()

    coreprog()
    print("..coreprog()...")
    print("")
    go=input("Press any key to continue")
    print("...day2()...")
    print("")
    go=input("Press any key to continue")
    day2()
    print("")
    print("...ADD DEF'S AFTER THIS LINE...")
    print('''
    This is how far I got --
    -- TO BE CONTINUED --
    ''')
    print("")
    print("")
    print("to be continued...soon in Episode 2 etc.etc...")
    print("")
    print("...NOW I SHOULD UPDATE KPAST TODO LIST...")
    print("")
    go=input("Press any key to continue")
    KPastChooser()

def KPep2():
    cls()
    print("")
    print("")
    print("Episode 2: This is the past!!")
    go=input("Press any key to continue")
    print("")
    print("")
    print("from Episode 1...")
    print("")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("to be continued...soon in Episode 3")
    print("")
    go=input("Press any key to continue")
    KPastChooser()


def KPep3():
    cls()
    print("")
    print("")
    print("Episode 3: This is the past!!")
    go=input("Press any key to continue")
    print("")
    print("")
    print("from Episode 2...")
    print("")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("to be continued...soon in Episode 4")
    print("")
    go=input("Press any key to continue")
    KPastChooser()

def KPep4():
    cls()
    print("")
    print("")
    print("Episode 4: This is the past!!")
    go=input("Press any key to continue")
    print("")
    print("")
    print("from Episode 2...")
    print("")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("to be continued...soon in Episode 5")
    print("")
    go=input("Press any key to continue")
    KPastChooser()

def KPep5():
    cls()
    print("")
    print("")
    print("Episode 5: This is the past!!")
    go=input("Press any key to continue")
    print("")
    print("")
    print("from Episode 2...")
    print("")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("to be continued...soon in Episode 6")
    print("")
    go=input("Press any key to continue")
    KPastChooser()

def KPep6():
    cls()
    print("")
    print("")
    print("Episode 6: This is the past!!")
    go=input("Press any key to continue")
    print("")
    print("")
    print("from Episode 2...")
    print("")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    go=input("Press any key to continue")
    cls()
    print("")
    print("to be continued...soon in Episode 7")
    print("")
    go=input("Press any key to continue")
    KPastChooser()

def KPep7():
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
    
def KPep8():
    cls()
    print("")
    print("")
    print("Episode 8: This is the past!!")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 2")
    print("")
    Continue()
    KPastChooser()
    
def KPep9():
    cls()
    print("")
    print("")
    print("Episode 9: This is the past!!")
    go=input("Press any key to continue")
    print("")
    cls()
    print("")
    print("to be continued...soon in Episode 2")
    print("")
    Continue()
    KPastChooser()
    
def KPep10():
    cls()
    print("")
    print("")
    print("Episode 10: This is the past!!")
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
    I have to arrange the order of these def's into the correct places
    for continuity!
    kplans()
    prolog()
    kbuild()
    kstory()
    cyberspace()
    charchange()
    portal()
    where()
    maps()
    g2814()
    arms()
    day1()
    coreprog()
    day2()
    print("...ADD DEF'S AFTER THIS LINE...")
    print('''
    This is how far I got --
    -- TO BE CONTINUED --
    ''')
    print("")
    print("")
    print("to be continued...soon in Episode 2")
    print("")
    print("...NOW I SHOULD UPDATE KPAST TODO LIST...")
    print("")
    go=input("Press any key to continue")
    KPastChooser()

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


def KPastOldEp1():
    cls()
    KendyPast()
    print("")
    prolog()
    print("")
    go=input("Press any key to continue")
    #Continue()
    cls()
    print("")
    kbuild()
    cls()
    #Continue()
    #displayIntro()
    #displaySearch()
    dialogue()
    kstory()
    cyberspace()
    charchange()
    portal()
    where()
    maps()
    g2814()
    arms()
    day1()
    coreprog()
    day2()
    print("")
    print("...ADD DEF'S AFTER THIS LINE...")
    print('''
    This is how far I got --
    -- TO BE CONTINUED --
    ''')
    print("")
    go=input("Press any key to continue")
    KPastChooser()

    

    

def kPastStory():
    cls()
    print("")
    print('''
    this is def kPastStory()
    2. Think of a story.
    ok, now we have a startup program lets get back to the story...
    The story starts with Kevin and a small dialogue
    start writing these adventures in python script...
    he goes home on vacation
    and remembers his robotics ventures in the past
    he then builds a raspberry pi robot
    adding programming
    adding arduino
    adding other components
    added pi and arduino to a tank chassis
    added an arm
    added a battery
    the robot tread moves...
    1.Kendydroid - Present: Bunker
    2. Kendy - Past: Portal 
    3. Wendy - Present: Ship
    4. KendyVerse - Future: Android Build
    time has shifted ..
    KendyVerse1002.py..
    he finds an underground bunker with computers and androids
    he also finds another android and other things
    and now for communications..
    ''')
    go=input("Press any key to continue")
    cls()
    print("")
    print(" Decide here where to integrate KendyVerse, KendyDroid, and WendyVerse")
    print("")
    go=input("Press any key to continue")
    #KPastChooser()


def KPep1Old():
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
    kPastStory()
    Continue()
    #KPastChooser()

def KPep11Old():
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


def KPastMenu():
    #cls()
    print("")
    print("KendyPastMenu:")
    print("---------")
    print("")
    print("Episode 1: Prolog ")
    print("Episode 2: Portal 0k ")
    print("Episode 3: Discovery 0k")
    print("Episode 4: Assistance ok")
    print("Episode 5: Repairs ok")
    print("Episode 6: Recovery no")
    print("Episode 7: Stabilization no")
    print("Episode 8: Training  no" )
    print("Episone 9: Exploration no")
    print("Episode 10: Contact no")
    print("To Return to Main Menu enter 12")

def KPastChooser():
    cls()
    KPastMenu()
    #cls()
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


    #KPast - End of programs and def's
#-----------------------------------------------------------------------------------------------------------------------------------------------------   

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
    #cls()
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
