import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext #for the scrolled test
win = tk.Tk()

#Label
alabel=ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

#Button Function
def clickMe():
    action.configure(text='Hello '+ name.get()+' '+numberChosen.get()) #internal lookup
    action.grid(column=2, row=1)
    print (name.get()+' '+numberChosen.get())

#Button
action=ttk.Button(win,text='Click Me!', command=clickMe) #event call
action.grid(column=2, row=1)

#Adding a textbox
name = tk.StringVar() #defining name
nameEntered = ttk.Entry(win, width=12, textvariable=name) #entry wiget/
nameEntered.grid(column=0,row=1)
nameEntered.focus()

#Combo Box
ttk.Label(win, text='Choose a number:').grid(column=1,row=0)
number=tk.StringVar()
numberChosen=ttk.Combobox(win,width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1,2,4,31,42,100)
numberChosen.grid(column=1,row=1)
numberChosen.current=(0)

#Check Buttons
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win, text='Disabled',variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0,row=2, sticky=tk.W) #alignment=west or alignment=left

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win, text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=2, sticky=tk.W)

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win, text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column=2,row=2, sticky=tk.W)
'''
#Radio Buttons
#Radio Button Globals
COLOR1='Blue'
COLOR2='Gold'
COLOR3='Red'

#Radio Callback
def radCall():
    radSel=radVar.get()
    if   radSel==1: win.configure(background=COLOR1)
    elif radSel==2: win.configure(background=COLOR2)
    elif radSel==3: win.configure(background=COLOR3)

#Radio Buttons
radVar=tk.IntVar
radVar=set(99) #done for several widgets remember to complete
rad1=tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=4, sticky=tk.W)

rad2=tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=4, sticky=tk.W)

rad3=tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=4, sticky=tk.W)
'''
#Scrolled Text
scrolW = 30
scrolH = 5 
scr=scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0,columnspan=3)

#Create Container to hold Labels
labelsFrame = ttk.LabelFrame(win, text='Labels in a frame')
labelsFrame.grid(column=0, row=7, padx=7, pady=40)

#Place labels into a Container element
ttk.Label(labelsFrame, text='Label 1').grid(column=0,row=6)
ttk.Label(labelsFrame, text='Label 2').grid(column=1,row=6)
ttk.Label(labelsFrame, text='Label 3').grid(column=2,row=6)
nameEntered.focus()

#Create Container to hold Labels Rows Version 2
labelsFramev2 = ttk.LabelFrame(win, text='Labels in a frame Version 2') #the longer the text makes the frame appear soo much more longer..
labelsFramev2.grid(column=0, row=8, padx=7, pady=40)

#Place labels into a Container element
ttk.Label(labelsFramev2, text='Label 1').grid(column=0,row=8)
ttk.Label(labelsFramev2, text='Label 2').grid(column=0,row=9)
ttk.Label(labelsFramev2, text='Label 3').grid(column=0,row=10)
nameEntered.focus()


for child in labelsFrame.winfo_children(): #grid_configure lets you modify elements before the mainloop, winfo_children returns a list of all the children belonging to the LabelsFrame this allows us to loop through them and assign the padding to each label
    child.grid_configure(padx=8, pady=4)


win.mainloop() #starting the GUI