#!/usr/bin/python

import urllib2 as ul2
import urllib as ul
import re
import Parser
import dloader

url = "http://brahmasri.com/Rama"
ext = "mp3"
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
		#print result
		urls.append(result)

dl = dloader.dloader(urls)

response.close()


