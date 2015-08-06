# John Dunham
# Defines the core of the view component for this application.
 
import tkinter as tk
 
#
# TODO design a proper MVC pattern for this, it may be to learn python, but I can do it right.
#

class View(tk.Frame):
	"""The Main Application Window"""
	
	def __init__(self, control):		
		menubar = tk.Menu(control.root)
		
		
		######################################
		# File r
		######################################
		filemenu = tk.Menu(menubar, tearoff=0)
		
		######################################
		# File Operations				     #
		######################################
		
		filemenu.add_command(label="New", command=self.askopenfile)
		filemenu.add_command(label="Open", command=self.askopenfile)
		filemenu.add_command(label="Save", command=self.askopenfile)
		filemenu.add_command(label="Save As", command=self.askopenfile)
		filemenu.add_command(label="Save Copy As", command=self.askopenfile)
		filemenu.add_separator()
		
		filemenu.add_command(label="Import CSV", command=self.askopenfile)
		filemenu.add_command(label="Export CSV", command=self.askopenfile)
		filemenu.add_separator()
		
		
		
		filemenu.add_command(label="Exit",command=control.root.quit)
		######################################
		
		
		######################################
		# Add to cascade
		######################################

		menubar.add_cascade(label="File",menu=filemenu)
		
		control.root.config(menu=menubar)

	def askopenfile(self):
		"""Returns an opened file in read mode."""
		filename= filedialog.askopenfilename(defaultextension='.csv')
		print(filename)		 
		
		
		
		
