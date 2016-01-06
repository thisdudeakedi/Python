#simple GUI
from Tkinter import *

#create new window
root = Tk()

#modify root window
root.title('Labeler')
root.geometry("300x100")

app = Frame (root)
app.grid()
label = Label (app, text = "This is a label!")
label.grid()

#kick off the event loop
root.mainloop()
