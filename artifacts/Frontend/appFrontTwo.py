import tkinter as tk
from tkinter import ttk, filedialog
import requests
from components import create_widgets, browse_file, scan_file, update_command_options, update_manual_entry, update_table

class Application(tk.Tk):
    """
    Main application class for the Tkinter GUI.
    This class sets up the main window, initializes GUI widgets, and handles
    interactions such as file browsing, scanning, and updating the display.
    """
    
    def __init__(self):
        super().__init__()
        self.title("Artifacts")
        self.geometry("1000x700")
        self.create_widgets()
        
    def create_widgets(self):
        # Create and initialize GUI widgets.
        create_widgets(self)
        
    def browse_file(self):
        # Handle file browsing and selection.
        browse_file(self)
        
    def scan_file(self):
        # Handle file scanning and send the scan request to the backend.
        scan_file(self)
            
    def update_command_options(self, event):
        # Update command options based on the selected platform.
        update_command_options(self, event)
        
    def update_manual_entry(self, event):
        # Update the manual command entry based on the selected command.
        update_manual_entry(self, event)
            
    def update_table(self, output):
        # Update the results table with the output from the scan.
        update_table(self, output)

if __name__ == "__main__":
    # Create an instance of the application and start the main loop
    app = Application()
    app.mainloop()
