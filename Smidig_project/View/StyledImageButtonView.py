import tkinter as tk
from Controller.FinishedImageButtonController import FinishedImageButton

class StyledImageButton:
    def __init__(self, master):
        self.master = master
        self.file_label = tk.Label(self.master, text="File:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10)
        self.file_entry = tk.Entry(self.master, width=50)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10)
        self.button = tk.Button(self.master, text="Browse", command=self.select_image_file)
        self.button.grid(row=0, column=2, padx=10, pady=10)
        self.finished_image_button = FinishedImageButton(self.file_entry)

    def select_image_file(self):
        self.finished_image_button.select_image_file()
