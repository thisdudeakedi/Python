print 'Compound Interest Calculator = present_value * (1 + 0.01 * annual_rate) ** years'
print 'Enter present value'
pv=raw_input()
pv=float(pv)
print 'Enter annual rate'
ar=raw_input()
ar=float(ar)
print 'Enter years'
y=raw_input()
y=float(y)
ci = pv*(1+0.01*ar)**y

print 'The future value of ', pv,'KSH in ', y, 'years at annual rate of', ar, 'percent is', ci
