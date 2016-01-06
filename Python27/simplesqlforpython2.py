
import MySQLdb
import sys

mydb1 = MySQLdb.connect(host='localhost',   #connections
                       user='root',
                       passwd='',
                       db='menu')

mydb2 = MySQLdb.connect(host='localhost',
                       user='root',
                       passwd='',
                       db='python')


cursor1 = mydb1.cursor()    #cursor objects
cursor1.execute('SELECT * FROM fish')
result = cursor1.fetchall()
mydb1.commit()
mydb1.close
print ('\n query 1 \n')
for record in result:
    
    print (record[0], '. ', record[1], '(%s)' %record[2])
    
'''
cursor2 = mydb2.cursor()
cursor2.execute('SELECT * FROM text')
result2 = cursor2.fetchall()
mydb2.commit()
mydb2.close
print '\n query 2 \n'
for record in result2:    
    print record[0], '. ', record[1], '(%s)' %record[2]

#sql sample queries
cursor1 = mydb1.cursor() 
cursor1.execute('SELECT * FROM fish WHERE ID = 2')
result3 = cursor1.fetchall()
mydb1.commit()
mydb1.close
print '\n query 3 \n'
for record in result3:    
    print record[0], '. ', record[1], '(%s)' %record[2]

cursor1 = mydb1.cursor()    
cursor1.execute('SELECT * FROM fish GROUP by name')
result4 = cursor1.fetchall()
mydb1.commit()
mydb1.close
print '\n query 4 \n'
for record in result4:    
    print record[0], '. ', record[1], '(%s)' %record[2]

'''#result formatting error to fix later
cursor1 = mydb1.cursor()    
cursor1.execute('SELECT name, count(*) FROM fish GROUP by name')
result5 = cursor1.fetchall()
mydb1.commit()
mydb1.close
print ('\n query 5 \n')
for record in result5:    
    print (record[0], '. ', record[1], '(%s)' %record[2])
'''
cursor2 = mydb2.cursor()
cursor2.execute('SELECT title, count(*) FROM text')
result6 = cursor2.fetchall()
mydb2.commit()
mydb2.close
print '\n query 6 \n'
for record6 in result:
    
    print record[0], '. ', record[1], '(%s)' %record[2] #this db has issues

cursor1 = mydb1.cursor()    
cursor1.execute('SELECT * FROM fish GROUP by name HAVING id>7') #HAVING not standard used
result7 = cursor1.fetchall()
mydb1.commit()
mydb1.close
print '\n query 7 \n'
for record7 in result:    
    print record[0], '. ', record[1], '(%s)' %record[2]

cursor1 = mydb1.cursor()    
cursor1.execute('SELECT * FROM fish GROUP BY name ORDER BY id DESC')
result8 = cursor1.fetchall()
mydb1.commit()
mydb1.close
print '\n query 8 \n'
for record in result8:    
    print record[0], '. ', record[1], '(%s)' %record[2]

cursor1 = mydb1.cursor()    
cursor1.execute('SELECT * FROM fish ORDER BY id DESC')
result9 = cursor1.fetchall()
mydb1.commit()
mydb1.close
print '\n query 9 \n'
for record in result9:    
    print record[0], '. ', record[1], '(%s)' %record[2]

'''
'''
mysql> SELECT * FROM menu GROUP BY name LIMIT 3,4;
mysql> SELECT * FROM menu ORDER BY id LIMIT 3,4;
mysql> SELECT * FROM menu ORDER BY id LIMIT 2,3;
mysql> SELECT * FROM menu LIMIT 2,4;
LIMITand HAVINGmay seem very similar as they both work to narrow 
the aggregate. The difference between them lies in the timing of their 
application by MySQL. HAVINGis applied as a parameter of the search 
beforeMySQL actions the query. The LIMITclause, on the other hand, is 
applied afterthe search results have been returned.

'''
