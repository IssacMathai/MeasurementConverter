from tkinter import *
from functools import partial 
import random

class Welcome_Screen:
    def __init__(self, partner):
        
        # Formatting variables
        background_color = "light blue"
        
        # Welcome Screen GUI
        self.welcome_screen_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.welcome_screen_frame.grid()

        # Main Heading (row 0)
        self.measurement_welcome_screen_label = Label(self.welcome_screen_frame, text="Measurement Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.measurement_welcome_screen_label.grid(row=0)

        # Metres and Feet Button (row 1)
        self.m_and_ft_welcome_screen_button = Button(self.welcome_screen_frame, text="Metres and Feet", font=("Arial", "14"), command=self.Metres_and_Feet_Converter, padx=10, pady=10)
        self.m_and_ft_welcome_screen_button.grid(row=1)

    def Metres_and_Feet_Converter(self):
        get_Metres_and_Feet_Converter = Metres_and_Feet_Converter(self)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()