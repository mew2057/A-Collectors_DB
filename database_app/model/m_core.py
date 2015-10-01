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
		
		# The default table name.
		self.defaulttable='No_Type'
		
		# Show all option for the table
		self.all_table='Show All'
		
		self.current_table='*'
		
		self.controller=control
	
	# Queries the database for all tables.
	def list_tables(self):
		return self.dbcursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite%';").fetchall()
	
	def set_active_table(self, table_name='all'):
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
		#PRAGMA table_info(tablename
		#print(self.dbcursor.execute("PRAGMA table_info(collection);").fetchall())
		#print(self.dbcursor.execute("SELECT DISTINCT Type from collection;").fetchall())

		# Present the collections.
		self.controller.present_collections()
		
	def import_csv(self, filename):
		
		# Make sure there's a database file before populating a database.
		self.databasefile = self.controller.dbmissing( os.path.dirname(filename), os.path.basename(filename)[:-4] + '.db' )
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
		
		# Super Hacky
		# TODO clean this up when we have the functionality we want.
		# Open the file in question
		with open(filename, newline='') as csvfile:
			
			headers = Collectible()
			collectionreader=csv.reader(csvfile)		
			fieldnames=next(collectionreader)
			keydatatypes=next(collectionreader)
			
			tableindex=-1
			
			# Generate the keys for the database.
			keystring='''('''
			insertstring='''('''
			for field,datatype in zip(fieldnames, keydatatypes):
				type=datatype
				
				# TODO store this better
				if datatype == "MONEY":
					type="NUMBER" # this should be INTEGER
				elif datatype == "BOOLEAN":
					type="INTEGER"
				elif datatype == "TABLE": # We shouldn't create a table for this.
					tableindex=fieldnames.index(field)
					continue 
					
				
				# This is a hack!
				if field == '_id':
					keystring += field + " " + type + " PRIMARY KEY AUTOINCREMENT,"
				else:
				#	self.dbcursor.execute()
					keystring += field + " " + type + ","
					
				insertstring+="?,"
			
			keystring = keystring[:-1] + ''')'''
			insertstring = insertstring[:-1] + ''')'''
			

			# This is probably terrible practice.
			# This acts as a fallback table.
			self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ self.defaulttable)
			
			
			currenttable=self.defaulttable
			tablemap=dict()
			
			# Populate the table.
			for row in collectionreader:
				# Find the table for this row, or default to the default table.
				if(tableindex > 0):
					if ( row[tableindex] != '' ):
						currenttable = row[tableindex].replace(' ','_')
					else:
						currenttable = self.defaulttable
				
				# Remove the table defining element from the row.
				del row[tableindex]
				
				# If the table doesn't exist create it.
				if not currenttable in tablemap:
					tablemap[currenttable] = 1
					self.dbcursor.execute('''DROP TABLE IF EXISTS '''+ currenttable)	
					self.dbcursor.execute('''CREATE TABLE '''+ currenttable + ''' ''' + keystring)	
				
				try:
					self.dbcursor.execute("INSERT INTO " + currenttable + " VALUES " +insertstring, row )
				except:
					print ("import failed"  )
			
			# No type should be the last table
			self.dbcursor.execute('''CREATE TABLE IF NOT EXISTS '''+ self.defaulttable + ''' ''' + keystring)	
					
			self.db.commit()
			
		self.controller.present_tables()

		
	