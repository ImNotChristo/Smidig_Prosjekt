import tkinter as tk
from tkinter import ttk

class StyledDropdown:
    def __init__(self, root, options):
        self.root = root
        self.options = options
        self.selected_option = tk.StringVar()
        
        style = ttk.Style()
        style.configure("TCombobox", padding=5)
        style.configure("TLabel", font=("Helvetica", 12))
        
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label = ttk.Label(self.frame, text="Scan:", style="TLabel")
        self.label.grid(row=0, column=0, padx=(0, 10), sticky=tk.W)

        self.combobox = ttk.Combobox(self.frame, textvariable=self.selected_option, values=self.options, style="TCombobox")
        self.combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))
        
        self.show_selected_button = ttk.Button(self.frame, text="Show Selected", command=self.show_selected)
        self.show_selected_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

    def show_selected(self):
        print("Selected item:", self.selected_option.get())

root = tk.Tk()
root.title("Styled Dropdown Menu")
root.geometry( "400x400" ) # Set the size of the window

# List of 20 different options
options = [
    "windows.info", "windows.pslist", "windows.psscan", "windows.pstree", "windows.dumpfiles", 
    "windows.memmap", "windows.handles", "windows.dlllist", "windows.cmdline", "windows.netscan", 
    "windows.netstat", "windows.registry.printkey", "windows.filescan", "windows.dumpfiles"
]

dropdown = StyledDropdown(root, options)

root.mainloop()
