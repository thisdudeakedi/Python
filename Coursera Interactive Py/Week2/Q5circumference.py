import math

print 'Calculating the circumference of a circle'
def circumference(radius):
    radius=input('Enter Radius ')
    radius=float(radius)
    circ=2*math.pi*radius
    return circ

print 'The circumference is', circumference(0), 'inches'
