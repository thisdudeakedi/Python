##incomplete mix of ttk and tkinter
from Tkinter import *
import Tkinter as ttk

#Frame attributes
frame = Tk()
frame.title('Simple GUI')
frame.geometry('300x200')

#Button
ttk.Button = ttk.Button(frame, text='Hello World').grid()

frame.mainloop()
