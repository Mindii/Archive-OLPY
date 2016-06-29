import os							# OS Module
from tkinter import Tk				# Clipboard module

# Let's get clipboard
r = Tk()
clip = r.clipboard_get()
growl_command = 'C:\Scripts\growlnotify.exe /r:"Script" /i:"c:/Scripts/vid.jpg" /t:"Stream" /n:"Script" /a:"Script"'

# if's for diffent sites
if "youtube" in clip:
   growl_say = R'%s "Playing link 720p from youtube."' % (growl_command)
   ls_command = R"livestreamer %s 720p" % (clip)
   os.system(growl_say)
   os.system(ls_command)
   exit()
   
if "hitbox" in clip:
   growl_say = R'%s "Playing link 720p from hitbox."' % (growl_command)
   os.system(growl_say)
   ls_command = R"livestreamer %s 720p" % (clip)
   os.system(ls_command)
   exit()

if "twitch" in clip:
   growl_say = R'%s "Playing link high from twitch."' % (growl_command)
   os.system(growl_say)
   ls_command = R"livestreamer %s high" % (clip)
   os.system(ls_command)
   exit()
   
else:
   growl_say = R'%s "Livestream/Video link no detected."' % (growl_command)
   os.system(growl_say)
   exit()