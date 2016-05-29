import math
print 'The area of a rectangle'
def rectangle_area(width,height):
    width=input('Enter Width ')
    width=float(width)
    height=input('Enter Height ')
    height=float(height)
    area=width*height
    return area
a1=rectangle_area(0,0)
print 'The Area of the rectangle is', a1, 'inches'
