# John Dunham
# Defines the core of the controller component for this application.

import view.v_core as view
import model.m_core as model

class Application():
	def __init__(self, root):
		self.root  = root
		self.view  = view.View(self)
		self.model = model.Model(self)
		
	def import_csv(self, file):
		self.model.import_csv(file)
		
	def db_missing(self, path, filename):
		return self.view.new_file(path, filename, '.db')
	
	def open_db(self, file):
		self.model.open_db(file)
	
	def open_table(self, table_name):
		print("Opening "+ table_name)
		self.view.show_entries(self.model.set_active_table(table_name))
		
	
	def present_collections(self):
		self.view.show_collections( self.model.list_collection())
		self.open_table()
		
	
	
