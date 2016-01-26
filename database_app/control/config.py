'''
Defines a class which holds the various configuration settings used by 
a database tool. Class accepts an absolute file location on construction, 
which is used to parse configuration details.

Author --- John Dunham (jdunham@us.ibm.com)
Date Modified --- January 14, 2016
'''
import configparser


class Config(object):
	
	""" Construct the database config object. Opens the supplied config file
	using standard .ini syntax. This function should not be overriden.
	
	Keyword arguments:
	
	file_location --- The absolute path to the file. 	
	"""
	def __init__(self, file_location):
		
		#  Open the configuration file.
		config = configparser.ConfigParser()
		config.read(file_location)
				
		# Parse the sections
		self.__parse_sections( config)
		
	''' Verify that the supported sections exist then propagate the 
	settings objects. The default implementation of this function 
	populates the proxy and server settings objects for use in 
	connecting to the database index.
	
	Keyword arguments:
	
	config ---	configparser object, used to access the ini file.
	'''
	def __parse_sections(self, config):
		
		# Check to see if the proxy section is present.
		if config.has_section('proxy'):
			self.__get_proxy_info(config['proxy'])
			
		# Check to see if the database section is present.
		if config.has_section('database.server'):
			self.__get_database_server_info(config['database.server'])

	''' Retrieves the proxy configuration, e.g. host, port, and proxy 
	type.
	
 	Keyword arguments:
 	proxy_section --- A section retrieved from the configparser.
	'''
	def __get_proxy_info(self, proxy_section):
		
		# Initialize the proxy settings.
		self.proxy_settings  = ProxySettings()

		# Set the fields in the proxy settings if the user specified.
		host = proxy_section.get('host')
		if host != None:
			self.proxy_settings.host = host
		
		port = proxy_section.get('port')
		if port != None:
			self.proxy_settings.port = int(port)
		
		proxy_type = proxy_section.get('proxy_type')
		proxy_type = proxy_type.lower()

		# TODO (jdunham@us.ibm.com) May not need socks
		if ( proxy_type == 'socks4'):
			self.proxy_settings.proxy_type = socks.PROXY_TYPE_SOCKS4
		elif ( proxy_type == 'socks5'):
			self.proxy_settings.proxy_type = socks.PROXY_TYPE_SOCKS5
		elif ( proxy_type == 'http'):
			self.proxy_settings.proxy_type = socks.PROXY_TYPE_HTTP
		elif ( proxy_type == 'https'):
			self.proxy_settings.proxy_type = socks.PROXY_TYPE_HTTPS
				
	
	''' Retrieves the database server configuration, e.g. host, port, 
	protocol, and directory.
	
 	Keyword arguments:
 	database_server_section --- A section retrieved from the configparser.
	'''
	def __get_database_server_info(self, database_server_section):
		
		# Initialize the database server settings.
		database_server_settings = databaseServerSettings()		
		
		host = database_server_section.get('host')
		if host != None:
			database_server_settings.host = host
			
		port = database_server_section.get('port')
		if port != None:
			database_server_settings.port = int(port)
		
		protocol = database_server_section.get('protocol')
		if protocol != None:
			database_server_settings.protocol = protocol
		
		directory = database_server_section.get('directory')
		if directory != None:
			database_server_settings.directory = directory	
			
		self.database_base_uri = database_server_settings.construct_uri()
		
		
# A structure for holding proxy settings.
class ProxySettings(object):
	port 	   = -1
	host 	   = ''
	proxy_type = socks.PROXY_TYPE_SOCKS5
	
# A structure for holding the server information.
class databaseServerSettings(object):
	protocol   = 'http'
	port       = -1
	host       = ''
	directory  = 'database'
	
	def construct_uri(self):
		uri = self.protocol + "://" + self.host
		
		if self.port != -1:
			uri += ":" + str(self.port)
				
		return uri + "/" + self.directory + "/"
