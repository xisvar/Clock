from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
root.resizable(0,0)


def time():
    #string = strftime('%H:%M:%S %p')"%I:%M:%S %p" 
    date = strftime('    %D''\n''%H:%M:%S %p')
    label.config(text=date)
    label.after(2, time)
label = Label(root, font = ("DS-digital", 40),background = "black", foreground = "cyan")

                    #anchor = center
label.pack(expand = False ,fill=X)
time()

mainloop()
