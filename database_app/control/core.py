# John Dunham
# Defines the core of the controller component for this application.

import view.core as view
import model.core as model

class Application():
	def __init__(self, master):
		view.MainWindow(master)
		
