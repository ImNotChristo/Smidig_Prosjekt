import tkinter as tk
from tkinter import filedialog, messagebox

class FinishedImageButton:
    def __init__(self, file_entry):
        # Entry widget for displaying the selected file path
        self.file_entry = file_entry

    def select_image_file(self):
        """
            Open a file dialog to select an image file and update the entry widget with the selected file path.
        """
        # Open a file dialog to select an image file
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
            # Display the selected file path in a message box
            messagebox.showinfo("Selected Image File", f"Selected file: {file_path}")
            # Clear the entry widget and insert the selected file path
            self.file_entry.delete(0, tk.END)
            self.file_entry.insert(0, file_path)
