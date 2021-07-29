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

        # Centimetres and Inches Button (row 1)
        self.cm_and_in_welcome_screen_button = Button(self.welcome_screen_frame, text="Centimetres and Inches", font=("Arial", "14"), command=self.Centimetres_and_Inches_Converter, padx=10, pady=10)
        self.cm_and_in_welcome_screen_button.grid(row=1)

    def Centimetres_and_Inches_Converter(self):
        get_Centimetres_and_Inches_Converter = Centimetres_and_Inches_Converter(self)

class Centimetres_and_Inches_Converter:
    def __init__(self, partner):

        # Formatting variables
        background = "lime green"

        # Disable Centimetres and Inches button while window is open
        partner.cm_and_in_welcome_screen_button.config(state=DISABLED)

        # Centimetres and Inches Converter child window
        self.cm_and_in_box = Toplevel()

        # If users press cross at top, closes window and re-enables Centimetres and Inches button
        self.cm_and_in_box.protocol('WM_DELETE_WINDOW', partial(self.close_Centimetres_and_Inches_Converter, partner))

        # GUI Frame
        self.cm_and_in_frame = Frame(self.cm_and_in_box, bg=background)
        self.cm_and_in_frame.grid()

        # Centimetres and Inches Converter heading (row 0)
        self.cm_and_in_heading = Label(self.cm_and_in_frame, text="Centimetres and Inches Converter",
                                 font="arial 18 bold", bg=background, padx=10, pady=10)
        self.cm_and_in_heading.grid(row=0)

        # Help Button
        self.help_button = Button(self.cm_and_in_frame, text="Help", font=("Arial", "14"), command=self.Help, padx=10, pady=10)
        self.help_button.grid(row=1)

    def close_Centimetres_and_Inches_Converter(self, partner):
        # Put "Centimetres and Inches" button in welcome screen back to normal... 
        partner.cm_and_in_welcome_screen_button.config(state=NORMAL)
        self.cm_and_in_box.destroy()

    def Help(self):
        get_Help = Help(self)



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()