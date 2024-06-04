import tkinter as tk

class OutputFieldController:
    def __init__(self, view):
        self.view = view
        # self.create_ouputfield()

    def create_ouput_field(self):
        self.print("hei fra create_output_field i OutputFieldController")
        self.view.create_ouput_field()