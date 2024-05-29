import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def select_image_file():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.png;*.raw;*.jpeg;*.gif;*.bmp")]
    )
    if file_path:
        # Display the selected file path in a message box
        messagebox.showinfo("Selected Image File", f"Selected file: {file_path}")

# Create the main window
root = tk.Tk()
root.title("Image File Selector")

# Create a label and entry field for the file input
file_label = tk.Label(root, text="File:")
file_label.grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)

# Create and place the button
select_button = tk.Button(root, text="Select Image File", command=select_image_file)
select_button.grid(row=0, column=2, padx=10, pady=10)

# Run the application
root.mainloop()