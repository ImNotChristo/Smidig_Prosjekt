import tkinter as tk
from tkinter import ttk
from Controller.DropdownMenu import SearchableCombobox

class StyledDropdown:
    # style on the popup window and assigning it also the method SearchableCombobox for functionality and searching
    def __init__(self, root, options):
        self.root = root
        self.options = options
        self.selected_option = tk.StringVar(value="")

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label = ttk.Label(self.frame, text="Scan:", font=("Helvetica", 12))
        self.label.grid(row=0, column=0, padx=(0, 10), sticky=tk.W)

        self.combobox = SearchableCombobox(self.frame, textvariable=self.selected_option)
        self.combobox.set_completion_list(self.options)
        self.combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))

        self.show_selected_button = ttk.Button(self.frame, text="Show Selected", command=self.show_selected)
        self.show_selected_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))

    #show selected shows the item that we selected when pressing Scan button
    def show_selected(self):
        print("Selected item:", self.selected_option.get())

# assigning the imported library to root for the frontend side
root = tk.Tk()
root.title("Searchable Dropdown Menu")
root.geometry("400x400")  # Set the size of the window

# List of options
options = [
    "windows.pslist", "windows.psscan", "windows.pstree", "windows.cmdline",
    "windows.services", "windows.registry", "windows.filescan", "windows.malware",
    "windows.network", "windows.memory", "windows.disk", "windows.eventlog",
    "windows.prefetch", "windows.timeline", "windows.locks", "windows.hooks",
    "windows.sysinfo", "windows.drivers", "windows.pipes", "windows.sockets"
]
# sending our sorted list into StyledDropdown method and assinging to dropdown variable
sorted_options = sorted(options)
dropdown = StyledDropdown(root, sorted_options)
