print 'point distance calculation returns the Euclidian distance between two points (x0,y0) and (x1,y1)'

def call_points (x0,y0):
    x0 = input('Enter x0 ')
    x0 = float(x0)
    y0 = input('Enter y0 ')
    y0 = float(y0)
    x1 = input('Enter x1 ')
    x1 = float(x1)
    y1 = input('Enter y1 ')
    y1 = float(y1)
    print x0,y0, 'and', x1,y1
    print 'Euclidian distance between points', ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    
call_points(0,0)
