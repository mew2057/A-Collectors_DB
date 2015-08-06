# John Dunham
# Defines the core of the controller component for this application.

import view.v_core as view
import model.m_core as model

class Application():
	def __init__(self, root):
		self.root  = root
		self.view  = view.View(self)
		self.model = model.Model(self)
		
	
	
