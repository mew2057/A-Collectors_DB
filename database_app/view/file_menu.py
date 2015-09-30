# John Dunham
#
#
import tkinter as tk
from tkinter import filedialog

class FileMenu(tk.Menu):

	def __init__(self, parent):
		parent.add_command(label="New", command=self.askopenfile)
		pass
		
	def InitFileMenu():
		pass
	
	######################################
	# New								 #
	# 
	######################################
	def NewDatabase():
		pass
		
		
	######################################
	# Open								 #
	######################################
	def OpenDatabase():
		pass
	
	######################################
	# Save								 #
	######################################
	def SaveDatabase():
		pass
	
	
	######################################
	# Save As							 #
	######################################
	def SaveDatabaseAs():
		pass
	
	
	######################################
	# Save Copy As						 #
	######################################
	def SaveDatabaseCopy():
		pass
		
		
	######################################
	# Export CSV						 #
	######################################
	def ExportCSV():
		pass
	
	
	######################################
	# Import CSV						 #
	######################################
	def ImportCSV():
		pass
		
	######################################
	# Quit      						 #
	######################################
	def Quit():
		pass
	