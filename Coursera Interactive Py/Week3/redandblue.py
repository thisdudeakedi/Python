from Tkinter import*
import Tkinter as ttk

def set_blue():
      bluebutton = frame.configure (bg = 'blue')

def set_red():
      redbutton = Button(text= 'change', bg = 'red')

#frame attributes
frame = Tk()
frame.title=('Red and Blue')
frame.geometry('200x100')

#Buttons
bluebutton  = ttk.Button(frame, width = 12, text = 'blue', command = set_blue).grid(column = 0, row = 0)
redbutton  = ttk.Button(frame, width = 12, text = 'red', command = set_red).grid(column = 1, row = 0)

frame.mainloop()
