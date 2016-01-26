# John Dunham
# Defines the core of the controller component for this application.

import view.v_core as view
import model.m_core as model

class Controller():
     def __init__(self, view):
          self.view  = view
          self.model = model.Model(self)
          self.id_loc=3
          self.default_attributes="Toy.Name,Series_id, Toy.Count,Toy._id"#self.root  = root
          self.entry_attributes=["Name","Series","Count"]
          
          #
          #
          ##select Toy.Name, Series.Name,Toy.Count  from Toy  LEFT OUTER JOIN Series where Toy.Series_id=Series._id And Series.Series_id=1 
          ## Gets only the root types of the members of the collection.
          ## Series parameterization, assumes it has the Series_id column
          ## WITH Root (_id) AS 
          ##	(SELECT DISTINCT Series.Series_id FROM TABLENAME LEFT JOIN SERIES ON TABLENAME.Series_id=Series._id ) 
          ## SELECT Serises._id,Series.Name FROM Root LEFT Join Series ON Root._id=Series._id
          #
          #
          #
          #
     def import_csv(self, file):
          self.model.import_csv(file)
          
     def db_missing(self, path, filename):
          pass
          #return self.view.new_file(path, filename, '.db')
     
     def open_db(self, file):
          self.model.open_db(file)
     
     def open_table(self, table_name):
          pass
          #print("Opening "+ table_name)
          #if table_name != '':
          #	self.view.show_entries(self.model.list_all_default_entries(table_name))
     
     def get_table_types(self, table_name):
          rpass
          #eturn self.model.list_types(table_name)
     
     def open_type(self, table_name, type):
          pass
          #self.view.show_entries(self.model.list_default_entries(table_name, type))	
     
     def present_collections(self):
          pass
          #self.view.show_collections(self.model.list_collection())
          
     
     
