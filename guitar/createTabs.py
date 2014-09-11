#/usr/bin/python

strmap = {'E':1, 'a':2, 'd':3, 'g':4, 'b':5, 'e':6}
nob = 4
beat = '-'
tabs = {}

def initTab():
	for key in strmap.keys():
			tabs[key] = beat * nob

def createTab(tab=None):
	if not tab:
			pass
	
	for key in strmap.keys():
			if key in tab:
					tabs[key] += tab.rstrip().strip(key).rjust(nob)
			else:
					tabs[key] += beat * nob

def printTabs():
	for strval in sorted(strmap.items(), key=lambda x:x[1]):
			print tabs[strval[0]]

initTab()

with open('tabfile') as fp:
	for line in fp:
			createTab(line)


printTabs()
