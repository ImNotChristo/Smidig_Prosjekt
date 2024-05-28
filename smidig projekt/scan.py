import tkinter as tk
from tkinter import ttk

class CurtainDropdown:
    def __init__(self, root, options):
        self.root = root
        self.options = options
        self.selected_option = tk.StringVar()
        
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.dropdown_button = ttk.Button(self.frame, text="Select Option", command=self.toggle_dropdown)
        self.dropdown_button.grid(row=0, column=0, sticky=tk.W)
        self.dropdown_open = False

        self.combobox = ttk.Combobox(self.frame, textvariable=self.selected_option, values=self.options)
        self.combobox.bind("<<ComboboxSelected>>", self.on_select)
        
        self.show_selected_button = ttk.Button(self.frame, text="Show Selected", command=self.show_selected)
        self.show_selected_button.grid(row=2, column=0, sticky=tk.W)

    def toggle_dropdown(self):
        if self.dropdown_open:
            self.combobox.grid_forget()
        else:
            self.combobox.grid(row=1, column=0, sticky=tk.W)
        self.dropdown_open = not self.dropdown_open

    def on_select(self, event):
        self.dropdown_open = False
        self.combobox.grid_forget()
        self.dropdown_button.config(text=self.selected_option.get())

    def show_selected(self):
        print("Selected item:", self.selected_option.get())

root = tk.Tk()
root.title("Curtain Dropdown Menu")

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
dropdown = CurtainDropdown(root, options)

root.mainloop()
