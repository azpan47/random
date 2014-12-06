#!/usr/bin/python

import urllib2 as ul2
import urllib as ul
import re
import Parser
import dloader

url = "http://brahmasri.com/ShivaMahaPuranam"
url = "http://odin-server.fr.nf/public/PARTAGE/torrents/Ethical%20Hacking%20and%20Penetration%20Testing%20%28Kali%20Linux%29/"
ext = "mp4"

cre = re.compile(ext)

response = ul2.urlopen(url)

# print response.info()

html = response.read()

#print html

parser = Parser.Parser("a", "href")

parser.feed(html)

urls = []

for result in parser.results:
	if(cre.search(result)):
		result = url + result
		#print result
		urls.append(result)

response.close()

dl = dloader.dloader(urls, "/media/azpan/TOSHIBA EXT/dload/auto")
