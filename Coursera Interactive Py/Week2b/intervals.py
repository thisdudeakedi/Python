#Compute whether two intervals intersect

def interval_intersect(a, b, c, d):
    return (c <= b) and (a <= d)
#Returns whether the intervals [a,b] and [c,d] intersect

def test (a, b, c, d):
    print 'Intervals ['+ str(a)+','+str(b)+'] and [' +str(c)+','+str(d)+']'
    if interval_intersect (a, b, c, d):
        print 'intersect'
    else:
        print 'do not intersect'

a = input('Input a ')
b = input('Input b ')
c = input('Input c ')
d = input('Input d ')

test(a, b, c, d)
