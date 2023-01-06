# Importing TKinter module and steamdata.py
from tkinter import *
from tkinter.ttk import *
import steamdata as sdata


# Setting up the GUI window
root = Tk()
root.title("SteamSpy Scraper")
root.geometry('600x600')
root.resizable(0,0)

# Get SteamSpy data
def steamdata():
    text = entry.get("1.0",END)
    text = text.rstrip().split('\n') # https://www.geeksforgeeks.org/python-ways-to-split-strings-using-newline-delimiter/
    sdata.get_steam_data(text, progress, percent)

# Creating the widgets
l1 = Label(root, text="Enter game names below, with a new line separating each name:", width = 80)
entry = Text(root, width=70, height=27, padx = 10, wrap=WORD)
button = Button(root, text="Execute", width=80)

# Percent and progress bar: https://www.youtube.com/watch?v=o_Ct13fHeck
percent = Label(root, text="", anchor=S)
progress = Progressbar(root, length=500, mode='determinate')
percent['text'] = "{}%".format(int(0))

# Positioning the widgets
l1.grid(row=1, column=1, padx = 10, pady = (10,0), sticky = 'W')
entry.grid(row=2, column=1,padx = 10, pady = (10,10))#, padx=5)#, #pady=(0,10))
button.place(relx=0.5, rely=0.85, anchor=CENTER)
percent.place(relx=0.5, rely = 0.90, anchor = CENTER)
progress.place(relx=0.5, rely = 0.94, anchor = CENTER)

# Button activation
button.configure(command=steamdata)

# Adding mainloop so the program is on repeat
root.mainloop()
