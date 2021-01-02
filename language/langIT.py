# Test code to see the settings of pyttsx3

# Importing and initializing engine
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')


# Part 02 of program
hourITA =  str('test in italiano')


for voice in voices:
   engine.setProperty('voice', voices[1].id)
   engine.say(hourITA)
   engine.runAndWait()
   break



# All the code
def languageIT():
   welcome = "Ciao! Questo programma controllerà il tempo del computer."
   strCurrentTime = "Tempo attuale =", current_time