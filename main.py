# PROGRAM: What time is it?
# Importing Classes
# Importing the time from Python included tools
# import gtts to enable Text To speech NOT WORKING! LOOKING TO USE pyttsx3
from datetime import datetime
import langMenu
import pyttsx3

# datetime grab
now = datetime.now()
current_time = now.strftime("%H:%M:%S")



# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
engine.setProperty('rate', 150)

#################################################################### PART 01: LANGUAGE MENU
# Execute Language select function from langMenu.py
# Important to get value of lanVal
langMenu.lanInput()



# Welcome message
welcomePrint = None
def welcomeMessage():
    global welcomePrint
    if langMenu.lanVal == 'EN':
        welcomePrint = "Welcome! This program will tell you the current time, both by text and TTS."
    if langMenu.lanVal == 'IT':
        welcomePrint = "Benvenuto! Questo programma ti dirà l'ora attuale tramite testo e TTS"
    if langMenu.lanVal == 'NO':
        welcomePrint = "Velkomment! Random text here."

welcomeMessage()
print(welcomePrint)



# Grabbing current hour, minutes and seconds
def currentTime():

    global strCurrentTime

    if langMenu.lanVal == 'EN':
        strCurrentTime = "Current Time =", current_time
    if langMenu.lanVal == 'IT':
        strCurrentTime = "Tempo attuale =", current_time
    if langMenu.lanVal == 'NO':
        strCurrentTime = "Nåværende tid =", current_time
    print(strCurrentTime)

currentTime()








# Grabbing hour only from strftime, to check which moment of the day it is
current_hour = now.strftime("%H")
# Converting the string "hour_int" to a integer to make it work with the comparison part
hour_int = int(current_hour)
print("The value of hour_int is: ",hour_int)


# Comparison Part.

def momentEN():
    moment = None

    if hour_int >= 5 and hour_int <= 12:
        moment = "morning"
    if hour_int >= 11 and hour_int <= 12:
        moment = "afternoon"
    if hour_int >= 17 and hour_int <= 24:
        moment = "evening"
    if hour_int >= 23 and hour_int <= 6:
        moment = "night"
    theTime = 'The current time is ' + current_time + '. and it is ' + moment
    print(theTime)
    engine.say(theTime)
    engine.runAndWait()

def momentIT():
    moment = None
    if hour_int >= 5 and hour_int <= 12:
        moment = "mattina"
    if hour_int >= 11 and hour_int <= 12:
        moment = "pomeriggio"
    if hour_int >= 17 and hour_int <= 24:
        moment = "sera"
    if hour_int >= 23 and hour_int <= 6:
        moment = "notte"
    theTime = 'Ora sono le ' + current_time + ', ed è ' + moment
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(welcomePrint)
    engine.say(theTime)
    print(theTime)
    engine.runAndWait()

def momentNO():
    moment = None
    global theTime
    if hour_int >= 5 and hour_int <= 12:
        moment = "morgen"
    if hour_int >= 11 and hour_int <= 12:
        moment = "ettermiddag"
    if hour_int >= 17 and hour_int <= 24:
        moment = "kveld"
    if hour_int >= 23 and hour_int <= 6:
        moment = "natt"
    theTime = 'Den nåværende tiden er ' + current_time + ', og nå er det ' + moment
    print(theTime)
    engine.say(theTime)
    engine.runAndWait()




# Final program part - Showing (TTS Working on macOS only for now. TTS Synthetizer has to be configured for italian and Norwegian too.)

def finalPartSPeech():
    if langMenu.lanVal == 'EN':
        momentEN()
    if langMenu.lanVal == 'IT':
        momentIT()
    if langMenu.lanVal == 'NO':
        momentNO()

finalPartSPeech()

# Letting the sound engine say the previous ¢string.

