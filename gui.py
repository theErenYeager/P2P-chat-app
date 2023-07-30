import tkinter as tk
from threading import *
# Gui


def Gui():
    tab = tk.Tk()
    tab.geometry('500x500')
    tk.Label(tab, text='P2P Chat').pack()
    tab.mainloop()
