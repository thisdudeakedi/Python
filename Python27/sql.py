
#MySQL for Python

import pymysql
import sys

#connection, with error handling
try: 
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='python'
        )
except Exception as e:
    sys.exit('We cannot get into the database')

#cursor does operations on MySQL (started with WAMP with db=python, table=text)
cursor = db.cursor()
#cursor.execute('INSERT INTO text (title, text) VALUES ("Jill", "Jack was here")')
#db.commit() 
cursor.execute('SELECT * FROM text')
result = cursor.fetchall()

print(result)

#written to solve readablity 
if result:
    for z in result:
        print (z[1]+ ': ' +z[2] )

#written by me to summarize entries but incomplete (needs to auto count)
print ('\nSummary:')
if result:
    for z in result:
        print (len(z[1])

#l = len(result)
#print ('Entries ='), l

#l1 = len(z[1])
#print ('Length of entry 1:'), l1

#l2 = len(z[2])
#print ('Length of entry 2:'), l2
