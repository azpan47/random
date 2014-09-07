from sys import argv
from QuickFindUf import QuickFindUf

def main(argv):
	
	noe = int(raw_input())
	qf = QuickFindUf(noe)

	while True:
			feed1 = raw_input()
			feed2 = raw_input()
			if not (feed1 and feed2):
					print "no of components: %d" %qf.count()
					print qf.cid
					break
			p = int(feed1)
			q = int(feed2)
			if not qf.connected(p,q):
					qf.union(p,q)
					print "%d %d" %(p,q)


if __name__ == '__main__':
		main(argv)
