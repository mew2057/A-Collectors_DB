# John Dunham
import sys
import tkinter as tk
from application.database_app import DatabaseApp




def main():
	DatabaseApp().run()
	#root = tk.Tk() # Root Widget.
	#frame = tk.Frame(root)
	#root.title('Collect DB')
	#app = controller.Application(root)     # Setup the Chips to let them fall.
	#root.geometry("850x300")
	#root.mainloop()     # Enter the Tkinter loop.

# This runs main.
if __name__ == '__main__':
	main()

