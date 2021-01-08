# This script will manage the music playback.
# I will try implementing PlaySound first.
# Using '7 PM.mp3' from Animal Crossing: New Leaf. Use your own backup or magical fingers to find it online.
import pyglet
#NOT_IN_USE from playsound import playsound
# Mazter's code to read the hour from current_hour, and play music file from index of one list
#current_song = f"{current_hour} AM.m4a"





# playsound does not support space in names. This has to be fixed.
# s_musicfile = "/Users/xxxxxxxxxx/Desktop/play this file.mp3"
# s_musicfile = s_musicfile.replace(" ", "%20")
# playsound(s_musicfile)


# Script grabbing current_hour, and then playing the proper OST music. Courtesy of Mazter.
# datetime grab

from datetime import datetime
now = datetime.now()
current_hour = now.strftime("%H")
hour_int = int(current_hour)





import pyglet
player = pyglet.media.Player()
player.queue(pyglet.media.load("music/wishloop.mp3"))
player.play()








#playsound("music/wishloop.mp3","music/wishloop.mp3")
# wtf is this, Mazter? hour_int is number from 0 to 23

am_or_pm = 'AM' if hour_int < 12 else 'PM'
short_hour = hour_int if hour_int < 13 else hour_int - 12
if short_hour == 0:
  current_hour = 12
song_name = f"music/{short_hour} {am_or_pm}.mp3"
song_namePrint = f"{short_hour} {am_or_pm}"
song_name = song_name.replace(" ", "%20")
print("Now playing",song_namePrint)
#playsound(song_name)







#currentHourOST =f"{short_hour} {am_or_pm}.mp3"
#currentHourOST = currentHourOST.replace(" ", "%20")
#print(currentHourOST)


# TEST VALUE FOR VAR currentHourOST = "7 PM.mp3"
#currentHourOST = currentHourOST.replace(" ", "%20")
#playsound(currentHourOST)
