from tkinter import *
from functools import partial 
import random


class Welcome_Screen:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "light blue"
        # Frame
        self.converter_frame = Frame(width=200, height=200, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Main Heading (row 0)

        # Centimetres and Inches Button (row 1)

        # Metres and Feet Button (row 1)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()                                 