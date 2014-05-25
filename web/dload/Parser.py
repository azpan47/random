from HTMLParser import HTMLParser

class Parser(HTMLParser):
	def __init__(self, mtag, mattr, dbg=False):
		#super(Parser,self).__init__()
		HTMLParser.__init__(self)
		self.mtag = mtag
		self.mattr = mattr
		self.dbg = dbg
		self.results = []

	def handle_starttag(self, tag, attrs):
		if(self.dbg):
			print "_dbg_ Start tag:", tag
			for attr in attrs:
				print "_dbg_ attr:", attr

		if(tag == self.mtag):
			if(attrs[0][0] == self.mattr):
				self.results.append(attrs[0][1])
