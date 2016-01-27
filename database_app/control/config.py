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
          self.config_file = file_location
          
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
     
     config --- configparser object, used to access the ini file.
     '''
     def __parse_sections(self, config):
          
          # Check to see if the proxy section is present.
          if config.has_section('user.settings'):
               self.__get_user_settings(config['user.settings'])

     ''' Retrieves the user settings.
     
     Keyword arguments:
     user_settings --- A section retrieved from the configparser.
     '''
     def __get_user_settings(self, user_settings):
          
          # Initialize the proxy settings.
          self.user_settings  = UserSettings()
          self.user_settings.write_function = self.write_user_settings

          # Grab the last dir and the last db used.
          self.user_settings.last_dir = user_settings.get('last_dir')
          self.user_settings.last_db  = user_settings.get('last_db')
          
     ''' Writes the user settings.
     '''     
     def write_user_settings(self):
          config_parser = configparser.ConfigParser()
          config_parser.read(self.config_file)
          
          config_parser['user.settings'] = self.user_settings.__dict__
          del config_parser['user.settings']['write_function']
                   
          with open(self.config_file, 'w') as config_file:
               config_parser.write(config_file)
          
          
# A structure for holding user settings.
class UserSettings(object):
     write_function = None
     
     last_dir     = ''
     last_db      = ''
     
     def set_last_dir(self,directory):
          self.last_dir = directory
          self.write_function()
          
     def set_last_db(self,db,directory):
          self.last_db = db
          self.last_dir = directory
          self.write_function()
