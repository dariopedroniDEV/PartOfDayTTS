# PROGRAM: What time is it?
# Importing Classes
# Importing the time from Python included tools
# import gtts to enable Text To speech NOT WORKING! LOOKING TO USE pyttsx3
from datetime import datetime
import pyttsx3
# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Language selection part (Italian, English and Norwegian)
lan = input("Language/Lingua/Språk: ")
# Grab input, create variable and convert to int value.


# A simple program that checks the computer clock time, and tells you if it's morning, afternoon, evening or night.
welcome = str ("Hello! This program will check your computer clock and tell you what ime is it.")
print(welcome)

# Grabbing current hour, minutes and seconds
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

# Grabbing hour only from strftime, to check which moment of the day it is
current_hour = now.strftime("%H")
# Converting the string "hour_int" to a integer to make it work with the comparison part
hour_int = int(current_hour)
print("The value of hour_int is: ",hour_int)


# Comparison Part.
if hour_int >= 5 and hour_int <= 12:
    moment = "morning"
if hour_int >= 11 and hour_int <= 12:
    moment = "afternoon"
if hour_int >= 17 and hour_int <= 24:
    moment = "evening"
if hour_int >= 23 and hour_int <= 6:
    moment = "night"


# Final program part - Showing
theTime = 'The current time is ' + current_time  + '. and it is ' + moment
itaTime = 'Sono le ' + current_time + ' Ed è' + moment
print(theTime)
# Letting the sound engine say the previous ¢string.
engine.say(theTime)
engine.say(itaTime)
engine.runAndWait()
