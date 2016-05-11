print ('Time converter, Hours and Minutes to Seconds')
print ('Enter Number hours')
hours=raw_input()
hours=int(hours)
sec=hours*60*60
print ('Enter Number minutes')
min=raw_input()
min=int(min)
sec1=min*60
print ('Enter Number seconds')
seconds=raw_input()
seconds=int(seconds)
seconds=seconds+sec+sec1

print ('Hello, numer of seconds = '), seconds,('seconds')
