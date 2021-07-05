from tkinter import *
from functools import partial 
import random

class Welcome_Screen:
    def __init__(self,partner):
        
        # Formatting variables...
        background_color = "light blue"
        
        # Welcome Screen GUI...
        self.welcome_screen_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.welcome_screen_frame.grid()

        # Main Heading (row 0)
        self.temp_welcome_screen_label = Label(self.welcome_screen_frame, text="Measurement Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.temp_welcome_screen_label.grid(row=0)

        # Centimetres and Inches Button (row 1)
        self.cm_and_in_welcome_screen_button = Button(self.welcome_screen_frame, text="Centimetres and Inches", font=("Arial", "14"), command=self.Centimetres_Inches_Converter, padx=10, pady=10)
        self.cm_and_in_welcome_screen_button.grid(row=1)

    def Centimetres_Inches_Converter(self):
        open_cm_in_converter = Centimetres_Inches_Converter(self)

class Centimetres_Inches_Converter(self,partner):
    def __init__(self, partner):
        background = "orange"

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.Centimetres_Inches_Converter, bg=background)
        self.help_frame.grid()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()
