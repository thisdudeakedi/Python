
def seconds_conversion(hours,minutes,seconds):
    hours=input('Enter the hours ')
    hours=float(hours)
    hours=hours*60*60
    minutes=input('Enter the minutes ')
    minutes=float(minutes)
    minutes=minutes*60
    seconds=input('Enter the seconds ')
    seconds=float(seconds)
    totalseconds=hours+minutes+seconds
    return totalseconds

a1 = seconds_conversion(0,0,0)
print 'conversion is', a1, 'seconds'
#print 'Seconds conversion is',(seconds_conversion(0,0,0),'seconds')
