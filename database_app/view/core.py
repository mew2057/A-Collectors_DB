# John Dunham
import Tkinter as tk
from tkFileDialog import *

class ApplicationView(tk.Frame):
	"""The Main Application Window"""
	
	def __init__(self, master):
		menubar = tk.Menu(master)
		
		
		######################################
		# File Option
		######################################
		filemenu = tk.Menu(menubar, tearoff=0)
		
		
		filemenu.add_command(label="Open", command=self.askopenfile)
		filemenu.add_separator()
		
		
		
		filemenu.add_command(label="Exit",command=master.quit)
		######################################
		
		
		######################################
		# Add to cascade
		######################################

		menubar.add_cascade(label="File",menu=filemenu)
		
		master.config(menu=menubar)

	def askopenfile(self):
		"""Returns an opened file in read mode."""

		return askopenfilename()
		
		
		
		
