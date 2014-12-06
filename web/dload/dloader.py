#from __future__ import (division, absolute_import, print_function, unicode_literals)
#from __future__ import print_function as printf
import sys, os, tempfile, logging
import re

if sys.version_info >= (3,):
	import urllib.request as ul2
	import urllib.parse as up
else:
	import urllib2 as ul2
	import urlparse as up

class dloader:

	def __init__(self, urls, desc="/media/azpan/64129DD7456AA94F/dload/music"):
		self.urls = urls
		for url in self.urls:
			self.download_file(url, desc)

	def download_file(self, url, desc):
		print url
		url = ul2.unquote(url)
		print url
		scheme, netloc, path, query, fragment = up.urlsplit(url)
		fname = os.path.basename(path)
		dname = os.path.dirname(path)
		if os.path.isabs(dname):
			dname = dname.lstrip('/')
		dname = os.path.join(desc, dname)

		fname = re.sub('[^\.\w\s-]', '', fname)
		fname = re.sub('[-\s]+', '-', fname).strip().lower()
		fname = os.path.join(dname, fname)

		if not os.path.exists(dname):
			os.makedirs(dname)
		
		qurl = ul2.quote(url, safe="%/:=&?~#+!$,;'@()*[]|")	
		response = ul2.urlopen(qurl)

		with open(fname, 'wb') as f:
			meta = response.info()
			meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
			meta_len = meta_func("Content-Length")
			file_size = None
			if meta_len:
				file_size = int(meta_len[0])
			print "Downloading: {0} Bytes: {1}" . format(url, file_size)
			print fname

			file_size_dl = 0
			block_sz = 8192

			while True:
				buffer = response.read(block_sz)
				if not buffer:
					break

				file_size_dl += len(buffer)
				f.write(buffer)

				status = "{0:16}" . format(file_size_dl)

				if file_size:
					status += " [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
				#status += chr(13)
				#rint '{0}\r' . format(status)
				sys.stdout.write("%s\r" %(status))

		print
		return fname

