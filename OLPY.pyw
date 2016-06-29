import os							# OS Module
from tkinter import Tk				# Clipboard module

# Getting clip
r = Tk()
app = "\"D:\Program Files (x86)\conkeror\conkeror.exe\""
clip = r.clipboard_get()
clip = clip.lstrip()
clip = clip.rstrip()

# Running command
ls_command = R"%s -f g %s" % (app, clip)
os.system(ls_command)