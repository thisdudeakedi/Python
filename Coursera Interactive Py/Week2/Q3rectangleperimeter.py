
    print 'rectangle perimeter calculator'

    def rectangle_perimeter(width, height):
        width=input('Enter Width ')
        width=float(width)
        height=input('Enter Height ')
        height=float(height)
        perimeter=(2*width)+(2*height)
        return perimeter

    a1 = (rectangle_perimeter(0,0))
    print 'Perimeter is', a1, 'inches'
