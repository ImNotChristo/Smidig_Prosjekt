import tkinter as tk
from View.terminal import MainApp

"""
appFrontMain.py

This file initializes and runs the main Tkinter application.
It imports and uses the MainApp class from the View.terminal module.
"""

# Initialize the root Tkinter window
root = tk.Tk()

# Create an instance of the main application
app = MainApp(root)

# Run the main application loop
app.run()
