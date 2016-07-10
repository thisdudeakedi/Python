from Tkinter import*
import Tkinter as ttk

def print_to_console():
      A = inputentry.get()
      print A

#Frame attributes
frame = Tk()
frame.title = 'Print to Console'
frame.geometry = ('400x100')
inputentry = StringVar()

#button
printbutton = ttk.Button(frame, width = 12, text= 'Print to Console', command = print_to_console).grid(column = 0, row =0)

#input using ttk input event
entry = ttk.Entry(frame, width = 15, textvariable = inputentry).grid()

frame.mainloop()
