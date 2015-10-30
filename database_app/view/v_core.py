# John Dunham
# Defines the core of the view component for this application.

import tkinter as tk
from tkinter import filedialog 
from tkinter import * 
from tkinter import ttk


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
		
		# Categories
		self.category_notebook=ttk.Notebook(self.controller.root)
		
		self.category_collections_frame = ttk.Frame(self.category_notebook) # The Collections frame.
		self.category_groups_frame      = ttk.Frame(self.category_notebook) # The groups frame. TODO make better name
		self.category_notebook.add(self.category_collections_frame, text='Collections')
		self.category_notebook.add(self.category_groups_frame, text='Groups')

		self.category_collections_tree=ttk.Treeview(self.category_collections_frame,show="tree")
		self.category_groups_tree=ttk.Treeview(self.category_groups_frame,show="tree")


		# Entries.
		self.entry_frame= ttk.Labelframe(self.controller.root,text="Entries")
		
		self.entry_tree=ttk.Treeview(self.entry_frame,show="headings")
		self.entry_frame.grid(row=0,column=1)
		
		self.category_notebook.grid(row=0, column=0)
		
		# GUI options, may need to refine.
		self.active_collection=""
		self.active_type=""
		self.active_entry=""
		
	def show_collections(self, collections):
		# First clear the previous collection list.		
		if self.category_collections_tree:
			self.category_collections_tree.destroy() 	
		
		# Remake the listbox 
		self.category_collections_tree=ttk.Treeview(self.category_collections_frame,show="tree")
		
		for collection in collections:
			collection_name=collection[0]
			
			# Add the existing types.
			types, category = self.controller.get_table_types(collection_name)
			
			if category == 1:
				id=self.category_collections_tree.insert('', END, text=collection_name)
			
				for type in types:
					print (type)
					self.category_collections_tree.insert(id, END, text=type[0])
			else:
				id=self.category_groups_tree.insert('', END, text=collection_name)
			
				for type in types:
					print (type)
					self.category_groups_tree.insert(id, END, text=type[0])
		
		# Bind the opening command for categories to actually enter the 
		self.category_collections_tree.bind("<Double-Button-1>", self.open_collection)
		self.category_collections_tree.bind("<Return>", self.open_collection)
		self.category_collections_tree.grid(row=0, column=0)
		
		self.category_groups_tree.bind("<Double-Button-1>", self.open_group)
		self.category_groups_tree.bind("<Return>", self.open_group)
		self.category_groups_tree.grid(row=0, column=0)
	
	# I hope this is pass by reference...
	def show_entries(self, entries):
		if not entries:
			return
			
		# First clear the previous entry list.		
		if self.entry_tree:
			self.entry_tree.destroy()
		
		# Remake the listbox 
		self.entry_tree=ttk.Treeview(self.entry_frame, show="headings", columns=self.controller.entry_attributes)

		# add the entry headings
		for col in self.controller.entry_attributes:
			self.entry_tree.heading(col, text=col)
		
		# add the entry to the list.
		for entry in entries:
			# Parent, where, identifier, values.
			self.entry_tree.insert('',END, entry[self.controller.id_loc], values=entry)	

		
		self.entry_tree.bind("<Double-Button-1>", self.open_entry)
		self.entry_tree.bind("<Return>", self.open_entry)
			
		self.entry_tree.grid(row=0, column=1, sticky="WENS")

	def open_group(self, event):
		item     = self.category_collections_tree.identify('item',event.x,event.y)
		parent   = self.category_collections_tree.parent(item)
		
		if parent:
			#self.active_type = self.category_collections_tree.item(item, "text")
			#self.active_collection = self.category_collections_tree.item(parent, "text")
			pass
			#self.controller.open_type(self.active_collection, self.active_type)
		else:
			#self.active_type = ""
			#self.active_collection = self.category_collections_tree.item(item, "text")			
			#self.controller.open_table(self.active_collection)
			pass
	
	def open_collection(self, event):
		item     = self.category_collections_tree.identify('item',event.x,event.y)
		parent   = self.category_collections_tree.parent(item)
		
		if parent:
			self.active_type = self.category_collections_tree.item(item, "text")
			self.active_collection = self.category_collections_tree.item(parent, "text")
			
			#self.controller.open_type(self.active_collection, self.active_type)
		else:
			self.active_type = ""
			self.active_collection = self.category_collections_tree.item(item, "text")			
			self.controller.open_table(self.active_collection)
			

	def open_entry(self, event):
		item              = self.entry_tree.identify('item',event.x,event.y)
		self.active_entry = self.entry_tree.item(item, "text")

		print(item)
	
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
		
		
		
