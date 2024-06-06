import tkinter as tk
from PIL import Image, ImageTk
from Controller.FinishedImageButtonController import FinishedImageButton

class StyledImageButton:
    def __init__(self, master):
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.file_label = tk.Label(self.master, text="File:", font=("Helvetica", 12))
        self.file_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.file_entry = tk.Entry(self.master, width=50)
        self.file_entry.grid(row=0, column=1)

        self.icon_image = Image.open("images/folderIcon.png")
        self.icon_image = self.icon_image.resize((20, 20), Image.Resampling.LANCZOS)
        self.icon = ImageTk.PhotoImage(self.icon_image)

        self.button = tk.Button(self.master, image=self.icon, command=self.select_image_file)
        self.button.grid(row=0, column=2, padx=2)
        self.button.image = self.icon

        self.finished_image_button = FinishedImageButton(self.file_entry)

    def select_image_file(self):
        self.finished_image_button.select_image_file()

    def get_file_path(self):
        return self.file_entry.get()
