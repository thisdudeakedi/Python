print '''computing the area of a triangle using Heron's forumular
and the triangle's vertices'''
print 'Enter the vertices of the triangle'
x0=input('Enter the point x0 ')
x0=int(x0)
y0=input('Enter the point y0 ')
y0=int(y0)
x1=input('Enter the point x1 ')
x1=int(x1)
y1=input('Enter the point y1 ')
y1=int(y1)
x2=input('Enter the point x2 ')
x2=int(x2)
y2=input('Enter the point y2 ')
y2=int(y2)

print 'Triangle of vertices', x0,y0, 'and', x1,y1, 'and', x2,y2

def point_distance(x0,y0,x1,y1):
    return ((x0-x1)**2+(y0-y1)**2)**0.5

a=point_distance(x0,y0,x1,y1)
b=point_distance(x0,y0,x2,y2)
c=point_distance(x1,y1,x2,y2)

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print 'has an Area of ', area
