from Tkinter import*
import Tkinter as ttk



def hello():
      print 'Hello'

def goodbye():
      print 'goodbye'

#Frame attributes
frame = Tk()
frame.title('Greetings')
frame.geometry('200x100')

#Buttons
hellobutton = ttk.Button(frame, width = 12, text = 'Hello', command = hello).grid(column=0, row = 0)
goodbybutton = ttk.Button(frame, width = 12, text = 'Goodbye', command = goodbye).grid(column=1, row = 0)

frame.mainloop()
