# John Dunham
# Defines the core of the model component for this application.

import csv
import sqlite3 
import os

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
		self.defaulttable='collection'
		
		self.controller=control
		
	def opendb(self, filename):
		# TODO try
		self.databasefile = filename
		self.databasedir  = os.path.dirname(self.databasefile)
		
		if self.db:
			self.db.close
			
		self.db       = sqlite3.connect(self.databasefile)
		self.dbcursor = self.db.cursor()
		
		print(self.dbcursor.execute('SELECT DISTINCT Name FROM'+ self.defaulttable +";").fetchall())
		
		
		
	def importcsv(self, filename):
		print("opening "+ filename)
		
		print("Creating db ")
		
		# Make sure there's a database file before populating a database.
		self.databasefile = self.controller.dbmissing( os.path.dirname(filename), os.path.basename(filename)[:-4] + '.db' )
		self.databasedir  = os.path.dirname(self.databasefile)
		
		# If no file was created, abandon ship.
		if not self.databasefile:
			return
		
		os.remove(self.databasefile)
		
		# If the db points to something attempt to close the connection.
		if self.db : 
			self.db.close()
			
		# Connect to the database.
		self.db       = sqlite3.connect(self.databasefile)
		self.dbcursor = self.db.cursor()
		
		# Super Hacky
		
		# Open the file in question
		with open(filename, newline='') as csvfile:
			
			headers = Collectible()
			collectionreader=csv.reader(csvfile)		
			fieldnames=next(collectionreader)
			keydatatypes=next(collectionreader)
			
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
			self.dbcursor.execute('''CREATE TABLE '''+ self.defaulttable + ''' ''' + keystring)	
			
			#keys = ', '.join(collectionreader.fieldnames)

			# Populate the table.
			# TODO Tables based on Type?
			for row in collectionreader:
				try:
					self.dbcursor.execute("INSERT INTO " + self.defaulttable + " VALUES " +insertstring, row )
				except:
					pass
					
			self.db.commit()

		
	