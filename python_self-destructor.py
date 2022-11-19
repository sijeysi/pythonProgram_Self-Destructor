# codes from Hallden "https://www.youtube.com/watch?v=_5pH_tr7uN0"
# I'm interested in this program —which allows the device owner to delete his/her files when someone robbed 
# him/her, or similar case, since I always lost my phone and I'm afraid when my info will leak.

# Idea: As I've said above, we can use this program to delete all files on a lost device to avoid invasion of privacy.
# We can improve this to only pop-up when the owner activate it using other trusted device. This can be a good
# type of security.



from tkinter import *
import os

master = Tk()
e = Entry(master)
e.pack()
e.focus_set()

def callback():
    if e.get() == "password":
        quit()

b = Button(master, text = "STOP", width=10, command=callback)
b.pack()

master.after(30000, master.destroy)
mainloop()

os.system(*rm -rf /home)