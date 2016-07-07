from Tkinter import*
import Tkinter as ttk

#print, swap, add, sub, div, mult

store = 12
operand = 3

def output():
      print 'Store = ', store
      print 'Operand = ', operand
      print ''

def swap():
      global store, operand
      store, operand = operand, store
      output()

def add():
      global store
      store = store +operand
      output()

def sub():
      global store
      store = store - operand
      output()

def mult():
      global store
      store = store * operand
      output()

def div():
      global store
      store= store / operand
      output()

#Enter a new operand
def inp():
      entry= 0
      global operand
      entry = inputentry.get()
      operand = int(entry)
      output()

#Frame attributes
frame=Tk()
frame.title('Calculator')
frame.geometry('300x200')
inputentry = StringVar()

#Button attributes using ttk events
outputbutton = ttk.Button(frame, width = 12, text= 'Print', command=output).grid(column = 0, row= 1)
swapbutton = ttk.Button(frame, width = 12, text= 'Swap', command=swap).grid(column = 0, row= 2)
addbutton = ttk.Button(frame, width = 12, text= 'Add', command=add).grid(column = 0, row= 3)
subbutton = ttk.Button(frame, width = 12, text= 'Subtract', command=sub).grid(column = 0, row= 4)
multbutton = ttk.Button(frame, width = 12, text= 'Multiply', command=mult).grid(column = 0, row= 5)
divbutton = ttk.Button(frame, width = 12, text= 'Division', command=div).grid(column = 0, row= 6)
inputbutton = ttk.Button(frame, width = 12, text= 'Enter', command=inp).grid(column = 0, row= 7)

#intput using ttk input event
Entered = ttk.Entry(frame, width=15, textvariable=inputentry).grid(column=1, row=7)

frame.mainloop()
