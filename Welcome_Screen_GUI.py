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
        self.welcome_screen_frame = Frame(width=200, height=200, bg=background_colour, pady=10)
        self.welcome_screen_frame.grid()

        # Main Heading (row 0)
        self.measurement_welcome_screen_label = Label(self.welcome_screen_frame, text = "Measurement Converter", font=("Arial", "20", "bold"), bg=background_colour, padx=10, pady=10)
        self.measurement_welcome_screen_label.grid(row=0)

        # Welcome Screen Buttons Frame
        self.welcome_screen_buttons_frame = Frame(self.welcome_screen_frame)
        self.welcome_screen_buttons_frame.grid(row=1, pady=10)

        # Centimetres and Inches Button (row 1)
        self.cm_and_in_welcome_screen_button = Button(self.welcome_screen_buttons_frame, text="Centimetres and Inches", bg=cm_and_in_button_colour, padx=10, pady=10)
        self.cm_and_in_welcome_screen_button.grid(row=1, column=0)

        # Metres and Feet Button (row 1)
        self.m_and_ft_welcome_screen_button = Button(self.welcome_screen_buttons_frame, text="Metres and Inches", bg=m_and_ft_button_colour, padx=10, pady=10)
        self.m_and_ft_welcome_screen_button.grid(row=1,column=1)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()                                 