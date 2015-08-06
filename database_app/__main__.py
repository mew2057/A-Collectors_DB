# John Dunham
import sys
import tkinter as tk
import control.core as controller

	 
# This runs main.
if __name__ == '__main__':
	root = tk.Tk() # Root Widget.
	app = controller.Application(root)     # Setup the Chips to let them fall.
	root.mainloop()     # Enter the Tkinter loop.