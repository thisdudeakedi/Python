#imports
import tkinter as tk
from tkinter import ttk #tkk extenstion has some adv widgets that make GUI look great
win = tk.Tk()
ttk.Label(win, text="A Label").grid(column=0, row=0) #passing the tkk Label constructor
win.mainloop()
