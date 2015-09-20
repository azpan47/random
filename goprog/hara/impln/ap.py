import os,sys

if len(sys.argv) != 2 :
		print "Usage: %s filename" %(sys.argv[0])
		sys.exit(1)

f = open(sys.argv[1])

m = int(f.readline().strip())

for i in range(m):		
		n, k = map(int, f.readline().split())
		a = filter(lambda x: x<=0, map(int, f.readline().split()))
		print k > len(a)
