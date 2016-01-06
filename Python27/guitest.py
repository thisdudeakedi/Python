import tkinter as tk
from tkinter import *
from ttk import *
win = tk.Tk()
aLabel = ttk.Label(win, text='A Label')		#Adding a Label
aLabel.grid(column=0,row=0)
win.mainloop()
