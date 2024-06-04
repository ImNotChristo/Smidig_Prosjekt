import tkinter as tk
from Controller.OutputFieldController import OutputFieldController

class OutputField:
    def __init__(self, master):
        self.master = master
        self.controller = OutputFieldController(self)
        self.create_ouput_field()
        print("hello")
    
    def create_ouput_field(self):
        print("hei fra create_outputfield i OutputFieldView")
        self.text_output_field = tk.Text(self.master, height=20, width=90)
        self.text_output_field.pack()
        self.text_output_field.insert(tk.END, "Output skal printes her!")
        self.text_output_field.config(state=tk.DISABLED)

    def display_output_text(self, message):
        self.text_output_field.config(state=tk.NORMAL)
        self.text_output_field.insert(tk.END, message)
        self.text_output_field.config(state=tk.DISABLED)
    

