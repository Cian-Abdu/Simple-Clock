import tkinter
from time import strftime

rel = tkinter.Label()
rel.pack()
rel['bg'] = ('black')
rel['fg'] = ('white')
rel['font'] = ('Arial 120 bold')

def tic():
    rel['text'] = strftime('%H:%M:%S')

def tac():
    tic()
    rel.after(1000, tac)


tac()
