import sys,os

if len(sys.argv) > 2 :
		print "Usage: %s length" % (sys.argv[0])

l = 27 if len(sys.argv) == 1 else sys.argv[1]

c = l/2.00

for i in range(8,13):
		bal = l - c - float(i)/8
		print i, bal
