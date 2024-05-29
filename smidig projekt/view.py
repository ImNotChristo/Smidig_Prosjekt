# view.py

import tkinter as tk
from tkinter import ttk
from controller import SearchableCombobox  # Import the SearchableCombobox class

class StyledDropdown:
    def __init__(self, root, options):
        self.root = root
        self.options = options
        self.selected_option = tk.StringVar(value="Choose option")

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label = ttk.Label(self.frame, text="Scan:", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=(0, 10), sticky=tk.W)

        self.combobox = SearchableCombobox(self.frame, textvariable=self.selected_option)
        self.combobox.set_completion_list(self.options)
        self.combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.show_selected_button = ttk.Button(self.frame, text="Show Selected", command=self.show_selected)
        self.show_selected_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

    def show_selected(self):
        print("Selected item:", self.selected_option.get())

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Searchable Dropdown Menu")
    root.geometry("400x400")  # Set the size of the window

    # List of options with a placeholder option at the beginning
    options = [
        "Choose option", "windows.pslist", "windows.psscan", "windows.pstree", "windows.cmdline",
        "windows.services", "windows.registry", "windows.filescan", "windows.malware",
        "windows.network", "windows.memory", "windows.disk", "windows.eventlog",
        "windows.prefetch", "windows.timeline", "windows.locks", "windows.hooks",
        "windows.sysinfo", "windows.drivers", "windows.pipes", "windows.sockets"
    ]
    sorted_options = sorted(options)
    dropdown = StyledDropdown(root, sorted_options)

    root.mainloop()
