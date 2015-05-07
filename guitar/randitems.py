# Randomly print items in the list
# Wait lag seconds

from random import randint
import time
import sys

items = [ 'C', 'G', 'D', 'Em' ]
lag = 3

while True:
	sys.stdout.write("%s \r" % items[randint(0,len(items)-1)])
	sys.stdout.flush()
	time.sleep(lag)
