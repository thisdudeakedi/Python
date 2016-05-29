
import tkinter as tk
win = tk.Tk()   #TK class instance to run in the mainloop
win.title("Python GUI") #title is a property in the tkinter import
win.resizable(0,0) #Prevents GUI from being resized, method in class instance win
win.mainloop()  #method in the class instance win, starts GUI 
                


class Aclass(object):   #class example runs after tk.TK() class
    print ('Hello from Aclass')

classinstance = Aclass()

