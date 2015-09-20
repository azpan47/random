import os,sys

def bs(n):

	for i in reversed(range(n/3+1)):

		d3 = i
		k = n - i*3
		d5 = k / 5
		r5 = k % 5

		if not r5:
			return d3*3*"5" + d5*5*"3"
	
	return -1

if len(sys.argv) != 2 :
	print "Usage: %s filename" %(sys.argv[0])
	sys.exit(1)

f = open(sys.argv[1])

m = int(f.readline().strip())

for i in range(m):		
	n = int(f.readline().strip())
	print bs(n)
