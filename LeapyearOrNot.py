n=int(input())
if n%4!=0:
print "normal year"
elif n%100==0:
if n%400==0:
print "leap year"
else:
print "normal year"
else:
print "leap year"
