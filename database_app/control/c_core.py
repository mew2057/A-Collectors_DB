# John Dunham
# Defines the core of the controller component for this application.

import view.v_core as view
import model.m_core as model

class Application():
     def __init__(self, root):
          self.root  = root
          self.view  = view.View(self)
          self.model = model.Model(self)
          #select Toy.Name, Series.Name,Toy.Count  from Toy  LEFT OUTER JOIN Series where Toy.Series_id=Series._id And Series.Series_id=1 
          # Gets only the root types of the members of the collection.
          # Series parameterization, assumes it has the Series_id column
          # WITH Root (_id) AS 
          #	(SELECT DISTINCT Series.Series_id FROM TABLENAME LEFT JOIN SERIES ON TABLENAME.Series_id=Series._id ) 
          # SELECT Series._id,Series.Name FROM Root LEFT Join Series ON Root._id=Series._id

          self.id_loc=3
          self.default_attributes="Toy.Name,Series_id, Toy.Count,Toy._id"
          self.entry_attributes=["Name","Series","Count"]
          
     def import_csv(self, file):
          self.model.import_csv(file)
          
     def db_missing(self, path, filename):
          return self.view.new_file(path, filename, '.db')
     
     def open_db(self, file):
          self.model.open_db(file)
     
     def open_table(self, table_name):
          print("Opening "+ table_name)
          if table_name != '':
               self.view.show_entries(self.model.list_all_default_entries(table_name))
     
     def get_table_types(self, table_name):
          return self.model.list_types(table_name)
     
     def open_type(self, table_name, type):
          self.view.show_entries(self.model.list_default_entries(table_name, type))	
     
     def present_collections(self):
          self.view.show_collections(self.model.list_collection())
          
     
     
