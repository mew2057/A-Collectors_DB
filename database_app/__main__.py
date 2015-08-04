# John Dunham
import sys
import Tkinter as tk
from tkFileDialog import askopenfilename
import view.core

	 
# This runs main.
if __name__ == '__main__':
	root = tk.Tk() # Root Widget.
	app = view.core.ApplicationView(root)     # Setup the Chips to let them fall.
	root.mainloop()     # Enter the Tkinter loop.