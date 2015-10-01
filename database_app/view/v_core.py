# John Dunham
# Defines the core of the view component for this application.

import tkinter as tk
from tkinter import filedialog 
from tkinter import *
#
# TODO design a proper MVC pattern for this, it may be to learn python, but I can do it right.
#

class View():
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
		
		self.filemenu.add_command(label="New", command=self.new_database)
		self.filemenu.add_command(label="Open", command=self.open_database)
		self.filemenu.add_command(label="Save", command=self.save_database)
		self.filemenu.add_command(label="Save As", command=self.save_database_as)
		self.filemenu.add_command(label="Save Copy As", command=self.save_database_copy)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Import CSV", command=self.import_csv)
		self.filemenu.add_command(label="Export CSV", command=self.export_csv)
		self.filemenu.add_separator()
		self.filemenu.add_command(label="Exit",command=control.root.quit)
		######################################
		

		######################################
		# Add to cascade
		######################################
		self.menubar.add_cascade(label="File",menu=self.filemenu)
		self.controller.root.config(menu=self.menubar)
		
		
		# Actual content.
		self.category_frame=tk.Frame(self.controller.root)
		self.category_list=tk.Listbox(self.category_frame)
		self.entry_list=tk.Listbox(self.category_frame)

		
		self.category_frame.pack()
		
	def show_collections(self, collections):
		# First clear the previous collection list.		
		if self.category_list:
			self.category_list.destroy()
		
		# Remake the listbox 
		self.category_list=tk.Listbox(self.category_frame)
		
		for collection in collections:
				
			self.category_list.insert(END, collection[0])
		
		# Bind the opening command for categories to actually enter the 
		self.category_list.bind("<Double-Button-1>", self.open_category)
		self.category_list.bind("<Return>", self.open_category)

		self.category_list.pack()
		
	
	# I hope this is pass by reference...
	def show_entries(self, entries):
		if not entries:
			return
			
		# First clear the previous entry list.		
		if self.entry_list:
			self.entry_list.destroy()
		
		# Remake the listbox 
		self.entry_list=tk.Listbox(self.category_frame)
		
		for entry in entries:
			# Make this better!
			self.entry_list.insert(END, entry[4])
		
		self.entry_list.bind("<Double-Button-1>", self.open_entry)
		self.entry_list.bind("<Return>", self.open_entry)
			
		self.entry_list.pack()

	def open_category(self, event):
		widget    = event.widget
		selection = widget.curselection()
		table     = widget.get(selection[0])
		self.controller.open_table(table)	

	def open_entry(self, event):
		widget    = event.widget
		selection = widget.curselection()
		entry     = widget.get(selection[0])
		print(entry)
	
	######################################
	# Create File
	######################################
	def new_file(self, path, filename, ext):
		return filedialog.asksaveasfilename(initialdir=path, initialfile=filename)
	
	######################################
	# New								 #
	######################################
	def new_database(self):
		pass
		
		
	######################################
	# Open								 #
	######################################
	def open_database(self):
		filename= filedialog.askopenfilename(filetypes=[('sqlite database', '.db')])
		if filename:
			self.controller.open_db(filename);
		
	
	######################################
	# Save								 #
	######################################
	def save_database(self):
		pass
	
	
	######################################
	# Save As							 #
	######################################
	def save_database_as(self):
		pass
	
	
	######################################
	# Save Copy As						 #
	######################################
	def save_database_copy(self):
		pass
		
		
	######################################
	# Export CSV						 #
	######################################
	def export_csv(self):
		pass
	
	
	######################################
	# Import CSV						 #
	######################################
	def import_csv(self):
		''' Imports a csv file to the application. '''
		filename= filedialog.askopenfilename(filetypes=[('Comma Separated Values', '.csv')])
		
		if filename:
			self.controller.import_csv(filename)
		
	######################################
	# Quit      						 #
	######################################
	def quit(self):
		pass
		
		
		
