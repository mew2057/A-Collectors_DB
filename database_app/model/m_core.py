# John Dunham
# Defines the core of the model component for this application.

import csv
import sqlite3 
import os
import sys

# A class that easily mutable.
class Collectible(object):
    pass


class Model():
	def __init__(self, control):
		#database=sqlite3
		self.databasefile=''
		self.databasedir=''
		
		self.db={}
		self.dbcursor={}
		
		# The default table name. This is really only useful for CSV now
		# TODO make a more robust solution.
		self.toy_table  = 'Toy'
		self.toy_keys   = '''( _id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Accessories TEXT, Defects TEXT, Description TEXT, Count INTEGER, MSRP INTEGER, Value INTEGER, GPS INTEGER, Childhood INTEGER, Replace INTEGER,Class_id INTEGER, Series_id INTEGER, Location_id INTEGER, FOREIGN KEY(Location_id) REFERENCES Location(_id), FOREIGN KEY(Series_id) REFERENCES Series(_id), FOREIGN KEY(Class_id) REFERENCES Class(_id) )'''
		self.toy_new = '''( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )'''

		self.class_table  = 'Class'
		self.class_keys   = '''( _id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT )'''
		self.class_create = '''( ? )'''
		self.class_create_key = '''( Name )'''

		
		self.series_table = 'Series'
		self.series_keys  = '''( _id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, ShortName TEXT, Series_id INTEGER, FOREIGN KEY(Series_id) REFERENCES Series(_id))'''
		self.series_create = '''( ?, ?, ?, ? )'''		
		self.series_insert = '''( ?, ?, ? )'''		
		self.series_create_key = '''( Name, ShortName, Series_id )'''


		self.location_table = "Location"
		self.location_keys  = '''( _id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Description TEXT, Images TEXT, MSRP INTEGER, Location_id INTEGER, FOREIGN KEY(Location_id) REFERENCES Location(_id))'''
		self.location_create   = '''(?, ?, ?, ?, ?, ? )'''
		self.location_create_key = '''( _id, Name, Description, Images, MSRP, Location_id )'''


		
		# This is a hack.
		self.collection_classifier='Type'
		
		self.current_table='*'
		
		self.controller=control
	
	# Queries the database for all tables.
	def list_collection(self):
		return self.dbcursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite%';").fetchall()

				
	def list_types(self, table_name):
		return self.dbcursor.execute("SELECT DISTINCT " + self.collection_classifier + " from " + table_name).fetchall()
	
	def list_all_default_entries(self, table_name):
		return self.dbcursor.execute("SELECT " + self.controller.default_attributes + " from " + table_name)	
		
	def list_entries(self, table_name, type):
		return self.dbcursor.execute("SELECT * from " + table_name + " WHERE type='" + type + "'" )		
	
	def list_default_entries(self, table_name, type):
		return self.dbcursor.execute("SELECT " + self.controller.default_attributes + " from " + table_name + " WHERE type='" + type + "'" )		

		
	def set_active_table(self, table_name):
		if not self.dbcursor:
			return
			
		self.current_table=table_name
				
		return self.dbcursor.execute("SELECT * from " + self.current_table).fetchall()
	
	def open_db(self, filename):
		# TODO try
		self.databasefile = filename
		self.databasedir  = os.path.dirname(self.databasefile)
		
		if self.db:
			self.db.close
			
		self.db       = sqlite3.connect(self.databasefile)
		self.dbcursor = self.db.cursor()	

		# Present the collections.
		self.controller.present_collections()

	def create_class():
		pass
	def import_series():
		pass
	def import_location():
		pass
	
	
	
	def import_csv(self, filename):
		
		# Make sure there's a database file before populating a database.
		self.databasefile = self.controller.db_missing( os.path.dirname(filename), os.path.basename(filename)[:-4] + '.db' )
		self.databasedir  = os.path.dirname(self.databasefile)
		
		# If no file was created, abandon ship.
		if not self.databasefile:
			return
		
		try:
			os.remove(self.databasefile)
		except:
			pass
		
		# If the db points to something attempt to close the connection.
		if self.db : 
			self.db.close()
			
		# Connect to the database.
		self.db       = sqlite3.connect(self.databasefile)
		self.dbcursor = self.db.cursor()
		
		# Super Hacky, Really just for my csv
		# TODO clean this up when we have the functionality we want.
		# Open the file in question
		with open(filename, newline='') as csvfile:
			
			collectionreader=csv.DictReader(csvfile)			
			
			# Nuke the old tables.	
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.class_table)
			self.dbcursor.execute('''CREATE TABLE '''+ self.class_table + ''' ''' + self.class_keys)	
			
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.series_table)
			self.dbcursor.execute('''CREATE TABLE '''+ self.series_table + ''' ''' + self.series_keys)	
			
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.location_table)			
			self.dbcursor.execute('''CREATE TABLE '''+ self.location_table + ''' ''' + self.location_keys)	
			
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.toy_table)
			self.dbcursor.execute('''CREATE TABLE '''+ self.toy_table + ''' ''' + self.toy_keys)
			
			classmap=dict()
			locationmap=dict()
			seriesmap=dict()
			
			# This is hacky, fast and lose
			# Populate the table.
			for row in collectionreader:
			
				# Location id.
				locid = row["LocID"] if row["LocID"] != '' else -1
				classid = -1
				seriesid= -1
				
				classification =  row["Classification"] if row["Classification"] != '' else 'N/A'
				
				
				
				# If it's a location.
				if row["Type"] == '''Location''':
					self.dbcursor.execute("INSERT INTO " + self.location_table + self.location_create_key + " VALUES " + self.location_create, 
					(row["_id"], row["Name"], row["Description"], "", 0, locid))
					continue
				
				# Check if Class Exists.
				if not classification in classmap :
					try:
						self.dbcursor.execute("INSERT INTO " + self.class_table + self.class_create_key + " VALUES " + self.class_create, (classification, ) )
						classmap[ classification ] = self.dbcursor.lastrowid
						classid = self.dbcursor.lastrowid
					except:
						print ("Class create failed!" )	
				else:
					classid = classmap[ classification ] 
				
				# Check if Series Exists.
				if not row["Type"] in  seriesmap:
					try:						
						self.dbcursor.execute("INSERT INTO " + self.series_table  + self.series_create_key  + " VALUES " + self.series_insert , (row["Type"], row["TypeCode"], -1) )
						seriesmap[ row["Type"] ] = self.dbcursor.lastrowid				
					except:
						print ("Type creation failed!" )
						
				if not row["Subline"] in  seriesmap:
					try:						
						self.dbcursor.execute("INSERT INTO " + self.series_table  + self.series_create_key  + " VALUES " + self.series_insert , (row["Subline"], row["SublineCode"], seriesmap[ row["Type"] ]) )
						seriesmap[ row["Subline"] ] = self.dbcursor.lastrowid
						seriesid = self.dbcursor.lastrowid						
					except:
						print ("Type creation failed!" )
				else:
					seriesid = seriesmap[ row["Subline"] ]
									
				try:
					self.dbcursor.execute("INSERT INTO " + self.toy_table + " VALUES " + self.toy_new, (row["_id"], row["Name"], row["Acessories"], row["Defects"], row["Description"], row["Count"], row["MSRP"],row["Value"],row["GPS"],row["Childhood"],row["Replace"],classid, seriesid, locid) )
				except:
					print("Toy import failed!")
			self.db.commit()
			
		self.controller.present_collections()

		
	