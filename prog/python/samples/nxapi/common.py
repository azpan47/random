import ConfigParser
import sys
import urllib2
import xml.etree.ElementTree as et

class NXapiCommon:
	def __init__(self, cfgfile="nxapi.cfg"):
		cfg = self.__loadconfig(cfgfile)
		self.headers = {"Content-type" : "text/xml"}
		if not self.__login(cfg):
				print "Login failed"
				print self.logerror
				sys.exit(1)
		print self.sessionid


	def __loadconfig(self, cfgfile):

		config = ConfigParser.ConfigParser()
		config.read(cfgfile)
		cfg = {}

		try:
			cfg["hostname"] = config.get('api', 'hostname')
			cfg["port"] = config.get('api', 'port')
			cfg["version"] = config.get('api', 'version')
			cfg["username"] = config.get('credentials', 'username')
			cfg["password"] = config.get('credentials', 'password')
		except Exception as e:
			print "Error parsing config file"
			raise e

		cfg["url"] = "https://%s:%s/api/%s/xml" % (cfg["hostname"], cfg["port"], cfg["version"])

		return cfg

	def __login(self, cfg):
		data = "<LoginRequest user-id=\"%s\" password=\"%s\" />" % (cfg["username"], cfg["password"])
		try:
			req = urllib2.Request(cfg["url"], data, self.headers)
			response = urllib2.urlopen(req)
			content = response.read()

			resxml = et.fromstring(content)

			if resxml.attrib.get('success') != '0':
				self.sessionid = resxml.attrib.get('session-id')
				return True
			else
				self.logerror = resxml[0][0][0].text
				return False

		except Exception as e:
			print "Exception logging in"
			raise e
			sys.exit(1)

		
		
