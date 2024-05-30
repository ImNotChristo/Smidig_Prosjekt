import tkinter as tk
import PIL as pil
from Controller.FinishedImageButtonController import FinishedImageButton
from PIL import Image, ImageTk

class StyledImageButton:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # Create file selection widgets
        self.file_label = tk.Label(self.master, text="File:", font=("Helvetica", 12))
        self.file_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.file_entry = tk.Entry(self.master, width=50)
        self.file_entry.grid(row=0, column=1)

        # self.button = tk.Button(self.master, text="Browse", command=self.select_image_file)
        # self.button.grid(row=0, column=2, padx=10, pady=10)

        # Load the icon image, resize it, and convert it to a PhotoImage object
        self.icon_image = Image.open("images/folderIcon.png")
        self.icon_image = self.icon_image.resize((20, 20), Image.Resampling.LANCZOS)  # Updated to use the correct resampling method
        self.icon = ImageTk.PhotoImage(self.icon_image)

        # Create and place the button with the resized icon
        self.button = tk.Button(self.master, image=self.icon, command=self.select_image_file)
        self.button.grid(row=0, column=2, padx=2)
        self.button.image = self.icon  # Keep a reference to prevent garbage collection

        self.finished_image_button = FinishedImageButton(self.file_entry)

    def select_image_file(self):
        # Open file dialog to select an image file
        self.finished_image_button.select_image_file()
