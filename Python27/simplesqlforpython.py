
import MySQLdb
import sys
mydb = MySQLdb.connect(host='localhost',
                       user='root',
                       passwd='',
                       db='menu')
cursor = mydb.cursor()
cursor.execute('SELECT * FROM fish')
result = cursor.fetchall()
mydb.commit()
mydb.close
print (result)
