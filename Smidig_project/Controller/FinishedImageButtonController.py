import tkinter as tk
from tkinter import filedialog, messagebox

class FinishedImageButton:
    def __init__(self, file_entry):
        self.file_entry = file_entry

    def select_image_file(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("JPEG files", "*.jpeg"),
                ("GIF files", "*.gif"),
                ("BMP files", "*.bmp"),
                ("All files", "*.*"),
                ("Raw files", "*.raw")
            ]
        )

        if file_path:
            messagebox.showinfo("Selected Image File", f"Selected file: {file_path}")
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)