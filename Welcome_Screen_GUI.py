from tkinter import *
from functools import partial 
import random


class Welcome_Screen:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "light blue"
        cm_and_in_button_colour = "lime green"
        m_and_ft_button_colour = "orange"

        # Frame
        self.converter_frame = Frame(width=200, height=200, bg=background_colour, pady=10)
        self.converter_frame.grid()

        # Main Heading (row 0)
        self.measurement_converter_label = Label(self.converter_frame, text = "Measurement Converter",
            font=("Arial", "20", "bold"),
            bg=background_colour,
            padx=10, pady=10)
        self.measurement_converter_label.grid(row=0)

        # Converter buttons frame
        self.converter_buttons_frame = Frame(self.converter_frame)
        self.converter_buttons_frame.grid(row=1, pady=10)

        # Centimetres and Inches Button (row 1)
        self.cm_and_in_converter_button = Button(self.converter_buttons_frame, text="Centimetres and Inches", bg=cm_and_in_button_colour, padx=10, pady=10)
        self.cm_and_in_converter_button.grid(row=1, column=0)

        # Metres and Feet Button (row 1)
        self.m_and_ft_converter_button = Button(self.converter_buttons_frame, text="Metres and Inches", bg=m_and_ft_button_colour, padx=10, pady=10)
        self.m_and_ft_converter_button.grid(row=1,column=1)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()                                 