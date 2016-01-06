
import MySQLdb

class Database:

    host   = 'localhost'
    user   = 'root'
    passwd = ''
    db     = 'test'

    def __init__(self): #contructor
        self.connection = MySQLdb.connect( host = self.host,
                                           user = self.user,
                                           passwd = self.passwd,
                                           db = self.db)

    def query(self, q): #cursor object, uses DictCursor(returns results formatted)
        cursor= self.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(q)
        self.connection.commit()
        self.connection.close()
        return cursor.fetchall()

    def __del__(self): #close connection
        self.connection.close()


if __name__ == '__main__': #main body
    db = Database()

    q = "DELETE FROM testtable" #q runs the db delete action

    db.query(q) #runs the db insert action

    q = """
    INSERT INTO testtable
    (name, age)
    VALUES
    ('Mike', 39),
    ('Micheal', 21),
    ('Angela', 21)
    """
    
    db.query(q) #another query

    q = """
    SELECT * FROM testtable
    WHERE age = 21
    """

    people = db.query(q)

    for person in people:
        print "Found: %s " % person ["name"]
