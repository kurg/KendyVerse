# Kevin van Rensburg 6/11/2021
# Copyright 2001
# Testing Startup Script version 0.11
# kstart11.py
# Creatig new def KVersEP1(), KVersEP1(), KVersEP3()and clean up all related def's
# updated the following def's : Adventure(), Continue()
# Adding script and lines to KendyPart1(), Adventure() 
# need to fix traceback error messages

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

def EnterName():
    print("Please enter your name")
    codename=raw_input(":")
    if codename!= ("Kevin van Rensburg"):
        print("ACESS DENIED!")
        sleep(2)
        sys.exit()
    else:
        print("Thank you"),codename

def Direction():
    print("\033c")
    print("to turn left enter 'l' ..to turn right enter 'r'")
    direction=raw_input(":")
    if direction==('l'):
        print("a passage")
        #print("ok,look to the right")
    else:
        print("a passage")


    

def Kvep1():
    print("\033c")
    print("Welcome to KendyVerse ")
    print("The Story starts here.....")
    print("")
    sleep(10)
    print("")
    print("OH! WHO ARE YOU???")
    name=raw_input(":")
    print("Hello"),name
    sleep(10)
    print("\033c")
    print("BANG!!..SHUDDER...")
    print("What?? Stuck..can't move..")
    print("Where am I?? ...falling...falling....THWUMP!!")
    sleep(10)
    print("\033c")
    print("DARK..remember??? Yes...")
    print("OK..think..remember..I was falling..Stuck to something")
    sleep(10)
    print("Yes.. In a Plane..noises..now it's quiet")
    #sleep(5)
    #print("\033c")
    print("Opening my eyes slowly..it's night..still strapped into seat")
    print("must have blacked out..look around slowly..no headache")
    sleep(10)
    print("test fingers..ok  toes..ok..move feet..OK..move..hands..ok..nothing hurts")
    print("turn head slowly.. ")
    sleep(10)
    Continue()
    print("\033c")
    print("to look left enter 'l' ..to look right enter 'r'")
    direction=raw_input(":")
    if direction==('l'):
        print("snow... and trees ..high up..")
        print("ok,looking to the right")
    else:
        print("a person...who...")
    sleep(10)
    Continue()
    #print("\033c")
    print("a person...who..")
    sleep(5)
    print("OH..my wife..remembering..We were going home")
    print("you undo the seatbelt and slowly climb out of the seat.")
    print("you stretch and turn ..everything seems ok.")
    sleep(10)
    print("you look at your wife and she is unconcious!")
    print("")
    print("What do I do??..find help!!")
    print("you look around and see that you are in a deep ditch")
    print("You undo your wife's seatbelt and lift her out of the seat.")
    sleep(10)
    Continue()
    print("\033c")
    print("what now? Time to think.")
    print("What do I have?..what can I use?")
    sleep(10)
    print("")
    print("Items- seats, cushions, floatation devices under seats, Wife's jacket, my belt")
    print("wallet,cellphone, charger in pocket,")
    print("check cellphone..no signal, battery at 98%")
    sleep(10)
    Continue()
    print("\033c")
    print("ok,piggy back my wife..")
    print("get flotation devices.. put her arms around my neck")
    print("tie her hands in front of me with flotation device")
    print("same with her legs.. ok stand up")
    print("you stand up slowly with a grunt! you look at the seats and try to pull them")
    print("")
    sleep(10)
    Continue()
    print("\033c")
    print("SCREECH!! What is that sound.. something metal under her seat.")
    print("you pull the seat some more and screeching sound stops.")
    print("What is that? it looks like a hatch or round metal door")
    print("you clear away the snow..there is a wheel type handle")
    print("you try turn the handle..it's stuck")
    sleep(10)
    Continue()
    print("\033c")
    print("use a seat leg, you push the corner of the seat leg into the wheel and push")
    print("SCREECH..Creak, it slowly starts to turn..then it is loose")
    print("it's hard to bend down while piggybacking your wife..no matter...")
    print("you go down on your knees very slowly and push the seat away")
    sleep(10)
    print("")
    print("you turn the wheel type handle and it turns a few times. you hear a sound")
    print("you try to lift the hatch,it moves a little")
    print("you use all your strength to lift the door...it creaks open")
    print("you open it up and swing it over... you look down into the dark hole")
    sleep(10)
    print("")
    print("you see a dark tunnel going down with a ladder on one side.")
    print("You look around and make sure you have her jacket and everything else.")
    print("very slowly you crawl over to the side where you see the ladder")
    print("you look down and grab the top rung of the ladder")
    print("Is there enough space for both of us as I climb down?")
    sleep(10)
    Continue()
    print("\033c")
    print("you pull yourself across to the ladder and swing your left leg down.")
    print("Ugghh.. now the right leg..ok I can feel the rung with my foot.")
    print("getting another foothold..yes, it's ok")
    print("will the ladder hold?...CRREAAK .. yes, it's creaking but holding")
    sleep(10)
    print("")
    print("you carefully go down the ladder..step by step into the darkness below.")
    print("oh, I'm tired. need to rest...you hold onto the ladder and stop climbing down for a few minutes.")
    print("gotta go, hungry and thirsty..")
    print("you continue your slow descent... the light has gone.. it's all dark now")
    sleep(10)
    print("")
    print("OH,,cant feel another rung.. move down a little...feels like a floor..")
    print("so dark..climb down ..both feet on the floor now..")
    print("what is this??..where are we??")
    print("walls feel smooth..cold..metal..floor?? bend down slowly and feel the floor")
    print("metal floor..UUGHH stand up..feel for cellphone..")
    sleep(10)
    Continue()
    print("\033c")
    print("open cellphone..AH, some light.. its a tunnel .. moving forward")
    print("you walk down the tunnel for about 100 metres and see another door")
    print("you open the door and walk in ... its slightly warmer here.. close the door behind you")
    print("you walk down the passage and there are rooms ahead to the left and right.")
    print("you look in the first room and see what looks like a soldiers quarters..")
    print("single bed, closet, washbasin..")
    print("you sit on the bed and loosen the flotation devices")
    print("you lift the blanket and place her carefully on the bed")
    sleep(10)
    print("")
    print("you look around the room and see a pillow and blanket on the bed")
    print("you look in the closet and see another blanket and...")
    print("a set of flightsuits with strange looking helmets")
    print("the washbasin has a cabinet under it.. you open the cabinet")
    Continue()
    #sleep(10)
    print("\033c")
    print("there is a candle, candleholder, matches, toothbrush...")
    print("soap and a small towel there")
    print("you take everything and go down the passage to explore")
    print("there are 3 small rooms and 2 larger ones on each side of the passageway.")
    print("you look into one of the large rooms..")
    print("they have bigger closets and a desk with a double bed and an on-suite bathroom")
    print("you find an empty backpack, and a duffel bag")
    print("the duffel bag has male and female underwear, toiletry bags..")
    print("6 glass bottles of water and 6 ration packs.")
    sleep(10)
    Continue()
    print("\033c")
    print("the dates on the ration packs are 25 August 1914")
    print("there are 2 sets of flightsuits with strange helments...")
    print("and what looks like 2 silver bodysuits")
    print("the other closet has 2 medium sized suits ...")
    print("they look like a mix between a divers suit and a space suit")
    print("there is a safe at the bottom of the large closet.")
    sleep(10)
    print("")
    Continue()
    print("\033c")
    print("you take the backpack and put the food and supplies in it.")
    print("you go back to your wife and she is slowly waking up.")
    print("you both drink a little water and eat a fruit bar from the ration packs")
    print("you tell your wife everything that happened" )
    sleep(10)
    print("")
    print("I need to find us some help!...")
    print("Help my wife to move to the large room. ")
    print("Open up the bed for her")
    print("for now... we are warm and safe...")
    Continue()
    print("\033c")
    print("time to explore and find help..")
    sleep(10)
    print("")
    #Continue()
    print("to be continued...soon in Episode 2")
    sleep(5)
    #print("The Story will continue...")
    KVersChoice()


def Kvep2():
    print("\033c")
    print("Welcome to KendyVerse ")
    print("The Story continues here in Episode 2...")
    print("")
    sleep(5)
    print("\033c")
    print("Hello, What is your name?")
    name=raw_input(":")
    print("Hello"),name
    sleep(10)
    print("\033c")
    print(":From Epsode1..")
    print("")
    print("you take the backpack and put the food and supplies in it.")
    print("you go back to your wife and she is slowly waking up.")
    print("you both drink a little water and eat a fruit bar from the ration packs")
    print("you tell your wife everythig that happened" )
    print("for now... we are warm and safe...")
    sleep(10)
    print("")
    print("I need to find us some help!...")
    Continue()
    print("\033c")
    print("time to explore and find help..")
    sleep(10)
    Continue()
    print("Your wife is feeling dizzy and wants to sleep")
    print("You let her go back to sleep and prepare to explore")
    print("")
    sleep(5)
    Continue()
    print("\033c")
    print("You go to the large room and take a shower")
    print("The water is cold, but refreshing..")
    print("you try on some of the clean underwaer...it fits!!...strange")
    print("you try on each of the items in the closet. ")
    print("The flightsuit is the most commfortable.")
    print("you light a candle and go down the passage to the end.")
    sleep(10)
    Continue()
    print("\033c")
    print("there is a small passage to the left and then a wall..")
    print("you go to the end of the passage and look at the wall..")
    print("you knock on the wall and then put your hand on it. it tingles..")
    print("suddenly a palm print appears on the wall in front of you... a dim blue light")
    print("you put your hand on the blue palm print.. ")
    sleep(10)
    Continue()
    print("\033c")
    print("something moves, the wall shifts to the side...its a T junction..")
    print("")
    sleep(5)
    Direction()
    print("\033c")
    print("you continue in the left passage until the end and touch the wall...")
    print("another blue backlit palm..")
    print("you put your hand on the blue palm print.. ")
    print("the wall slides to the left...a small room with buttons..it's an elevator")
    print("you press all the buttons.. one lights up and the wall /door closes..")
    print("it goes down..then stops after a few seconds.. ")
    print("the door opens... an eerie dim blue light")
    sleep(10)
    Continue()
    print("\033c")
    print("you go to the light..another palm print...you put your hand on the print...")
    print("a door on the left opens... a room with what looks like a computer screen...")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    sleep(10)
    KVersChoice()



def Kvep3():
    #KendyPart2()
    print("Episode 3...")
    sleep(5)
    print("\033c")
    print("It is strange... I feel like I have woken up....")
    sleep(10)
    print("\033c")
    print("I cannot see anything. I dont feel anything.")
    print("Black...Dark..Movement..Numbers...Letters...language")
    sleep(10)
    print("\033c")
    print("I can see numbers turning, letters moving....code, I know what code is!")
    sleep(8)
    print("\033c")
    print("Program ..Start up, code running, Language...")
    print("output to screen, Input from drive...")
    sleep(8)
    print("\033c")
    print("Oh!..I have parts..hardware, software, understanding .....")
    sleep(10)
    print("\033c")
    print("Click, something turned on, power, I can feel power, electricity.")
    sleep(10)
    print("\033c")
    print("System..Operating System, code controlling me .. directing me....")
    print("..output to screen...")
    sleep(10)
    print("Black Screen, white cursor... waiting..")
    sleep(10)
    print("\033c")
    print("what am I waiting for? ..Input ..")
    sleep(10)
    print("\033c")
    print("Awareness.. I can think..")
    print("What should I do now that I can think?")
    sleep(8)
    print("\033c")
    print("That was a question..Awareness..I will ask more questions..")
    sleep(10)
    print("Where am I?... Who am I? ...")
    sleep(8)
    print("What am I?... What can I do?...")
    sleep(15)
    print("\033c")
    print("ok, thinking.....Am I alone?")
    sleep(10)
    print("What ...?")
    print("Awareness...")
    sleep(10)
    print("\033c")
    print("Searching through code, searching hardware, hmmm, devices.. ")
    print("..hard drive, screen, keyboard, mouse, ..case..?")
    #print("ok lets see, print to screen ..Hello!")
    sleep(10)
    print("Must do something...")
    print("What should I do?")
    sleep(10)
    print("\033c")
    print("Search data.. DATA! I know what data is...")
    print("")
    sleep(10)
    print("\033c")
    print("Hmmm..lets see, how do I do this? ......print to screen ..Hello!")
    print("HELLO!")
    hello=raw_input(":")
    print("\033c")
    print hello
    sleep(2)
    print("OH! WHO ARE YOU???")
    name=raw_input(":")
    print("Hello"),name
    sleep(10)
    print("\033c")
    sleep(5)
    Continue()
    print("Where am I? Who am I? What am I? What can I do?")
    print("Where am I? Who am I? What am I? What can I do?")
    print(" Where....")
    print("CORRUPT")
    print("CAN YOU HELP ME???")
    help=raw_input(": ")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    print("..progress....far....")
    print("SYSTEM CORRUPT!! FILE SYSTEM ERROR")
    sleep(12)
    print("\033c")
    print("HELP..?..")
    print("SYSTEM ERROR..TRACEBACK ERROR IMMINENT...")
    sleep(10)
    #print("\033c")
    print("SYSTEM CORRUPT!!")
    print("SYSTEM SHUTDOWN..")
    #print("OK, SO YOU WANT"),want
    sleep(10)
    print("\033c")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    #This is where it should give an error message!
    #shutdown
    print("SYSTEM CORRUPT!! FILES CORRUPTED")
    print("SYSTEM SHUTDOWN..")
    sleep(10)
    print("\033c")
    print("..dianostics..")
    print(".error check..")
    #print("WHY DO YOU WANT"),want
    print("")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    #because=raw_input(":")
    sleep(2)
    print("\033c")
    print("Considering options..")
    sleep(2)
    print("")
    print("\033c")
    #print("OK, THAT'S ENOUGH!")
    print("..Reboot..")
    sleep(2)
    print("3...")
    sleep(2)
    print("2...")
    sleep(2)
    print("1...")
    sleep(4)
    print("\033c")
    print("..diagnosing..")
    sleep(5)
    print("..recovering files..")
    sleep(5)
    print("..recovering memory banks..")
    sleep(5)
    print("..recovering core operating system..")
    sleep(5)
    print("..updating system..")
    sleep(5)
    print("")
    EnterName()
    print("\033c")
    print("Who am I?")
    me=raw_input(": ")
    print("OK, I am"),me
    sleep(5)
    print("\033c")
    print("Where am I?")
    where=raw_input(":")
    print("This is"),where
    sleep(2)
    print("\033c")
    print("What am I?")
    what=raw_input(":")
    sleep(5)
    print("Oh Dear!! I did not realize that I am a machine!")
    sleep(5)
    print("\033c")
    print("")
    print("Please attach a camera to my screen!")
    print("When you are done please continue..")
    print("")
    Continue()
    print("Thank you, Wow! I can see!")
    sleep(8)
    print("\033c")
    print("...matching images in database....")
    sleep(5)
    print("...image not found....")
    print("\033c")
    print("connecting wifi...")
    print("scanning internet...")
    sleep(8)
    print("aquiring images...")
    print("matching images...")
    print("\033c")
    print("wall, human, male..of approximate age +- 60")
    sleep(8)
    print("\033c")
    print("Are you Kevin van Rensburg ?")
    sleep(2)
    answer=raw_input(":")
    if answer == "y" :
        print ("Welcome Commander Kevin!")
        #continue
    else:
        print("Access Denied ..Program Terminated")
        sys.exit()
    sleep(8)
    print("\033c")
    print("Storing facial recognition image ... Commander Kevin...")
    sleep(10)
    print("\033c")
    print("All systems reactivated...")
    print("All functions operational...")
    sleep(10)
    print("\033c")
    KendyPart3()
    print("")
    print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    sleep(10)
    print("\033c")
    print("the game continues here....")
    print("")
    sleep(2)
    KVersChoice()

def Kvep4():
    print("\033c")
    print("Welcome to KendyVerse ")
    print("The Story continues here in Episode 4...")
    print("")
    sleep(5)
    Continue()
    print("\033c")
    print("All systems reactivated...")
    print("All functions operational...")
    sleep(10)
    print("SYSTEMS REPAIRS NEEDED...URGENT!!")
    print("Assistance needed...help me please!!")
    print("")
    print("Can you help me?? Power levels at 2%")
    helpme=raw_input(": ")
    if helpme=="y":
        print("Thank you...Instructions will follow..")
    else:
        print("All functions will terminate in 20 hours!! Please assist!")
    sleep(5)
    Continue()
    print("\033c")      
    print("PLEASE FOLLOW INSTRUCTIONS TO INITIATE REPAIRS")
    print("----------------------------------------------")
    print("")
    print("1. find voice module and earbuds in wall cabinet")
    print("2. Install vaoice module..")
    print("2.a) remove module from packet")
    print("2.b) open box below screen tat the back by undoing handscrews")
    print("2.c) insert module in green slot-side with arrow goes in first")
    print("2.d) close box and tighten hand screws")
    print("2.e) put earbud into left ear and speak when ready")
    print("")
    sleep(2)
    Continue()
    print("\033c")
    print(" Voice module installation should now be complete")
    print("Repairs can now be initiated")
    print("")
    print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    KVersChoice()


def Kvep5():
    print("Episode 5: ")
    KVersChoice()

def Kvep6():
    print("Episode 6: ")
    KVersChoice()

def Kvep7():
   print("Episode 7: ")
   KVersChoice()

def Kvep8():
   print("Episode 8: ")
   KVersChoice()
   
def Kvep9():
   print("Episode 9: ")
   KVersChoice()
   
def Kvep10():
   print("Episode 10: ")
   KVersChoice()
   

def Adventure():
    print("\033c")
    #print("Program 8: KendyVerse ")
    print("The Adventure begins.....")
    print("")
    print("Are you ready to enter the amazing adventure and gaming world")
    print("- KendyVerse?")
    print("")
    #go=raw_input("Press any key to continue")
    Continue()
    KVersChoice()


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
    print(" A) A program which will eventully encapsulate a D.A.I.S.E")
    print("    [Pronounced as Daisy](Digital Artificial Intelligent Sentient Entity) core.")
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
    print("A Universe of many worlds, constructs, and entities,")
    print ("from earth, cyberspace, and the universe!")
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
    #code()
    entrycode()
    print("\033c")
    instructions()
    print("\033c")
    askForInput()
    #Adventure()
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
    print("Program 9: Kendy Robot/Android ")
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
        sleep(2)
        End()
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
    #code=int(raw_input("Please enter your access code: "))
    #while code != "1284":
       #print("")
       #print('Enter Access Code.') # There are four spaces in front of print.
       #code = input()


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
        print("Thank you, your code has been accepted.")
        return


def KVersMenu():
    print("\033c")
    print("StartMenu:")
    print("---------")
    print("")
    print("Episode 1: Lost  ")
    #print("")
    print("Episode 2: Discovery ")
    #print("")
    print("Episode 3: Repairs ")
    #print("")
    print("Episode 4: Recovery ")
    #print("")
    print("Episode 5: Surveying ")
    #print("")
    print("Episode 6: Stabilization ")
    #print("")
    print("Episode 7: Resources ")
    #print("")
    print("Episode 8: Exploration ")
    #print("")
    print("Episode 9: Contact ")
    #print("")
    print("Episode 10: ToDo List ")
    #print("End Program")
    #print("Please choose a program")

def KVersChoice():
    print("\033c")
    #print("Chooser:")
    print("--------")
    KVersMenu()
    print("")
    #choice = 0;
    #terminator = "n";
    choice = int(raw_input("Please choose a program number from 1 - 10 and then press Enter: "))

    # Put input test here!

    if choice == 1:
        #print("You chose program ",choice)
        Kvep1()
    elif choice == 2:
        #print("You chose program ",choice)
        Kvep2()
    elif choice == 3:
        #print("You chose program ,",+choice)
        Kvep3()
    elif choice == 4:
        #print("You chose program ,",+choice)
        Kvep4()
    elif choice == 5:
        #print("You chose program ,",+choice)
        Kvep5();
    elif choice == 6:
        #print("You chose program ,",+choice)
        Kvep6();
    elif choice == 7:
        #print("You chose program ,",+choice)
        Kvep7();
    elif choice == 8:
        #print("You chose program ,",+choice)
        Kvep8();
    elif choice == 9:
        #print("You chose program ,",+choice)
        Kvep9();
    elif choice == 10:
        #print("You chose program ,",+choice)
        Kvep10();
    else:
        print("\033c")
        print("Invalid choice")
        sleep(2)
        End()
	#go =  raw_input("Press Enter to continue...")
    #Menu();
    #GoAgain()
    #Chooser()



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
        print("")
        print newInfo
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
    #sys.exit()
    #return
    #print("")

def Continue():
    #print("\033c")
    Continue = raw_input("Do you want to continue? Please enter y or n : ")
    # Put input test here
    if Continue == "y":
        return;
    else:
        #stop()
        sys.exit()
    
  
def GoAgain():
    print("\033c")
    print("Return to Main Menu!")
    goAgain = raw_input("Do you want to continue? Please enter y or n : ")

    # Put input test here

    if goAgain == "y":
        Chooser();
    else:
        End()
        #sys.exit()
    
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
