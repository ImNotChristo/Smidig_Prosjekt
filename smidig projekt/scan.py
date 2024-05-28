import tkinter as tk
from tkinter import ttk

class CurtainDropdown:
    def __init__(self, root, options):
        self.root = root
        self.options = options
        self.variables = []
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.dropdown_button = ttk.Button(self.frame, text="Select Options", command=self.toggle_dropdown)
        self.dropdown_button.grid(row=0, column=0, sticky=tk.W)
        self.dropdown_open = False

        self.checkbuttons_frame = ttk.Frame(self.frame)
        self.create_checkbuttons()

    def create_checkbuttons(self):
        for idx, option in enumerate(self.options):
            var = tk.StringVar(value="")
            chk = ttk.Checkbutton(self.checkbuttons_frame, text=option, variable=var, onvalue=option, offvalue="")
            chk.grid(row=idx, column=0, sticky=tk.W)
            self.variables.append(var)

        self.show_selected_button = ttk.Button(self.checkbuttons_frame, text="Show Selected", command=self.show_selected)
        self.show_selected_button.grid(row=len(self.options), column=0, sticky=tk.W)

    def toggle_dropdown(self):
        if self.dropdown_open:
            self.checkbuttons_frame.grid_forget()
        else:
            self.checkbuttons_frame.grid(row=1, column=0, sticky=tk.W)
        self.dropdown_open = not self.dropdown_open

    def show_selected(self):
        selected_items = [var.get() for var in self.variables if var.get()]
        print("Selected items:", selected_items)

root = tk.Tk()
root.title("Curtain Dropdown Menu")

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
dropdown = CurtainDropdown(root, options)

root.mainloop()
