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
		self.toy_keys   = '''( _id INTEGER PRIMARY KEY AUTOINCREMENT, Accessories TEXT, Defects TEXT, Description TEXT, Count INTEGER, MSRP INTEGER, Value INTEGER, GPS INTEGER, Childhood INTEGER, Replace INTEGER,CONSTRAINT Location_id FOREIGN KEY(_id) REFERENCES Location(_id),CONSTRAINT Series_id FOREIGN KEY(_id) REFERENCES Series(_id),CONSTRAINT Class_id FOREIGN KEY(_id) REFERENCES Class(_id))'''
		self.toy_insert = '''( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )'''

		self.class_table  = 'Class'
		self.class_keys   = '''( _id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, CONSTRAINT Class_id FOREIGN KEY(_id) REFERENCES Class(_id) )'''
		self.class_insert = '''( ?, ?, ? )'''

		
		self.series_table = 'Series'
		self.series_keys  = '''( _id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, ShortName TEXT, CONSTRAINT Series_id FOREIGN KEY(_id) REFERENCES Series(_id) )'''
		self.class_insert = '''( ?, ?, ?, ? )'''


		self.location_table = "Location"
		self.location_keys  = '''( _id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Description TEXT, Images TEXT, MSRP INTEGER, CONSTRAINT Location_id FOREIGN KEY(_id) REFERENCES Location(_id))'''
		self.class_insert   = '''( ?, ?, ?, ?, ?, ? )'''

		
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
			
			print('''CREATE TABLE '''+ self.class_table + ''' ''' + self.class_keys)
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.class_table)
			self.dbcursor.execute('''CREATE TABLE '''+ self.class_table + ''' ''' + self.class_keys)	
			
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.series_table)
			self.dbcursor.execute('''CREATE TABLE '''+ self.series_table + ''' ''' + self.series_keys)	
			
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.location_table)			
			self.dbcursor.execute('''CREATE TABLE '''+ self.location_table + ''' ''' + self.location_keys)	
			
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.toy_table)
			self.dbcursor.execute('''CREATE TABLE '''+ self.toy_table + ''' ''' + self.toy_keys)
			
			tablemap=dict()
			
			# Populate the table.
			for row in collectionreader:
				# Find the table for this row, or default to the default table.
				#if(tableindex > 0):
				#	if ( row[tableindex] == self.location_table ):
				#		currenttable = self.location_table
				#	else:
				#		currenttable = self.default_table
				
				# Remove the table defining element from the row.
				#del row[tableindex]
				
				# If the table doesn't exist create it.
				#if not currenttable in tablemap:
				#	tablemap[currenttable] = 1
				#	self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ currenttable)	
				#	self.dbcursor.execute('''CREATE TABLE '''+ currenttable + ''' ''' + keystring)	
				
				#try:
			    #   self.dbcursor.execute("INSERT INTO " + currenttable + " VALUES " + insertstring, row )
				#except:
				#	print ("import failed" )	
				pass	
			self.db.commit()
			
		self.controller.present_collections()

		
	