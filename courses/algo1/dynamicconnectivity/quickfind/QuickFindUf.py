class QuickFindUf:
	"Implement Quick Find algorithm"
	
	cid = []

	def __init__(self, noe):
		self.cid = range(noe)

	def connected(self, p, q):
		return self.cid[p] == self.cid[q]

	def union(self, p, q):
		pcid = self.cid[p]
		qcid = self.cid[q]

		for i in range(len(self.cid)):
				if self.cid[i] == pcid:
						self.cid[i] = qcid

	def find(self, p):
		return self.cid[p]
	
	def count(self):
		d = dict((i,0) for i in self.cid)
		return len(d.keys())



