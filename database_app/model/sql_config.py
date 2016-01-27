# John Dunham
# Defines the group behavior.
import json

class SQLConfig():
     def __init__(self, filename):
          with open(filename,'r') as file:
               db_config = json.load(file)
          
          self.collection_queries = db_config["Collection_Queries"]
          self.group_queries = db_config["Group_Queries"]
          self.tables = db_config["Tables"]
          
