# John Dunham
import sys
import tkinter as tk
import control.c_core as controller

def main():
     root = tk.Tk() # Root Widget
     root.state('zoomed')
     frame = tk.Frame(root)
     root.title('Collect DB')
     app = controller.Application(root)     # Setup the Chips to let them fall.
     root.mainloop()     # Enter the Tkinter loop.
      
# This runs main.
if __name__ == '__main__':
     main()
