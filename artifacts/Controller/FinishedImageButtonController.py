import tkinter as tk
from tkinter import filedialog, messagebox

class FinishedImageButton:
    def __init__(self, file_entry):
        self.file_entry = file_entry

    def select_image_file(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[
                ("Mem files", "*.mem"),
                ("Raw files", "*.raw")
            ]
        )

        if file_path:
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
