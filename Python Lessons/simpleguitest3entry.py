import tkinter as tk
from tkinter import ttk
win = tk.Tk()

def clickMe():
	action.configure(text='Hello '+ name.get()) #internal lookup
	action.grid(column=1, row=1)

#Button
action=ttk.Button(win,text='Click Me!', command=clickMe) #event call
action.grid(column=1, row=1)

actionButton=ttk.Button(win,text='Click Me!', command=clickMe, state='disabled') #event call
actionButton.grid(column=2, row=1)

#Label
alabel=ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

#Adding a textbox
name = tk.StringVar() #defining name
nameEntered = ttk.Entry(win, width=12, textvariable=name) #entry wiget/
nameEntered.grid(column=0,row=1)


win.mainloop() #starting the GUI