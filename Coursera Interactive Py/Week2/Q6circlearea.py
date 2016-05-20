import math
print 'Calculating the area of a circle'
def circle_area(radius):
    radius=input('Enter Radius ')
    radius=float(radius)
    return math.pi*radius**2
print 'The area of the circle is', circle_area(0),'square inches'
