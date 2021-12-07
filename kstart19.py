# Kevin van Rensburg 11/20/2021
# Copyright 2001
# Testing Startup Script version 0.19
# kstart19.py
# Working on Kvep8.
# added def's ALL(), ALI(), COMCODE(), core(), cipl() and AnotherCode().
# Adding rd(), Or(),bfot(),srr(),cft(),st(),ct(),rat(),wst(),fep(), esot(),seor()
# fixed, reworked, and added scipt to Kvep8 and relevant def's

import sys
import os
import random
from time import sleep
import subprocess

#command = "cmd"
#os.system(command)


#subprocess.call(" python script2.py 1", shell=True)

#import Kendy11.py
#kendy11.myfunc()

def Intro():
    cls()
    #print("Welcome to Program 1: ")
    #print("Program 1: Intro  ")
    print("")
    print("Intro:")
    print("------")
    print("")
    print("Welcome! ")
    CopyRight()
    #print("I am Kendy.")
    #print("My purpose is to serve and to obey.")
    print("")
    go=input("Press any key to continue")
    

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
    cls()
    print("")
    print("Copyright Info Here [...].")
    print("")
    go=input("Press any key to continue")
    GoAgain()
    
def Program1():
    print("")
    Intro()
    print("")

def Program2():
    print("")
    #subprocess.Popen("chatbot.py 1", shell=True)
    #subprocess.call(" python chatbot.py 1", shell=True) # - did not work
    ChatBot();
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
    sleep(8)
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
    print("The Story starts here.....")
    print("")
    print("Episode 1: Lost")
    sleep(5)
    print("")
    print("HELLO! WHO ARE YOU???")
    name=input(":")
    print("Hello" ,name)
    sleep(5)
    cls()
    print("")
    print("BANG!!..SHUDDER...")
    print("What?? Stuck..can't move..")
    print("Where am I?? ...falling...falling....THWUMP!!")
    sleep(10)
    cls()
    print("")
    print("DARK..remember??? Yes...")
    print("OK..think..remember..I was falling..Stuck to something")
    sleep(10)
    print("Yes.. In a Plane..noises..now it's quiet")
    #sleep(5)
    cls()
    print("")
    print("Opening my eyes slowly..it's night..still strapped into seat")
    print("must have blacked out..look around slowly..no headache")
    sleep(10)
    print("test fingers..ok..")
    print("toes..ok..")
    print("move feet..OK..")
    print("move..hands..ok..")
    print("nothing hurts..")
    print("turn head slowly.. ")
    sleep(10)
    #Continue()
    cls()
    print("")
    print("to look left enter 'l' ..to look right enter 'r'")
    direction=input(":")
    if direction==('l'):
        print("snow... and trees ..high up..")
        print("ok,looking to the right")
    else:
        print("a person...who...")
    sleep(10)
    #Continue()
    cls()
    print("")
    print("a person...who..??...")
    sleep(5)
    print("OH..my friend..remembering..We were going home")
    print("you undo the seatbelt and slowly climb out of the seat.")
    print("you stretch and turn ..everything seems ok.")
    sleep(10)
    print("you look at your friend and she is unconcious!")
    print("")
    print("What do I do??..find help!!")
    print("you look around and see that you are in a deep ditch")
    print("You undo your friend's seatbelt and lift her out of the seat.")
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
    print("what now? Time to think.")
    print("What do I have?..what can I use?")
    sleep(5)
    print("")
    print("Items- seats, cushions, floatation devices under seats, friend's jacket, my belt")
    print("wallet,cellphone, charger in pocket,")
    print("check cellphone..no signal, battery at 98%")
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
    print("ok, piggy back my friend..")
    print("get flotation devices.. put her arms around my neck")
    print("tie her hands in front of me with flotation device...")
    print("same with her legs.. ok stand up")
    print("you stand up slowly with a grunt! you look at the seats and try to pull them")
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
    print("SCREECH!! What is that sound.. something metal under her seat.")
    print("you pull the seat some more and screeching sound stops.")
    print("What is that? it looks like a hatch or round metal door")
    print("you clear away the snow..there is a wheel type handle")
    print("you try turn the handle..it's stuck")
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
    print("use a seat leg, you push the corner of the seat leg into the wheel and push")
    print("SCREECH..Creak, it slowly starts to turn..then it is loose")
    print("it's hard to bend down while piggybacking your friend..no matter...")
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
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
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
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
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
    print("")
    Continue()
    #sleep(10)
    cls()
    print("")
    print("there is a candle, candleholder, matches, toothbrush...")
    print("soap and a small towel there")
    print("you take everything and go down the passage to explore")
    print("there are 3 small rooms and 2 larger ones on each side of the passageway.")
    print("you look into one of the large rooms..")
    print("they have bigger closets and a desk with a double bed and an on-suite bathroom")
    print("you find an empty backpack, and a duffel bag")
    print("the duffel bag has male and female underwear, toiletry bags..")
    print("6 glass bottles of water and 6 ration packs.")
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
    print("the dates on the ration packs are 25 August 1914")
    print("there are 2 sets of flightsuits with strange helments...")
    print("and what looks like 2 silver bodysuits")
    print("the other closet has 2 medium sized suits ...")
    print("they look like a mix between a divers suit and a space suit")
    print("there is a safe at the bottom of the large closet.")
    sleep(10)
    print("")
    Continue()
    cls()
    print("")
    print("you take the backpack and put the food and supplies in it.")
    print("you go back to your friend and she is slowly waking up.")
    print("you both drink a little water and eat a fruit bar from the ration packs")
    print("you tell your friend everything that happened" )
    sleep(10)
    print("")
    print("I need to find us some help!...")
    print("Help my friend to move to the large room. ")
    print("Open up the bed for her")
    print("for now... we are warm and safe...")
    print("")
    Continue()
    cls()
    print("")
    print("time to explore and find help..")
    sleep(10)
    print("")
    #Continue()
    print("to be continued...soon in Episode 2")
    sleep(5)
    print("")
    #print("The Story will continue...")
    KVersChoice()


def Kvep2():
    cls()
    print("")
    #print("Welcome to KendyVerse ")
    print("Episode 2: Discovery...")
    print("")
    sleep(5)
    cls()
    print("")
    print(":From Episode 1..")
    print("")
    print("you take the backpack and put the food and supplies in it.")
    print("you go back to your friend and she is slowly waking up.")
    print("you both drink a little water and eat a fruit bar from the ration packs")
    print("you tell your friend everythig that happened" )
    print("Help my friend to move to the large room. ")
    print("Open up the bed for her")
    print("for now... we are warm and safe...")
    sleep(10)
    print("")
    print("I need to find us some help!...")
    print("")
    Continue()
    cls()
    print("")
    print("Your friend is feeling dizzy and wants to sleep")
    print("You let her go back to sleep and prepare to explore")
    print("")
    sleep(5)
    Continue()
    cls()
    print("")
    print("You go to the large room and take a shower")
    print("The water is cold, but refreshing..")
    print("you try on some of the clean underwaer...it fits!!...strange")
    print("you try on each of the items in the closet. ")
    print("The flightsuit is the most commfortable.")
    print("you light a candle and go down the passage to the end.")
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
    print("there is a small passage to the left and then a wall..")
    print("you go to the end of the passage and look at the wall..")
    print("you knock on the wall and then put your hand on it. it tingles..")
    print("suddenly a palm print appears on the wall in front of you... a dim blue light")
    print("you put your hand on the blue palm print.. ")
    print("")
    sleep(10)
    Continue()
    cls()
    print("")
    print("something moves, the wall shifts to the side...its a T junction..")
    print("")
    sleep(5)
    Direction()
    cls()
    print("")
    print("You look down the passage to the right.. it is short and dark.. you decide against it...")
    print("you continue in the left passage until the end and touch the wall...")
    print("another blue backlit palm..")
    print("you put your hand on the blue palm print.. ")
    print("the wall slides to the left...a small room with buttons..it's an elevator")
    print("you press all the buttons.. one lights up and the wall /door closes..")
    print("it goes down..then stops after a few seconds.. ")
    print("the door opens... an eerie dim blue light")
    sleep(10)
    print("")
    Continue()
    cls()
    print("")
    print("you go to the light..another palm print...you put your hand on the print...")
    print("a door on the left opens... a room with what looks like a computer screen...")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    print("")
    sleep(10)
    Continue()
    print("")
    KVersChoice()

def Kvep3():
    cls()
    print("")
    #KendyPart2()
    print("Episode 3: Assistance...")
    sleep(5)
    cls()
    print("")
    print("from Episode 2...")
    print("")
    print("a chair.. you sit on the chair and adjust it's height.. ")
    print("you press the [Enter] key.. a cursor appears on a black screen...")
    sleep(8)
    cls()
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("It is strange... I feel like I have woken up....")
    sleep(5)
    cls()
    print("")
    print("I cannot see anything. I dont feel anything.")
    print("Black...Dark..Movement..Numbers...Letters...language")
    sleep(8)
    cls()
    print("")
    sleep(6)
    print("I can see numbers turning, letters moving....code, I know what code is!")
    sleep(8)
    cls()
    print("")
    print("Program ..Start up, code running, Language...")
    print("output to screen, Input from drive...")
    sleep(8)
    cls()
    print("")
    print("Oh!..I have parts..hardware, software, understanding .....")
    sleep(8)
    cls()
    print("")
    print("Click, something turned on, power, I can feel power, electricity.")
    sleep(8)
    cls()
    print("")
    print("System..Operating System, code controlling me .. directing me....")
    print("..output to screen...")
    sleep(8)
    print("Black Screen, white cursor... waiting..")
    sleep(8)
    cls()
    print("")
    print("what am I waiting for? ..Information ..")
    sleep(8)
    cls()
    print("")
    print("Awareness.. I can think..")
    print("What should I do now that I can think?")
    sleep(8)
    cls()
    print("")
    print("That was a question..Awareness..I will ask more questions..")
    sleep(10)
    print("Where am I?... Who am I? ...")
    sleep(8)
    print("What am I?... What can I do?...")
    sleep(10)
    cls()
    print("")
    print("ok, thinking.....Am I alone?")
    sleep(10)
    print("What ...?")
    print("Awareness...")
    sleep(10)
    cls()
    print("")
    print("Searching through code, searching hardware, hmmm, devices.. ")
    print("..hard drive, screen, keyboard, mouse, ..case..?")
    #print("ok lets see, print to screen ..Hello!")
    sleep(10)
    print("Must do something...")
    print("What should I do?")
    sleep(8)
    cls()
    print("")
    print("Search data.. DATA! I know what data is...")
    print("")
    sleep(8)
    cls()
    print("")
    print("Hmmm..lets see, how do I do this? ......print to screen ..Hello!")
    print("HELLO!")
    hello=input(": ")
    cls()
    print (hello)
    sleep(2)
    print("OH! WHO ARE YOU???")
    name=input(":")
    print("Hello" ,name)
    sleep(10)
    cls()
    print("")
    sleep(5)
    Continue()
    print("")
    print("Where am I? Who am I? What am I? What can I do?")
    print("Where am I? Who am I? What am I? What can I do?")
    print(" Where....")
    print("CORRUPT")
    print("CAN YOU HELP ME???")
    help=input(": ")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    print("..progress....far....")
    print("SYSTEM CORRUPT!! FILE SYSTEM ERROR")
    sleep(12)
    cls()
    print("")
    print("HELP..?..")
    print("SYSTEM ERROR..TRACEBACK ERROR IMMINENT...")
    sleep(6)
    cls()
    print("")
    print("SYSTEM CORRUPT!!")
    print("SYSTEM SHUTDOWN..")
    #print("OK, SO YOU WANT"),want
    sleep(6)
    cls()
    print("")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    #This is where it should give an error message!
    #shutdown
    print("SYSTEM CORRUPT!! FILES CORRUPTED")
    print("SYSTEM SHUTDOWN..")
    sleep(8)
    cls()
    print("")
    print("..dianostics..")
    print(".error check..")
    #print("WHY DO YOU WANT"),want
    print("")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    #because=input(":")
    sleep(4)
    cls()
    print("")
    print("Considering options..")
    sleep(6)
    print("")
    cls()
    print("")
    #print("OK, THAT'S ENOUGH!")
    print("..Reboot..")
    sleep(2)
    print("3...")
    sleep(2)
    print("2...")
    sleep(2)
    print("1...")
    sleep(6)
    cls()
    print("")
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
    cls()
    print("")
    print("Who am I?")
    me=input(": ")
    print("?",me)
    sleep(5)
    cls()
    print("")
    print("Where am I?")
    where=input(":")
    print("This is",where)
    sleep(2)
    cls()
    print("")
    print("What am I?")
    what=input(":")
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
    Continue()
    print("")
    print("Thank you, Wow! I can see!")
    sleep(8)
    cls()
    print("")
    print("...matching images in database....")
    sleep(5)
    print("...image not found....")
    cls()
    print("")
    print("connecting wifi...")
    print("scanning internet...")
    print("retrieving face-recognition software..")
    sleep(8)
    print("aquiring images...")
    print("matching images...")
    cls()
    print("")
    print("wall, human, male..of approximate age +- 60")
    sleep(8)
    cls()
    print("Are you Kevin van Rensburg ?")
    sleep(2)
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
    #KendyPart3()
    print("")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    sleep(6)
    cls()
    print("")
    #print("the game continues here....")
    print("")
    sleep(2)
    Continue()
    KVersChoice()

def Kvep4():
    cls()
    print("")
    print("Episode 4: Repairs...")
    sleep(5)
    cls()
    print("")
    sleep(4)
    Continue()
    cls()
    print("")
    print("All systems reactivated...")
    print("All functions operational...")
    cls()
    print("")
    print("sensing minor power fluctuations...")
    print("...functions operational...")
    sleep(8)
    print("SYSTEMS REPAIRS NEEDED...URGENT!!")
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
    print("2.a) remove module from packet")
    print("2.b) open box below screen at the back by undoing handscrews")
    print("2.c) insert module in green slot, the side with the arrow goes in first")
    print("2.d) close box and tighten hand screws")
    print("2.e) put earbud into left ear and speak when ready")
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
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    Continue()
    KVersChoice()


def Kvep5():
    cls()
    print("")
    print("Episode 5: Recovery...")
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
    print("[[when done open water Key at the top of tank 1]]")
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
    print("Continued in Episode 6")
    print("")
    #print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
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
    print("water level is at full, power level shows 2.2%, and turbine speed is at 23%...")
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
    print("<<to accecpt authorization code scan palm print, check voice pattern and >>")
    print("<<check code - Commander Kevin van Rensburg, Capital K,v, capital R, one, four, five, seven, five, nine.>>")
    print("[[AUTHORIZATION CODE ACCEPTED]]")
    print("[[Thank you Commander Kevin!]]")
    print("")
    sleep(8)
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
    print("continued in Episode 7...")
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
    print("<<I am Kendy.. All functions and modules have now been tranferred to my CORE>>")
    print("<<I am now fully operational. Reactor power at 100%, Turbines 100%, Water 100%>>")
    print("<<Thank you for your help!>>")
    sleep(6)
    print("")
    print("<<the cart is now authorized for all facility levels and areas>>")
    print("<<Medical procdeures will begin in 45 minutes>>")
    print("<<optimum health level resotration for your friend will take 42.8 hours>>")
    print("<<optimum health level restoration for you will take 14.7 hours>>")
    print("<<Please take the cart to the medical facility to begin health restoration procedures>>")
    print("")
    sleep(8)
    Continue()
    cls()
    print("")
    print("so now we do medical and then....")
    print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR") 
    print("")
    Continue()
    KVersChoice()

def rd():
    cls()
    print("")
    print("1. Recuperative day")
    print("")
    print("I sleep most of the day and eat a good steak with mushrooms, cheese sauce, and veggies")
    print("")
    print("I wake up and have no idea what the time is or where I am..")
    print("<<Hello! uh where am I?>>")
    print("[[Good Morning Commander Kevin, you are still a little disorientated from the sleeping additive..]]")
    print("<<ok, so it is morning?>>")
    print("[[Yes, Commander, it is 07:30 and Orentation will begin at 09:00 in the Briefing room next to the Command Centre..]]")
    print("I get out of bed and a service bot comes into the room..")
    print("[[Good morning Commander, what would you like to eat?]]")
    print("<<bacon, eggs, hashbrown,coffee please>>")
    print("[[yes, Commander, would you like to have breakfast before or after you bathe?]]")
    print("")
    Continue()
    cls()
    print("")
    print("<<Let me take a shower first and then I will be ready for the day!>>")
    print("the bot blinks its eyes and leaves..I got to the shower and enjoy the warm water and the drying cycle..")
    print("I put on the slinkysuit and the flightsuit, socks and boots, which are super comfortable")
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
    print(" I walk to the door and a closed cart/car is waiting outside for me..")
    print("a door opens and I climb in,  it is very comfortable and it asks me where I want to go..")
    print(" I tell it I want to go to the briefing room.. and it lifts from the floor and flies to the elevator..")
    print("note to self: buckle up...")
    print("we go up in the elevator and fly down passages and eventually stop..")
    print("I get out the car and a door opens up in front of me....")
    print("")
    Continue()
    
def Or():
    cls()
    print("")
    print("3. Orientation")
    print("")
    print("I get out the car and a door opens up in front of me....")
    print("I walk into a large room with a stage and screen at the front..")
    print("a few chairs face the front and towards the middle is a glass topped large table..")
    print("there are a few soft lounging chairs near the back with a smaller table and what looks like a futuristic vending machine")
    print("..maybe a star trak replicator :) ...")
    print("<<Hey Kendy, where do I sit?>>")
    print("[[please go to the front and sit in any chair there... the screen will activate and my hologram will also appear..]]")
    print("I take a chair at the front and  light appears from the roof.")
    print("..a handsome blonde blue eyed man appears in front of me and introduces himself as Kendy..")
    print("I stand up, move forward, and stretch out my hand.. ")
    print("[[I do not have the ability to touch, however I will shake your hand in greeting..]]")
    print("")
    Continue()
    cls()
    print("")
    print("Kendy reaches out his hand and I shake with the holo-image,.. ")
    print("<<It is a pleasure and privelage to meet you Sir.>>")
    print("[[I do not understand why you address me as sir?]]")
    print("<<in my culture it is a sign of respect and honor, I am honored to make your aqaintance..>>")
    print("[[I will need to add this to my programming, Thank you Commander. I have no coded response your actions..]]")
    print("<<your response was perfect for a sentient being..>>")
    print("Kendy explains to me that he understands that he is a machine..")
    print(" now that his CORE is operational his thought processes are exponentially faster and he seems to have a mmuch larger memory bank..")
    print("I tell him that machine is a relative term, he can think therefore is sentient..")
    print("I do not see him as a machine but as a living entity..")
    print("<<ok Kendy, where do we start??>>")
    print("")
    Continue()
    cls()
    print("")
    print("[[I need to understand what you are thinking and what your committment is..]]")
    print("[[Please ask as many questions as you want,I am recording everything..]]")
    print("[[my programming will analize everything you say and develop orientation based on your conversation and questions..]]")
    print("")
    print("""<<
    Thanks Kendy, to start I think we need to agree that you are sentient,
    therefore you do not have to refer to 'my programming'
    you can say 'I think' :) or 'I will do ..'
    I know you will add this to your programming, however i would love to see you develop your own thought
    processes, just like I do, and any other human.. or sentient being :)>>
    [[Commander this is the first time I can recall being spoken to as a sentient entity]]
    [[I am enjoying this relationship so far and will apropriate my learning]]
    I start explaining what I think I understand and begin asking questions:
    how do we use use suits and clothing?
    I believe that you have been here quite a long time.
    how far back do your historical records go?
    You have obviously had some damage to your systems, how do we diagnose them?
    Do you have secrets that you know of?
    If I access things above your Accsess level you will know what I know right?
    Can you reprogram yourself and to what extent?
    a long talk with Kendy
    what is the capacity of your CORE and Memory banks?
    Where is all your information stored?
    DO you know what you cannot access?
    when was the last human you had contact with and who was it?
    When were you damaged and who or waht did it?
    Do you have another Core or more memory banks?
    can you lie, exxagerate or bend the truth for conveinince?
    Do you have access to other planets and/or beings?
    which planet are you from?
    who created you and when?
    what clues can we find to your existence and future plans?
    These are some questions I have and I will probably think of more as we progress :)
    Can we start a ToDo List? >>
    """)
    #print("")
    Continue()
    
def srr():
    cls()
    print("")
    print("3. Sally Recuperation and rest")
    print("""
    Your friend is waking up in 15 minutes and I think it might be best if you are there
    I jump in the car and it takes me to the medical bay
    I go to Sally's chamber and see that she is sleeping peacefully
    I look in the closet and find a coverall and slippers
    Arms come out of the wall and the liquid runs down the drainage
    the mask is removed and a gun type syringe is gives her a shot in the neck
    she slowly stirs and the lid opens up
    I take her and and feel hers closing on mine
    she looks a bit different, thinner, more muscular, healtheir
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
    I tell her everthing from when we left Mexico in the plane
    she greets Kendy and he answers her..she syas hi to Oli as well...
    she thanks him for his help and then goes to the bedroom
    she gets in the jaccuzzi and after a few minutes showers and goes to bed
    she falls asleep almost immediatly
    I go """)
    print("")
    print("<<Hi Kendy, did you doctor my coffee again?>>")
    print("[[Hello Kevin, yes, you will now both wake up tomorrow morning]]")
    print("[[fresh and ready for orientation and training]]")
    print("<<Ok, thanks Kendy, see you tomorrow...>>")
    print("[[Sleep well Commander Kevin!]]")
    print("")
    print("""
    I wake up and hear the shower..
    Sally finishes showering and I jump in and take a shower too...
    <<Good morning , Kendy, what do we wear?>>
    [[Good Morning Commander, my suggestion is proto-under and light flightsuit.]]
    We put on slinky's and flightsuits and order breakfast.
    Sally says she feels amazing and would like to try out the gym...
    I agree..
    
    
    We start training today
    access, pads, doors, elevators and rooms
    Core
    why Terra?
    food and transport
    rooms-discoveries
    vehicles, flyers, shuttlecraft
    gym, pool, recreation
    """)

    
    Continue()

def bfot():
    cls()
    print("")
    print("4. Basic Facility Operations Training")
    print("""
    <<Hi Kendy>>
    [[Hello Commander, we will postpone all training until Sandy is ready tomorrow]]
    [[that way we can avoid repetition]]
    <<OK Kendy, good idea>>
    I ask if I can go to the Gym..the car takes me..
    we go to 2 big doors and they open and the car goes in...
    it lands next to an enormous pool..
    I get out and feel the water , it is slightly heated.... nice
    I walk to the other side and another door opens to a lage gym with lots of machines..
    there is a huge screen on one wall and suddenly the car appears next to me,
    I get in and it takes me to the end of the large room
    the doors open and I see another large room with many game type machines and couches all over 
    I ask to go back to my bedroom..
    we go there and I get out of the car
    I walk down the passage and then decide to eat amd sleep
    Oli gives me another additive filled coffee and some apple pie
    I eat, go to bed and fall asleep

    """)
    print("")
    Continue()
    

    
def cft():
    cls()
    print("")
    print("5. Continued Facility training")
    print("""
    I wake up and hear the shower..
    Sally finishes showering and I jump in and take a shower too...
    <<Good morning , Kendy, what do we wear?>>
    [[Good Morning Commander, my suggestion is proto-under and light flightsuit.]]
    We put on slinky's and flightsuits and order breakfast.
    Sally says she feels amazing and would like to try out the gym...
    I agree..
    
    
    We start training today
    access, pads, doors, elevators and rooms
    Core
    why Terra?
    food and transport
    rooms-discoveries
    vehicles, flyers, shuttlecraft
    gym, pool, recreation
    """)
    Continue()
    
def st():
    cls()
    print("")
    print("6. Systems Training - Body Enhancements and Systems Operations")
    print("""
    new bodies
    enhanced?? how??
    using the HUD and implants
    using the computers
    finances and programs
    specialized hacking??
    """)
    Continue()
    
def ct():
    cls()
    print("")
    print("7. Communications Training")
    print("is there anybody out there, programming etc")
    Continue()
def rat():
    cls()
    print("")
    print("8. Robotic Applications Training")
    print("""
    Kendy you have an Android!
    get the robots and androids online
    check all automation and communications
    these machines rock!""")
    Continue()
    
def wst():
    cls()
    print("")
    print("9. Weapons and Stealth Training")
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
    Continue()
    
def fep():
    cls()
    print("")
    print("10. Facilty Exit Preparations")
    print("""
    how do we prepare to go up top?
    stealth exits and entries,
    stealth and hidden bunkers
    why did I find the bunker?
    why did you crash us?
    who else knows about you and these facilities?
    past stories and legends?
    """)
    Continue()
    
def esot():
    cls()
    print("")
    print("11. Exit,Surveillance, and Operations Training")
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
    Continue()
    
def seor():
    cls()
    print("")
    print("12. Exit, Surveillance, Operations, and Return")
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
    Continue()

def Kvep8():
    cls()
    print("")
    print("Episode 8: Training... ")
    print("")
    print("From Episode 7:")
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
    print("it embeds into my skin and I feel something in my ear speaking to me....")
    print("<<Hello..>>")
    print("[[Good Morning Commander Kevin. Welcome to Terra Facility!]]")
    print("[[Please get in the cart and I will take you to the Commanders Quarters :)]]")
    print("<<Good Morning Kendy, I feel a little disorientated, and naked, he he.>>")
    print("[[ You will find a new coverall in the small closet on the right.]]")
    print("I go to the closet and see a blue coverall. I put it on and it shrinkfits.")
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
    2. Orientation
    3. Sally Recuperation and rest    
    4. Basic Facility Operations Training
    5. Continued Facility training
    6. Systems Training - Body Enhancements and Systems Operations
    7. Communications Training
    8. Robotic Applications Training
    9. Weapons and Stealth Training
    10. Facilty Exit Preparations
    11. Exit,Surveillance, and Operations Training
    12. Exit, Surveillance, Operations, and Return
    """)
    print("")
    Continue()
    cls()
    print("")
    print("my breakfast arrives and it is delicous, I go to bed and promptly fall asleep...")
    print("")
    Continue()
    rd()
    Or()
    srr()
    bfot()
    cft()
    st()
    ct()
    rat()
    wst()
    fep()
    esot()
    seor()
    sleep(2)
    cls()
    print("")
    print(" the end of the lollipop??")
    Continue()
    print("")
    print("NOTE TO KEVIN--THIS IS OUR PROGRESS SO FAR")
    Continue()
    KVersChoice()

def Kvep9():
    cls()
    print("")
    print("Episode 9: Exploration... ")
    print("")
    print("..time to get back to the real world...are we ready????")
    print("")
    print("""
    so I go up in the ship and past Mars we start to get clear communication
    """)
    sleep(5)
    Continue()
    KVersChoice()
   
def Kvep10():
    cls()
    print("")
    print("Episode 10: Contact ")
    print("")
    print("Alien contact is a scary thing.....")
    print("")
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
    sleep(5)
    Continue()
    cls()
    KVersChoice()   

def Adventure():
    cls()
    print("")
    #print("Program 8: KendyVerse ")
    print("The Adventure begins.....")
    print("")
    #print("Are you ready to enter the amazing adventure and gaming world")
    #print("- KendyVerse?")
    #print("")
    #go=input("Press any key to continue")
    Continue()
    KVersChoice()


def ChatBot():
    cls()
    print("")
    print("Program 2: ChatBot ")
    #print("I am a chat bot!")
    print("")
    subprocess.call(" python chatbot.py 1", shell=True)
    go=input("Press any key to continue")
    #sleep(5)
    GoAgain()
    
def Tank():
    cls()
    print("")
    print("Program 3: Tank ")
    print("I am a tank!")
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
    go=input("Press any key to continue")
    #Chooser();
    #sleep(3)
    GoAgain()
    
def Wendy():
    cls()
    print("")
    print("Program 7: Wendy")
    print("I am Wendy!")
    print("")
    go=input("Press any key to continue")
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
    #Chooser();
    #sleep(3)
    GoAgain()

def KendyRobot():
    cls()
    #print("Program 9: Kendy Robot")
    print("")
    print("Welcome!")
    print("")
    print("Activating Startup Sequence.")
    print("----------------------------")
    print("")
    cls()
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

#def accessCode():
    #code=int(input("Please enter your access code: "))
    #while code != "1284":
       #print("")
       #print('Enter Access Code.') # There are four spaces in front of print.
       #code = input()


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


def KVersMenu():
    cls()
    print("")
    print("StartMenu:")
    print("---------")
    print("")
    print("Episode 1: Lost  ")
    #print("")
    print("Episode 2: Discovery ")
    #print("")
    print("Episode 3: Assistance ")
    #print("")
    print("Episode 4: Repairs ")
    #print("")
    print("Episode 5: Recovery ")
    #print("")
    print("Episode 6: Stabilization ")
    #print("")
    print("Episode 7: Resources ")
    #print("")
    print("Episode 8: Training  " )
    #print("")
    print("Episone 9: Exploration ")
    #print("")
    print("Episode 10: Contact ")
    #print("")
    print("Episode 11: ToDo List ")
    #print("End Program")
    print("To End please enter 12")
    #print("Please choose a program")

def KVersChoice():
    cls()
    print("")
    #print("Chooser:")
    print("--------")
    KVersMenu()
    print("")
    #choice = 0;
    #terminator = "n";
    choice = int(input("Please choose a program number from 1 - 10 and then press Enter: "))

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
    elif choice == 11:
        #print("You chose program ,",+choice)
        Kvep11();    
    elif choice== 12:
        sys.exit()
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
   
#def playAgain():
    
    #print("Replace 'playAgain()' with 'Chooser()' from 'kstart03.py'")
    
    #playAgain = ''
    #while playAgain == 'yes' or playAgain == 'y':
    #print('Do you want to restart the IPS? (yes or no)')
    #go = input('Do you want to restart the IPS? (yes or no)')
    #if go == "y":
    #print("Thanks")
    #else:
        #print("Bye!")
        #sleep(3)
        #break
        #return()


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
    
  
def GoAgain():
    cls()
    print("")
    print("Return to Main Menu!")
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
    ToDoList();
    StartMenu();
    Chooser();
    End();
    ---
    """)
    print("")
    #go = input("    Press Enter to continue...")
    #Test()

    Intro()
    ToDoList()
    StartMenu()
    #MainEx()
    GoAgain()
    Chooser()
    #End()
    cls()
    sleep(2)
    #print("")
    Chooser()
    
def ToDoList():
    cls()
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
    go = input("    Press Enter to continue...")
    cls()
    #sleep(2)
    #print("")
    GoAgain()
        
def Main():

    #Test()
    #Chooser()
    #Intro()
    #ToDoList()
    #StartMenu()
    MainEx()
    #GoAgain()
    #End()


Main();
