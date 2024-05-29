import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def select_image_file():
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
        # Update the file entry field
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Create the main window
root = tk.Tk()
root.title("Image File Selector")

# Create a label and entry field for the file input
file_label = tk.Label(root, text="File:")
file_label.grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)

# Load the icon image, resize it, and convert it to a PhotoImage object
icon_image = Image.open("icon.png")
icon_image = icon_image.resize((30, 30), Image.Resampling.LANCZOS)  # Updated to use the correct resampling method
icon = ImageTk.PhotoImage(icon_image)

# Create and place the button with the resized icon
select_button = tk.Button(root, image=icon, command=select_image_file)
select_button.grid(row=0, column=2, padx=10, pady=10)
select_button.image = icon  # Keep a reference to prevent garbage collection

# Run the application
root.mainloop()

