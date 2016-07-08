from Tkinter import*
import Tkinter as ttk

count =0

def reset():
      global count
      count = 0
      
def increment():
      global count
      count += 1

def decrement():
      global count
      count -= 1

def print_count():
      #global count
      print count

#Frame attributes
frame = Tk()
frame.title=('Count')
frame.geometry('200x100')

#Buttons
buttonadd = ttk.Button(frame, width = 12, text = 'Add One', command = increment).grid(column=0, row=0)
buttonsub = ttk.Button(frame, width = 12, text = 'Take One', command = decrement).grid(column=1, row=0)
buttonreset = ttk.Button(frame, width = 12, text = 'Reset', command = reset).grid(column=0, row=1)
buttonprint = ttk.Button(frame, width = 12, text = 'Print', command = print_count).grid(column=1, row=1)

frame.mainloop()
