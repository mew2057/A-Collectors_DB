# John Dunham
# Defines the core of the view component for this application.
 
import tkinter as tk
from tkinter import filedialog 

#
# TODO design a proper MVC pattern for this, it may be to learn python, but I can do it right.
#

class View(tk.Frame):
	"""The Main Application Window"""
	
	def __init__(self, control):	
		# Set the controller for this view.
		self.controller = control
		
		self.menubar = tk.Menu(control.root)
		
		
		######################################
		# File r
		######################################
		self.filemenu = tk.Menu(self.menubar, tearoff=0)
		
		######################################
		# File Operations				     #
		######################################
		
		self.filemenu.add_command(label="New", command=self.askopenfile)
		self.filemenu.add_command(label="Open", command=self.opendatabase)
		self.filemenu.add_command(label="Save", command=self.askopenfile)
		self.filemenu.add_command(label="Save As", command=self.askopenfile)
		self.filemenu.add_command(label="Save Copy As", command=self.askopenfile)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Import CSV", command=self.importcsv)
		self.filemenu.add_command(label="Export CSV", command=self.askopenfile)
		self.filemenu.add_separator()
		
		
		
		self.filemenu.add_command(label="Exit",command=control.root.quit)
		######################################
		
		
		######################################
		# Add to cascade
		######################################

		self.menubar.add_cascade(label="File",menu=self.filemenu)
		
		self.controller.root.config(menu=self.menubar)

	def askopenfile(self):
		"""Returns an opened file in read mode."""
		filename= filedialog.askopenfilename(filetypes=('Comma Separated Values', '.csv'))
		print(filename)		
	
	
	######################################
	# Create File
	######################################
	def newfile(self, path, filename, ext):
		return filedialog.asksaveasfilename(initialdir=path, initialfile=filename)
	
	######################################
	# New								 #
	######################################
	def NewDatabase(self):
		pass
		
		
	######################################
	# Open								 #
	######################################
	def opendatabase(self):
		filename= filedialog.askopenfilename(filetypes=[('sqlite database', '.db')])
		if filename:
			self.controller.opendb(filename);
		
	
	######################################
	# Save								 #
	######################################
	def SaveDatabase(self):
		pass
	
	
	######################################
	# Save As							 #
	######################################
	def SaveDatabaseAs(self):
		pass
	
	
	######################################
	# Save Copy As						 #
	######################################
	def SaveDatabaseCopy(self):
		pass
		
		
	######################################
	# Export CSV						 #
	######################################
	def ExportCSV(self):
		pass
	
	
	######################################
	# Import CSV						 #
	######################################
	def importcsv(self):
		''' Imports a csv file to the application. '''
		filename= filedialog.askopenfilename(filetypes=[('Comma Separated Values', '.csv')])
		
		if filename:
			self.controller.importcsv(filename)
		
	######################################
	# Quit      						 #
	######################################
	def Quit(self):
		pass
		
		
		
