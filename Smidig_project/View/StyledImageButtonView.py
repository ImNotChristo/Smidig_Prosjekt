import tkinter as tk
from Controller.FinishedImageButtonController import FinishedImageButton

class StyledImageButton:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create file selection widgets
        self.file_label = tk.Label(self.master, text="File:")
        self.file_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.file_entry = tk.Entry(self.master, width=40)
        self.file_entry.grid(row=0, column=1, padx=10, pady=10)

        self.button = tk.Button(self.master, text="Browse", command=self.select_image_file)
        self.button.grid(row=0, column=2, padx=10, pady=10)

        self.finished_image_button = FinishedImageButton(self.file_entry)

    def select_image_file(self):
        # Open file dialog to select an image file
        self.finished_image_button.select_image_file()
