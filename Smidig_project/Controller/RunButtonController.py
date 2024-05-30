import tkinter as tk

class RunButtonFunction:
    def __init__(self, master, command):
        self.master = master
        self.command = command
        # Create the Run button
        self.create_button()
    
    def create_button(self):
        """
            Create the Run button and set its command.
        """
        # Create a button widget with the text 'RUN' and assign the command
        self.btn = tk.Button(self.master, text='RUN', command=self.command)
        # Position the button using place geometry manager
        self.btn.place(x=250, y=10)
