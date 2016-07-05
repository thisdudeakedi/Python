import Tkinter as tk
#from Tkinter
import ttk
win = tk.Tk()
aLabel = ttk.Label(win, text='A Label')		#Adding a Label
aLabel.grid(column=0,row=0)

#Button Click Event Callback Function
def clickMe():
	action.configure(text="** I have been Clicked! **") 
	aLabel.configure(foreground="red")

#Adding a Button
action = ttk.Button(win, text='Click Me!', command=clickMe) 	#the event call
action.grid(column=1, row=0)

win.mainloop()
