import math
print '''Heron's formula states the area of a triangle is v(s(s-a)(s-b)(s-c))
where a, b and c are the lengths of the sides of the triangle and s=12(a+b+c)
is the semi-perimeter of the triangle'''

def find_area(a,b,c):
    a= input('Enter length of side A ')
    a=float(a)
    b= input('Enter length of side B ')
    b=float(b)
    c= input('Enter length of side C ')
    c=float(c)
    s=(a+b+c)/2
    #print s
    y=abs(s-a)
    #print y
    x=abs(s-b)
    #print x
    z=abs(x-c)
    #print z
    w=(y*x*z)
    #print w
    r=s*w
    #print r
    area =r**(0.5)
    #print area
    return area
    print 'area is', area
find_area(0,0,0)

    
