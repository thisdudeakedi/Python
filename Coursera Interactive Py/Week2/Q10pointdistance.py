
print 'Euclidian distance between two points'
def point_distance(x0,y0,x1,y1):
    x0=input('Enter x0 ')
    x0=int(x0)
    y0=input('Enter y0 ')
    y0=int(y0)
    x1=input('Enter x1 ')
    x1=int(x1)
    y1=input('Enter y1 ')
    y1=int(y1)
    return ((x0-x1)**2+(y0-y1)**2)**0.5
print point_distance(0,0,0,0), 'inches'
