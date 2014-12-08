import ConfigParser
import sys
import urllib2
import xml.etree.ElementTree as et

class NXapiCommon:
	def __init__(self, cfgfile="nxapi.cfg"):
		self.__loadconfig(cfgfile)

	def __loadconfig(self, cfgfile):

		config = ConfigParser.ConfigParser()
		config.read(cfgfile)

		try:
			self.cfg["hostname"] = config.get('api', 'hostname')
			self.cfg["port"] = config.get('api', 'port')
			self.cfg["version"] = config.get('api', 'version')
			self.cfg["username"] = config.get('credentials', 'username')
			self.cfg["password"] = config.get('credentials', 'password')
		except:
			print "Error parsing config file"
			raise
