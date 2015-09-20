import sys, os

n = int(input("Enter the number < 200 :"))
r = [1]

def prod(r, i):
	c = 0
	for j in range(len(r)):
			t = r[j]*i + c
			r[j] = t%10
			c = t/10

	if(c):
			r.append(c)

for i in range(2,n+1):
		prod(r, i)

print r
