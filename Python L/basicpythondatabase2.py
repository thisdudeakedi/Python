#import MySQLdb
import pymysql

class Database:
    host = 'localhost'
    user = 'root'
    passwd = ''
    db = 'test'
    
    mydb=pymysql.connect(host='localhost',
    def __init__(self):
        self.connection = MySQLdb.connect ( 
        host = self.host,
        user = self.user,
        passwd = self.passwd,
        db = self.db )
        
    def query (self, q):
        cursor = .cursor (MySQLdb.cursors.DictCursor)
        cursor.execute(q)
        
        return cursor.fetchall()
    
    def __del__(self):
        self.connection.close()
        
if __name__ ==  '__main__':
    db = Database()
    q = 'Delete FROM testtable'
    
    db.query(q)
    
    q = '''
    Insert into testTable ('id','name', 'age')
    VALUES
    ('1', 'Mike', '39'), ('2', Micheal','21'), ('3',Angela','21')
    '''
    
    q = '''
    SELECT * FROM testtable WHERE age = 21'''
    
    people = db.query(q) 
     
    for person in people:
        print ('Found: %s') %person ('name')
        print (people)
