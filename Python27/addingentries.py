#inserting records

import pymysql
import pymysql.cursors
import sys

try:
    db = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='test'
        )
except Exception as e:
    sys.exit('We cannot get into the database')

cursor=db.cursor()
#cursor.execute('INSERT INTO text (title, text) VALUES ("Tom", "Peggy was here")')
cursor.execute("INSERT INTO testtable (name,age) VALUES ('Jack','45')")
cursor.execute('SELECT * FROM testtable')
result = cursor.fetchall()
db.commit()
db.close()
print (result)
