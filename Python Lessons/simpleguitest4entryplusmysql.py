import pymysql
import sys
import tkinter as tk
from tkinter import ttk 
win=tk.Tk()

mydb=pymysql.connect(host='localhost',
                    user='root',
                    passwd='',
                    db='test')

#Get Action
def buttongetdata():
	buttongetdata.configure(text='Fetched '+name.get()+'-'+age.get(),command=getdata)
	buttongetdata.grid(column=1,row=1)
	
#print(fetchedname) how do I call the data or results from a function

#Get Button
buttongetdata=ttk.Button(win, text='Get Data', command=buttongetdata)
buttongetdata.grid(column=1,row=1)

def getdata():
	cursor=mydb.cursor()
	cursor.execute('SELECT * FROM testtable')
	result=cursor.fetchall()
	mydb.close
	print (result)
	for record in result:    
		print (record[0], '. ', record[1], '(%s)' %record[2])	

#resultofsearch=getdata.result

#Post Action
def buttonpostdata():
	buttonpostdata.configure(text='Posted', command=postdata)
	buttonpostdata.grid(column=1,row=2)

#Post Button
buttonpostdata=ttk.Button(win, text='Post Data', command=buttonpostdata)
buttonpostdata.grid(column=1,row=2)

#Name TextBox
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=2,row=3)

#Age TextBox
age=tk.StringVar()
ageEntered=ttk.Entry(win,width=6,textvariable=age)
ageEntered.grid(column=2,row=4)

#using placeholders in python for sql entries
def postdata():
	cursor=mydb.cursor()
	cursor.execute("INSERT INTO testtable (name,age) VALUES (%s, %s)" % name.get(),age.get())
	cursor.execute('SELECT * FROM testtable')
	result = cursor.fetchall()
	mydb.commit()
	mydb.close()
	print (result)
'''
cursor=mydb.cursor()
cursor.execute('SELECT * FROM testtable')
result=cursor.fetchall()
mydb.close
print (result)

cursor=mydb.cursor()
cursor.execute("INSERT INTO testtable (name,age) VALUES ('Annie','27')")
cursor.execute('SELECT * FROM testtable')
result = cursor.fetchall()
mydb.commit()
mydb.close()
print (result)
'''
nameLabel=ttk.Label(win,text='Enter Name').grid(column=1,row=3)
ageLabel=ttk.Label(win,text='Enter Age').grid(column=1,row=4)

win.mainloop()