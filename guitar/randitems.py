# Randomly print items in the list
# Wait lag seconds

from random import randint
import time

items = [ 'C', 'G', 'D', 'Em' ]
lag = 10

while True:
	print items[randint(0,len(items)-1)]
	time.sleep(lag)
