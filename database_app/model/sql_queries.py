# John Dunham
# Defines the group behavior.
import json

class SQLConfig():
     __init__(self):
          with open('db_config.json','r') as file:
               db_config = json.load(file)
          
          self.collection_queries = db_config["Collection_Queries"]
          self.group_queries = db_config["Group_Queries"]
          self.tables = db_config["Tables"]
          
          print (self.tables)
